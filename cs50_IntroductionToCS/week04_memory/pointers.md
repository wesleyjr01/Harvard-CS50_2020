# Pointers
* Pointers are just addresses!
* Pointers provide an alternative way to pass data between functions.
    * Recall that up to this point, we have passed all data by value, with one exception.
    * When we pass data by value, we only pass a copy of that data.
* If we use pointers instead, we have the power to pass the actual variable itself.
    * That means that a change that is made in one function can impact what happens in a different function.
    * Previously, this wasn't possible!
* A **pointer**, then, is a data item whose.
    * *value* is a memory address
    * *type* describes the data located at that memory address
* As such, pointers allow data structures and/or variables to be shared among functions.
* The simples pointer available to us in C is the **NULL pointer**.
    * AS you might expect, this pointer points to nothing (a fact which can actually come in handy!)
* When you create a pointer and you don't set its value immediatly, you should **always** set the value of the pointer to NULL.
* Another easy way to create pointers is to simply **extract** the address of an already existing variable. We can do this with the **address extraction operator &**.
    * If **x** is an int-type variable, then **&x** is a pointer-to-int whose value is the address of **x**.
* If **arr** is an array of doubles, then **&arr[i]** is a pointer-tp-double who value is the address of the ith element of **arr**.
    * **An array's name, then, is actually just a pointer to its first element - you've been working with pointers all along!**
---
* Summary:
```
int* p;
```
* The value of **p** is an address.
* We can dereference **p** with the **\*** operator.
* If we do, what we'll find at that location is an int.