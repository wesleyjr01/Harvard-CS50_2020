# Algorithms
* Linear Search: without some sorting, this is genreally the way to go. See an example of linear search trying to find an element with name 50.
```
For i from 0 to n-1
    If i'th element is 50
        Return true
Return false
```
* Binary Search: with sorted elements, binary seach makes a lot of sense. See an example of linear search trying to find an element with name 50, knowing that there is an sorting:
```
If no items
    Return false
If middle is 50
    Return true
Else if 50 < middle item
    Search left half
Else if 50 > middle item
    Search right half
```
---
# Classification of Algorithms
* Classification of Algorithms, **O** stands for Order Of for worst case cenario, the **upper bound** of how many steps an algorithm might take:
    * **O(n²)** &#8592; selection sort
    * **O(n log n)** merge sort
    * **O(n)** &#8592; linear search
    * **O(log n)** &#8592; binary search
    * **O(1)**
* The **Ω** simbol is the opposite of Big **O**, is the **lower bound** of how many steps an algorithm might take:
    * **Ω(n²)**  &#8592; bubble sort, selection sort
    * **Ω(n log n)** &#8592; merge sort
    * **Ω(n)** &#8592; bubble sort
    * **Ω(log n)** 
    * **Ω(1)** &#8592; linear search, binary search
* The last notation is **Θ**, which denotes that the algorithm has the same upper bound and lower bound:
    * **Θ(n²)**  &#8592; selection sort
    * **Θ(n log n)** &#8592; merge sort
    * **Θ(n)** &#8592; 
    * **Θ(log n)** 
    * **Θ(1)** &#8592; 
---  

  
# Introduction of our own custom types
* We will use structures with they keyword **struct**, which is a container in which you can put many data types. We will define it with:
```
typedef struct
{
    type varname1;
    type varname2;
}
structname;

// Example
typedef struct
{
    string name;
    string number;
}
person;

```
# Sorting Cost
* How expansive is it to sort a set of numbers? There should be a tradeoff between sorting the numbers and then doing a binary search, or dont sort them and just go on a linear search.
Pseudocode of a **bubble sort** algorithm:
```
Repeat n-1 times until no swap
    For i from 0 to n-2
        if i'th and i+1'th elements out of order
            Swap them
```
* How many steps did it take, what is the **O** of this algorithm, what's the running time of this algorithm?
    * The answer is: **(n-1)x(n-2)**, which is **n²-3n+2**.
    * So the dominating factor of this algorithm is **n²**. So the order of this algorithm, **O** is **O(n²)**.
---
# Selection Sort
* Lets try a different approach for sorting, since the bubble sort is very costly. We will do now **Selection sort**. Let's see it's pseudocode:

```
Repeat until no sorted elements remain:
    Search the unsorted part of the data to find the smallest value
    Swap the smallest found value with the first element of the unsorted part
```   
* That leads us to **n(n+1)/2** steps, which is is in the order of n2, so **O(n²)**.
---
# Recursion
* Implement an algorithm that calls itself. We define a recursive function, if we reference it's own name in its own code.
* Every recursive function has two cases that could apply, given any input:
    * The *base case*, which when triggered will terminate the recursive process.
    * The recursive case, which is where the recursion will actually occur.
* In general, but not always, recursive functions replace loops in non-recursive functions.
---
# Merge Sort
```
If only one item
    Return
Else
    Sort left half of items
    Sort right half of items
    Merge sorted halves
```
* The order of this algorthm is **O(n log n)**.