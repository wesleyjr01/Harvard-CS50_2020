# Shorts - Singly-Linked Lists
* So far in the course, we've only had one kind of data structure for representing collections of like values (array).
    * *strucs*, recall, give us "containers" for holding variables of different data types, typically.
* Arrays are great for element lookup, but unless we want to insert at the very end of the array, inserting elements is quite costly - remember insertion sort?
* Arrays also suffer from a great inflexibility - what happens if we need a larger array than we thought?
* Though **clever use of pointers, dynamic memory allocation, and structs**, we can put the pieces together to develop a new kind of data structure that gives us the ability to grow and shrink a collection of like values to fit our needs.
* We call this combination of elements, when used in this way, a **linked list**.
* A linked list **node** is a special kind of struct with two members:
    * Data of some data type (int, char, float...)
    * A pointer to another node of the same type

* In this way, a set of nodes together can be thought of as forming a chain of elements that we can follow from beggining to end.
```
typedef struct sllist
{
    VALUE val;
    struct sslist* next;
}
sllnode;
```
* In order to work with linked lists effectively, there are a number of operations that we need to understand:
    1) Create a linked list when it doen't already exist.
    2) Search though a linked list to find an element.
    3) Insert a new node into the linked list.
    4) Delete a single element from a linked list.
    5) Delete an entire linked list.
* Create a linked list.
    * ``` sllnode* create(VALUE val);```
    * Steps involved:
        1) Dynamically allocate space for a new sllnode.
        2) Check to make sure we didn't run out of memory.
        3) Initialize the node's *val* field.
        4) Return a pointer to the newly created sllnode.
    * ``` sllnode* new = create(6);```
* Search through a linked list to find an element.
    * ```bool find(sllnode* head, VALUE val);```
    * Steps involved:
        1) Create a traversal pointer pointing to the list's head.
        2) If the current node's val field is what we're looking for, report sucess.
        3) If not, set the traversal pointer to the next pointer in the list and go back to step 2.
        4) If you've reached the end of the list, report failure.
* Insert a new node into the linked list.
    *``` sllnode* insert(sllnode* head, VALUE val);```
    * Steps involved:
        * 1) Dynamically allocate space for a new sllnode.
        * 2) Check to make sure we didn't run out of memory.
        * 3) Populate and insert the node at the beggining of the linked list.
        * 4) Return pointer to the new head of the linked list.
    * Notice, the new created node will have to point to the (old first element of the list), and then set this newly created element to have the pointer of the start of the list.
* Delete an entire linked list.
    * ```void destroy(sslnode* head);```
    * Steps involved:
        * 1) If you've reached a null pointer, stop.
        * 2) Delete the rest of the list (recursion, delete everybody else, then come back and delete me).
        * 3) Free the current node.