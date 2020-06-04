# JS
* In order to develop more interactive WebPages, we have to introduce a programming language, JavaScript. A programming language that our WebBrowsers are able to know, interprete and understand so that JavaScript code can actually run inside the of the Browser, alongside a WebPage that you'll be displaying to user.
* Let's take a look between similarities and differences between JavaScript and C:   
```
// C
int counter = 0;

// JavaScript
let counter = 0;
```

```
// C
counter = counter + 1;

// JavaScript
counter = counter + 1;

// Both
counter++;
```

```
// C
if (x < y)
{

}
else if (x > y)
{
    
}
else
{
    
}

// JavaScript
if (x < y)
{

}
else if (x > y)
{
    
}
else
{

}
```

```
// C
while(true)
{

}

// JavaScript
while(true)
{

}
```

```
// C
for (int i = 0; i < 50; i++)
{

}

// JavaScript
for (let i = 0; i < 50; i++)
{

}
```

```
// C
void cough(int n)
{

}

// JavaScript
function cough(n)
{

}
```
* **Document Object Model**: graphical representation of the hierachy inside the html. JavaScript is powerfull because it has the ability to manipulate the **DOM**.
* First JS Example, using the alert() fuction.
```
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>Hello!</title>
        <script>
            function greet()
            {
                let name = document.querySelector('#name').value;
                if (name === '')
                {
                    name = 'world';
                }
                alert('Hello, ' + name + '!');
            }
        </script>
    </head>
    <body>
        <form onsubmit="greet(); return false;">
            <input type="text" id="name">
            <input type="submit">
        </form>
    </body>
</html>
```
* We can use the JavaScript to change the DOM.
* **Callback Function** : function that should be called after we get some information.