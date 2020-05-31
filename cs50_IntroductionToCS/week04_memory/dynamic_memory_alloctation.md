# Dynamic Memory Allocation
* We can use pointers to get access to a block of **dynamically-allocated memory** at runtime.
* Dynamically allocated memory comes from a pool of memory known as the **heap**.
* Prior to this point, all memory we've been working with has been coming from a pool of memory known as the **stack**.
* We get this dynamically-allocated memory by making a call to the C standard library function malloc(), passing as its parameter the number of bytes requested.
* After obtaining memory for you (if it can), malloc() will return a pointer to that memory.
* What if malloc() can't give you memory? It'll hand you back NULL.
    * So every time you call malloc(), you need to check if it is not NULL, because if further you do dereference to this pointer, you will suffer a **segmentation fault**.
```
// statically obtain an integer
int x;

// dynamically obtain an integer
int *px = malloc(sizeof(int));

// array of floats on the stack
float stack_array[x];

// array of float on the heap
float* heap_array = malloc(x * sizeof(float));
```
* Here's the trouble: Dynamically-allocated memory is not automatically returned to the system for later use when the function in which it's created finishes execution.
* Failing to return memory back to the system when you're finished with it results in a **memory leak** which can compromise your system's performance.
* When you finish working with dynamically-allocated memory, you must free() it.