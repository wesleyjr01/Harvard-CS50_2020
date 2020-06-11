# Databases
* So far, we’ve learned how to write a server that can respond with webpages that are the same for every user. But there are websites where we can log in, and it will show us information specific to us.
* Recall that cookies are small files that websites ask our browser to store on our computer, with some kind of identifier that our browser shows the website the next time we go there, so the website knows who we are. This allows our server to have sessions, or data for users’ interactions with a website, specific to each of them.
* We’ll look at the task list application we made last time. Since our task list was stored in a global variable in our server application, everyone who visits our page will see the same list.
* To solve this, we can use sessions from Flask, by importing and initializing their implementation. By doing so, our tasks() function can look in the global session variable, and read, set, or update a todos key within it. Flask will take care of making sure that the global session variable is actually specific to the user who made that request, by storing and checking some cookies.
* If we want to store more complex data, it would make more sense to use a database instead of session objects. So we’ll create a new application to store registration information, like names and emails.
* We’ll make a new empty file, lecture.db, and run sqlite3 lecture.db to create a table and set column names and types for the data we think we’ll need.
* Using sqlite3:
```
CREATE TABLE 'registrants' (
                'id' INTEGER PRIMARY KEY,
                'name' VARCHAR(255),
                'email' VARCHAR(255)
                );
```
```
INSERT INTO registrants (name, email) VALUES ('Alice', 'alice@example.com');
```
* In sqlite3, we can run queries to select or insert into the table to check that everything works. In our new Flask application, we’ll import the SQL library from CS50 so we can work with our database more easily, and establish a connection to our lecture.db file. In our / route, we can run a SELECT query to get the rows from our registrants table, and pass them into our template. Our template will in turn iterate over each row, and generate an <li> item with the values of each column in each row.