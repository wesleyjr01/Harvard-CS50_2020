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
* Classification of Algorithms, **O** stands for Order Of for worst case cenario, the **upper bound** of how many steps an algorithm might take:
    * O(n²) 
    * O(n log n) 
    * O(n) <- linear search
    * O(log n) <- binary search
    * O(1)
* The **Ω** simbol is the opposite of Big O **O**, is the **lower bound** of how many steps an algorithm might take:
    * Ω(n²) 
    * Ω(n log n) 
    * Ω(n) <- count search
    * Ω(log n) 
    * Ω(1) <- linear search, binary search

---  

  
# Introduction of our own custom types
* We will use structures with they keyword **struct**. We will define it with:
```
typedef struct
{}
```