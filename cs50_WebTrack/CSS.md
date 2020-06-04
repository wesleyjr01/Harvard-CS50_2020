# CSS
* Add some styling to the html files.
* You can add a ```<style>``` tag inside the html file, right inside the ```<head>``` tag, something like this:
```
    <head>
        <title>
            Hello!
        </title>
        <style>
            h2{
                text-align: center;
                color: blue;
            }
        </style>
    </head>
```
* **Class**: A Class describes a category of html elements, that all should be styled in similar way, they don't all need to be ```<h1>``` or all ```<h2>```, it could be any elements, but it's a way of giving a name to a particular category or class of elements, such that they can be styled acording to particular rules. Example:
```
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>
            Hello!
        </title>
        <style>
            .title{
                text-align: center;
                color: red;
            }
        </style>
    </head>
    <body>
        <h1 class="title">Hello, world!</h1>

        <h2 class="title">Subsection 1</h2>

        <p>This is some text.</p>

        <h2 class="title">Subsection 2</h2>

        <p>This is some more text.</p>
    </body>
</html>
```
* We can also have more than one class on each html element, like this:
```
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>
            Hello!
        </title>
        <style>
            .title{
                text-align: center;
                font-family: sans-serif;
            }

            .green{
                color: green;
            }
            
        </style>
    </head>
    <body>
        <h1 class="title green">Hello, world!</h1>

        <h2 class="title green">Subsection 1</h2>

        <p class="green">This is some text.</p>

        <h2 class="title green">Subsection 2</h2>

        <p class="green">This is some more text.</p>
    </body>
</html>
```
* As this goes, our html file tends to get too long, and so we should split our css code in another file, for example, creating another file called **styles.css**, and isolate our css like this:
```
.title
{
    text-align: center;
}

.green
{
    color: green;
}
```
* Then, on your html page, you call the css file like this:
```
    <head>
        <title>
            Hello!
        </title>
        <link rel="stylesheet" href="styles.css">
    </head>
```
* CSS Libraries: **Bootstrap**. You can go to the bootstrap page, and copy a reference on you ```<head>``` section to the bootstrap code:
```
    <head>
        <title>
            Table Example!
        </title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    </head>
```