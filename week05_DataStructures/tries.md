# Shorts - Tries
* We have seen a few data structures that handle the mapping of key-value pairs.
    * Arrays: The key is the element index, the value is the data at that location.
    * Hash tables: They key is the hash code of the data, the value is a linked list of data hashing to that hash code.
* What about a slightly different kind of a data structure where the key is guaranteed to be unique, and the value could be as simple as a Boolean that tells you whether the data exists in the structure?
* Tries combine structures and pointers together to store data in an interesting way.
* The data to be searched for in the trie is now a roadmap.
    * If you can follow the map from beggining to end, the data exists in the trie.
    * If you can't, it doesn't.
Unlike with a hash table, there are no collisions, and no two pieces of data(unless they are identical) have the same path.
* For this example, let's map key-value pairs where the keys are four-digit years (YYYY) and the values are names of universities founded during those years.
* In a trie, the paths from a central **root** node to a **leaf** node (where the school names would be), would be labeled with digits of the year.
* Each node of the path com root to leaf could have 10 pointers emanating from it, one fro each digit.
```
typedef struct _trie
{
    char university[20];
    struct _trie* paths[20];
}
trie;
```
* To search for an element in the trie, use successive digits to nagivate from the root, and if you can make it to the end without hitting a dead end(a NULL pointer), you've found it.