# Data Structures (Notes)
---
### Linked List
* Inserting additional numbers into array:
    * **O(n)** <- insert
* Linked Lists. By using Linked Lists, we lost random acess to elements, so we can do no longer binary search.
    * **O(n)** <- search, insert
---
### Trees
* **Binary Search Trees**. we can achieve this more or less like a linked lists, but using two pointers in the structure:
```
typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;
```
* Every node has at most two children.
* **Recursive definition:** For any node in the tree, every element to the left is smaller than it, and every element to the right is greater than it.
* Now we have back binary search.
* Implementing binary seach now:
```
bool search(node *tree)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (50 < tree->number)
    {
        return search(tree->left);
    }
    else if (50 > tree->number)
    {
        return search(tree->right);
    }
    else if (50 == tree->number)
    {
        return true;
    }
}
```
* Now with binary search in a tree:
    * **O(log n)** <- search, insert
---
###  Hash Table
* A hash table is a combination of an array and linked list inside of it. Vertically, it is an array, and horizontally, it is a linked list.
* In a Hash table, we index into using a Hash Function. One way a hash function could work, is by looking at the first two letters, or three letters. The more letters we use to look at, creating new buckets, the more memory in the vertical array we will need, so there will be a tradeoff.
    * **O(1)** <- search, best case
    * **O(n)** <- search, worst case
---
### Tries
* A Trie is a tree, each of whose nodes is essentially an array.
* To store a name in a Trie, we have to look at every word in the name.
* **O(k)** <- search, insert
* So, now the search and insert time becomes a constant(super fast). but we consume a lot of memory.
---
### Queue
* Data structure that is a FIFO, First In, First Out.
* Two fundamental operations:
    * Enqueue.
    * Dequeue.
---
### Stacks
* Data structure which is sort of the opposite of Queues.
* Unlike FIFO for Queues, in this data structure it is Last In, First out.
* G-mail for example.
* Operations:
    * Push (always from the top)
    * Pop (always from the top)
---
### Dictionary (S2)
* A Dictionary is the abstraction that you can get on the top of a HashTable.
* A Dictionary is a Data Structure that has keys, and values.