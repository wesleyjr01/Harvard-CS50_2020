# Python
* Released in 1991.
* Python is heavily inspered by C.
* Instead of arrays, we have lists.
* **Tuples**:
    * Tuples are ordered, immutable sets of data; they are great for associating collections of data, sort of like a struct in C, but where those values are unlikely to change.
* **Dictionaries**
    * Python also has a built in support for **dictionaries**, allowing you to specify list indices with words or phrases (keys), instead of integers, which you were restricted to in C.
    * But this creates a somewhat new problem... how do we iterate through a dictionary? We don't have indexes ranging from [0, n-1] anymore:
        * ```for pie in pizzas:```   
                ```#use pie in here as a stand-in for "i"```
* Like C, if you wish to define a ```main``` function, you must at the very end of your code have:
```
if __name__ == "__main__":
    main()
```
---
# Objects
* Python is an object-oriented programming language.
* An object is sort of analogous to a C structure.
* C structures contain a number of *fields*, which we might also call *properties*.
    * But the properties themselves can not ever stand on their own.
* Objects, meanwhile, have properties but also *methods*, or functions that are inherent tot he object, and mean nothing outside of it. You define the methods inside the objects also.
    * Thus, properties and methods don't ever stand on their own.
* You define a type of object using the *class* keyword in Python.
* Classes require an initialization function, also more-generally known as *constructor*, which sets the starting values of the properties of the object.
* In defining each method of an object, self should be its first parameter which stipulates on what object the method is called.