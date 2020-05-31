# SQL
* Often times, in order for us to build the most functional website we can, we depend on a **database** to store information.
* SQL( the *Structured Query Language*) is a programming language whose purpose is to **query** a database.
* **MySQL** is one open-source platform on which you can establish the type of relational database that SQL is most adept at working with.
    * **SQLite** is another, which we've actually use in CS50 since 2016.
* Many installations of SQL come with a GUI tool called **phpMyAdmin** which can be used to execute database queries in a more user-friendly way.
* After you create a database, the next thing you'll most likely want to do is create a **table**.
    * Then  syntax for doing this is actually a bit awkward to do programmatically, at least at the outset, and so this is where phpMyAdmin will come handy.
* As part of the process of creating a table, you'll be asked to specify all of the **columns** in that table.
* Thereafter, all your queries will refer to **rows** of that table.
* Unlike in C, the CHAR data type in SQL does not refer to a single character. Rather, it is a fixed-lenght string.
    * In most relational databases, including MySQL, you actually specify the fixed-lenght as part of the type definition, e.g. CHAR(10).
* A VARCHAR refers to a variable-lenght string.
    * VARCHARs also require you to specify the **maximum** possible length of a string that could be stored in that column, e.g. VARCHAR(99).
* SQLite has these data types as well, but affiliates each with a "type affinity" to simplify things.   
``` NULL | INTEGER | REAL | TEXT | BLOB ```
* One other important consideration when constructing a table in SQL is to choose one column to be your **primary key**.
* Primary keys enable rows of a table to be uniquely and quickly identified.
    * Choosing your primary key appropriately can make subsequent operations on the table much easier.
* SQL is a programming language, but its vocabulary is fairly limited.
* We will primarily consider just **four** operations that one may perform on a table.   
    * **INSERT**: insert elements into a table:   
``` INSERT INTO <table> (<columns>) VALUES (<values>)```   
``` INSERT INTO users (username, password, fullname) VALUES ('newman', 'USMAIL', 'Newman')```
    * When defining the column that ultimately ends up being your table's primary key, it's usually a good ideia to have that column be an integer. Moreover, so as to eliminate the situation where you may accidentally forget to specify a real value for the primary key column, you can configure that column to **autoincrement**, so it will pre-populate that column for you automatically when rows are added to the table.
    * **SELECT**: Extract information from a table.   
``` SELECT <columns> FROM <table> WHERE <condition> ORDER BY <column> ```
    * **SELECT (JOIN)** : Extract information from multiple tables.   
``` SELECT <columns> FROM <table1> JOIN <table2> ON <predicate> ```   
``` SELECT users.fullname, moms.mother FROM users JOIN moms ON users.username = moms.username```
    * **UPDATE**: Modify information in a table.   
``` UPDATE <table> SET <column> = <value> WHERE <predicate> ```
    * **DELETE**: Remove information from a table.   
``` DELETE FROM <table> WHERE <predicate> ```