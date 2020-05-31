# Hexadecimal Representation
* Order: 
```
0, 1, 2, 3, 4, 5, 6, 7,  
8, 9, A, B, C, D, E, F.
```
* In binary, we were usings powers of 2, in hexadecimal we will use powers of 16.
* In hexadecimal, ```10``` is sixteen.
* RGB are represented in hexadecimal digits. ``` 00 00 00 | RR GG BB```:
    * ``` FF 00 00 ``` : a lot of red, no green, no blue.
    * ``` FF FF FF ``` : white.
    * ``` 00 00 00 ``` : black.
* This hexadecimal representation can get quite confusing, because we can confuse de deciaml number 12 to the **hexadecimal number 12 (which is 18 in decimal)**. So we made the following convention, when working with hexadecimal numbers we add a **0x** before the numbers:
```
0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7,
0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF,
0x10, 0x11 ...
```
* In **c**, **&** means **the address of** operator.
* When we create a a string called "EMMA", we are atually storing the following:
```
E M M A \0
```
* if we say ```string s = "EMMA"```, **s** will be a pointer to the first byte array of characters:
``` 
string s = "EMMA";
is equal to
char *s = "EMMA";
```
* Lets construct the string type:
```
typedef char *string;
```