# File Pointers
* Implementing a file to store our information after the program ends.
* The ability to read data from and write data to files is the primary means of storing **persistent data**, data that does not disappear when your program stops running.
* The abstraction of files that C provides is implemented in a data structure known as **FILE**.
    * Almost universally when working with files, we will be using pointers to them, FILE*.
---
* The file manipulation functions all live in stdio.h
    * All of them accept FILE* as one of their parameters, except for the function ```fopen()```, which is used to get a file pointer in the first place.
* Some of the most common file input/output(I/O) functions that we'll be working with are:
* ```fopen(), fclose(), fgetc(), fputc(), fread(), fwrite().```
---
* ```fopen()```:
    * Opens a file and returns a file pointer to it.
    * Always check the return value to make sure you don't get back NULL.
    * ``` FILE* ptr = fopen(<filename>, <operation>); ```
    * ``` FILE* ptr1 = fopen("file1.txt", "r"); ```
    * ``` FILE* ptr2 = fopen("file2.txt", "w"); ```
    * ``` FILE* ptr3 = fopen("file3.txt", "a"); ```
---
* ```fclose()```
    * Closes the file pointed to by the given file pointer.
    * ``` fclose(<file pointer>);
---
* ```fgetc()```
    * Reads and returns the next character from the file pointed to.
    * Note: The operation of the file pointer passed in as parameter must be "r" for read, or you will suffer an error.
    * ```char ch = fgetc(<file pointer>);```
    * The ability to get single characters from files, if wrapped in a loop, means we could read all the characters from a file and print them to the screen, one-by-one, essentially:

    ```
    char ch;
    while ((ch = fgetc(ptr)) != EOF)
        printf("%c", ch);
    ```
---
* ```fputc()```
    * Writes or appends the specified character to the pointed-to file.
    * Note: The operation of the file pointer passed in as the parameter must be "w" for write or "a" for append, or you will suffer an error.
    * ``` fputc(<character>, <file pointer>);```
    * ``` fputc("A", ptr2);```
    * Now we can read characters from files and write characters to them. Let's extend our previous example to copy one file to another, instead of printing to the scree.
    ```
    char ch;
    while((ch = fget(ptr)) != EOF)
        fputc(ch, ptr2);
---
* ```fread()```
    * A generic version of fgetc(), allowing to get a large amount of information.
    * ```fread(<buffer>, <size>, <qty>, <file pointer>);```
```
int arr[10];
fread(arr, sizeof(int), 10, ptr);

// read from arr2, store in ptr
double* arr2 = malloc(sizeof(double) * 80);
fread(arr2, sizeof(double), 80, ptr);
```
---
* ``` fwrite()```
    * ```fwrite(<buffer>, <size>, <qty>, <file pointer>);```

```
int arr[10];
fwrite(arr, sizeof(int), 10, ptr);
```