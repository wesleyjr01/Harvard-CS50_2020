import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash, safe_str_cmp
from dotenv import load_dotenv

from helpers import apology, login_required, lookup, usd

load_dotenv()

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Create a New Table for USERS if Not Exists Already
def_user = """
CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
hash TEXT,
cash REAL DEFAULT 10000)
"""
db.execute(def_user)

# Create a New Table for BUYS if Not Exists Already
def_buys = """
CREATE TABLE IF NOT EXISTS buys
(id INTEGER PRIMARY KEY AUTOINCREMENT,
symbol TEXT,
shares INT,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
user_id INT, FOREIGN KEY(user_id) REFERENCES users(id))
"""
db.execute(def_buys)

# Create a New Table for SELLS if Not Exists Already
def_sells = """
CREATE TABLE IF NOT EXISTS sells
(id INTEGER PRIMARY KEY AUTOINCREMENT,
symbol TEXT,
shares INT,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
user_id INT,
FOREIGN KEY(user_id) REFERENCES users(id))
"""
db.execute(def_sells)

# Create a New Table for HISTORY if Not Exists Already
def_history = """
CREATE TABLE IF NOT EXISTS history
(id INTEGER PRIMARY KEY AUTOINCREMENT,
symbol TEXT,
shares INT,
operation_type TEXT,
share_price_old REAL,
total_cost_old REAL,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
user_id INT,
FOREIGN KEY(user_id) REFERENCES users(id))
"""
db.execute(def_history)

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    query = """
    SELECT h.symbol, SUM(h.shares) as 'shares', u.cash
    FROM history h
    JOIN users u ON u.id = h.user_id
    WHERE h.user_id = :user_id
    GROUP BY h.symbol
    HAVING SUM(h.shares)>0
    """

    rows = db.execute(query, user_id=session["user_id"])
    acum_stocks_price = 0
    for row in rows:
        lk = lookup(row["symbol"])
        current_stock_price = lk["price"]
        stock_name = lk["name"]
        total_stocks_price = current_stock_price*row['shares']
        acum_stocks_price += total_stocks_price
        row["name"] = stock_name
        row["current_stock_price"] = usd(current_stock_price)
        row["total_stocks_price"] = usd(total_stocks_price)

    cash_row = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    cash = cash_row[0]["cash"]
    acum_stocks_price = acum_stocks_price
    total_patrimony = cash + acum_stocks_price

    return render_template("index.html",
                                rows=rows,
                                cash=usd(cash),
                                acum_stocks_price=usd(acum_stocks_price),
                                total_patrimony=usd(total_patrimony))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        shares = int(shares) if shares.isdigit() else ''

        # Make Sure Symbol os neighther Empty or Invalid
        if (symbol == '') or (lookup(symbol) is  None):
            return apology("Bad Stock Symbol.")

        # Make sure to that Shares is a digit
        elif not str(shares).isdigit():
            return apology("Bad shares format, insert a positive integer.")

        # Make Sure Shares is a Positive Integer
        elif (shares <= 0) or (shares % 2 not in [0 ,1]):
            return apology("Bad shares format, insert a positive integer.")
        else:
            price = lookup(symbol)["price"]
            rows = db.execute("SELECT * FROM users WHERE id = :id",
                          id=session["user_id"] )
            available_cash = rows[0]["cash"]
            buy_price = price * shares
            if buy_price > available_cash:
                return apology("Not enough Money.")
            else:
                # Register this BUY Action in the BUY TABLE
                register_in_buy = """
                INSERT INTO buys (symbol, shares, user_id)
                VALUES (:symbol, :shares, :user_id)
                """
                db.execute(register_in_buy,
                              symbol=symbol,
                              shares=shares,
                              user_id=session["user_id"])

                # Register this BUY Action in the HISTORY TABLE
                register_in_history = """
                INSERT INTO history (symbol, shares, operation_type, share_price_old, total_cost_old, user_id)
                VALUES (:symbol, :shares, :operation_type, :share_price, :total_cost, :user_id)
                """
                db.execute(register_in_history,
                              symbol=symbol,
                              shares=+1*shares,
                              operation_type="BUY",
                              share_price=price,
                              total_cost=buy_price,
                              user_id=session["user_id"])

                # Update the Amount of Cash of User in the USER TABLE
                update_user = """
                UPDATE users SET cash = :remaining_cash WHERE id = :user_id
                """
                db.execute(update_user,
                            remaining_cash=available_cash - buy_price,
                            user_id=session["user_id"])

                flash(f"Bought {symbol} stocks successfully!")
                return redirect("/")
    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    query = """
    SELECT *
    FROM history
    WHERE user_id = :user_id
    ORDER BY time ASC
    """

    rows = db.execute(query, user_id=session["user_id"])

    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        find_user = """
        SELECT * FROM users WHERE username = :username
        """
        rows = db.execute(find_user,
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash('You were successfully logged in')
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        json_response = lookup(symbol)
        name = json_response["name"]
        symbol = json_response["symbol"]
        price = usd(json_response["price"])
        if json_response is None:
            return apology("Stock not found.")
        return render_template("quoted.html", name=name, symbol=symbol, price=price)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 403)

        # Ensure password and confirmation match
        elif not safe_str_cmp(request.form.get("password"), request.form.get("confirmation")):
            return apology("password and confirmation must match", 403)

        else:
            # Query database for unique username check
            rows = db.execute("SELECT * FROM users WHERE username = :username",
                              username=request.form.get("username"))
            if len(rows) != 0:
                return apology("This username is already taken.", 403)
            else:
                db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                                              username=request.form.get("username"),
                                              hash=generate_password_hash(request.form.get("password")))

                # Remember which user has logged in
                rows = db.execute("SELECT * FROM users WHERE username = :username",
                                    username=request.form.get("username"))
                session["user_id"] = rows[0]["id"]

                # Redirect to Login page
                flash("Registration succeded!")
                return redirect("/")


    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    query="""
    SELECT symbol, SUM(shares) as 'sum_shares'
    FROM history
    WHERE user_id = :user_id
    GROUP BY symbol
    HAVING SUM(shares)>0
    """
    rows = db.execute(query, user_id=session["user_id"])
    symbols = [row["symbol"] for row in rows]

    if request.method == "POST":
        # Try to convert requested shares into integer
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Insert a integer number of shares.")

        symbol = request.form.get("symbol")

        # Make sure the user selected a stock
        if symbol is '':
            return apology("Select a Stock Symbol.")

        # Make sure to pick a stock which the user have shares
        elif symbol not in symbols:
            return apology("Select a Stock Symbol which you have Shares.")

        # Make sure the user inputed a positive integer number of shares to sell
        elif shares < 0:
            return apology("Select a positive integer number of Shares to Sell.")

        else:
            sum_shares = [row.get("sum_shares") for row in rows if row.get("symbol") == symbol][0]

            # Make sure the user have enough shares to sell
            if sum_shares < shares:
                return apology(f"You currently have only {sum_shares} to sell.")
            else:
                price = lookup(symbol)["price"]
                sell_price = price * shares

                # Register this SELL Action in the SELL TABLE
                register_in_sell = """
                INSERT INTO sells (symbol, shares, user_id)
                VALUES (:symbol, :shares, :user_id)
                """
                db.execute(register_in_sell,
                              symbol=symbol,
                              shares=shares,
                              user_id=session["user_id"])

                # Register this SELL Action in the HISTORY TABLE
                register_in_history = """
                INSERT INTO history (symbol, shares, operation_type, share_price_old, total_cost_old, user_id)
                VALUES (:symbol, :shares, :operation_type, :share_price, :total_cost, :user_id)
                """
                db.execute(register_in_history,
                              symbol=symbol,
                              shares=-1*int(request.form.get("shares")),
                              operation_type="SELL",
                              share_price=price,
                              total_cost=sell_price,
                              user_id=session["user_id"])

                # Update the Amount of Cash of User in the USER TABLE
                query_cash = "SELECT cash FROM users WHERE id = :id"
                row_cash = db.execute(query_cash, id=session["user_id"])
                available_cash = row_cash[0]["cash"]

                # Update the amount of cash available for the user.
                update_user = """
                UPDATE users SET cash = :remaining_cash WHERE id = :user_id
                """
                db.execute(update_user,
                            remaining_cash=available_cash + sell_price,
                            user_id=session["user_id"])

                flash(f"Sold {shares} shares from {symbol} successfully!")
                return redirect("/")

    else:
        return render_template("sell.html", rows=rows)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
