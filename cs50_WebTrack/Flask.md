# Flask
* So far, we’ve learned how to write webpages that are saved as a file and returned by an HTTP server. But we can also have web servers, or applications, that generate content dynamically before returning it as a response.
* We’ll use a framework in Python called Flask, which allows us to write a web server with many features.
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"
```
* In a ```<form>``` field, using the **action** we can define a route we are taken to, when the form is submitted: ```<form action="/hello">```
    * When we submit this form, it will submit a request to route ```/hello```, and then the ```/hello``` route will figure out what to do with this request.
* Also, we have to declare the field **name** inside **form** to be able to acess what the user typed in:
```
<form action="/hello">
    <input name="name" type="text">
    <input type="submit">
</form>
```
* We write a form that has a name input, and write a route function that gets the input with request.args.get(), and returns a template with the input substituted in.
* It turns out that we can have templates for our templates, since many of our pages might have similar HTML code around its content. We’ll create layout.html, and add a special block inside the ```<body>``` tag. Then, our other files like index.html can use the template with extends "layout.html", and only have the content block for the body.
* Send data, by a ```<form>```, to the route **/add**, with a method **POST**:
```
<form action="/add" method="post">
    <input name="task" type="text" placeholder="Task Name">
    <input type="submit">
</form>
```
* We we handle request with something like this:
```
@app.route("/")
def tasks():
    return render_template("tasks.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("task")
        todos.append(todo)
        return redirect("/")
```