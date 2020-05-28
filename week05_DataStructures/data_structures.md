# Shorts - Data Structures
* By this point we've now examined four different ways to store sets of data:
    * Arrays
    * Linked lists
    * Hash tables
    * Tries

* There are even some variations on these (trees and heaps, quite similar to tries, stacks and queues quite similar to arrays or linked lists, etc,) but this will generally cover most of what we're looking at this in C.
---
### Arrays
* Insertion is bad - lots of shifting to fit an element in the middle.
* Deletion is bad - lots of shifting after removing an element,
* Lookup is great - random acess, constant time.
* Relatively easy to sort.
* Relatively small size-wise.
* Stuck with a fixed size, no flexibility.
---
### Linked List
* Insettion is easy - just tack onto the front
* Deletion is easy - once you find the element
* Lookup is bad - have to rely on linear search
* Relatively difficult to sort - unless you're willing to compromise on super-fast insertion and instead sort as you construct
* Relatively small size-wise(not as small as arrays)
---
### Hash tables
* Insertion is two-step process - hash, then add
* Deletion is easy - once you find the element
* Lookup is on average better than with liked lists because you have the benefit of a real-world constant factor
* Not an ideal data structure if sorting is the goal - just use an array
* Can run the gamut of size
---
### Tries
* Inserting is complex - a lot of dynamic memory allocation, but gets easier as you go
* Deletion is easy - just free a node
* Lookup is fast - not quite as fast as an array, but almost
* Already sorted - sorts as you build in almost all situations
* Rapidly becomes huge, even with very little data present, not great if space is at a premium