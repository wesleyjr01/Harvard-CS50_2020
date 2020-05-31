#include <stdbool.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <math.h>

#include "dictionary.h"


// size of hashtable
#define SIZE 1000000

// create nodes for linked list
typedef struct node
{
    char word[LENGTH+1];
    struct node* next;
}
node;

// create hashtable
node* hashtable[SIZE] = {NULL};

// create hash function
int hash (const char* word)
{
    int hash = 0;
    int n;
    for (int i = 0; word[i] != '\0'; i++)
    {
        // alphabet case
        if(isalpha(word[i]))
            n = word [i] - 'a' + 1;

        // comma case
        else
            n = 27;

        hash = ((hash << 3) + n) % SIZE;
    }
    return hash;
}

// create global variable to count size
int dictionarySize = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Set all hashtable indexes pointing to NULL at first
    for (int i = 0; i < SIZE; i++)
    {
        hashtable[i] = NULL;
    }

    // Open File
    FILE* f = fopen(dictionary, "r");
    if (f == NULL)
    {
        return false;
    }
    char word_dict[LENGTH + 1];

    while(fscanf(f, "%s", word_dict) != EOF)
    {
        // Create a new node
        node* new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }

        // Fill in the new_node
        strcpy(new_node->word, word_dict);
        new_node->next = NULL;

        // Hash the node
        unsigned long n_hash = hash(word_dict);

        // Insert Node into Hash Table
        new_node->next = hashtable[n_hash];
        hashtable[n_hash] = new_node;

        // Update size of the dict
        dictionarySize++;
    }
    fclose(f);
    return true;
}

// Returns true if word is in dictionary else false
bool check(const char *text_word)
{
    // lowercase the word first
    char copy_text_word[LENGTH + 1];
    int len = strlen(text_word);
    for(int i = 0; i < len; i++)
        copy_text_word[i] = tolower(text_word[i]);
    copy_text_word[len] = '\0';

    // hash the incoming word
    unsigned long hash_val = hash(copy_text_word);

    // check if exists in the linked list of index hash_val
    node* pointing_to = hashtable[hash_val];
    while(pointing_to != NULL)
    {
        if(strcasecmp(pointing_to->word, copy_text_word) == 0)
        {
            return true;
        }

        pointing_to = pointing_to->next;
    }
    // TODO
    return false;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded.
unsigned int size(void)
{
    // TODO
    // if dictionary is loaded, return number of words
    if (dictionarySize > 0)
    {
        return dictionarySize;
    }

    // if dictionary hasn't been loaded, return 0
    else
        return 0;
}

// Unloads dictionary from memory.  Returns true if successful else false.
bool unload(void)
{
    // TODO
    // create a variable to go through index
    int index = 0;

    // iterate through entire hashtable array
    while (index < SIZE)
    {
        // if hashtable is empty at index, go to next index
        if (hashtable[index] == NULL)
        {
            index++;
        }

        // if hashtable is not empty, iterate through nodes and start freeing
        else
        {
            while(hashtable[index] != NULL)
            {
                node* cursor = hashtable[index];
                hashtable[index] = cursor->next;
                free(cursor);
            }

            // once hashtable is empty at index, go to next index
            index++;
        }
    }

    // return true if successful
    return true;
}

void makelower(const char* str, char* copy)
{
    // Iterate loop till last character of string
    strcpy(copy,str);

    for(int i=0; copy[i]!='\0'; i++)
    {
        if(copy[i]>='A' && copy[i]<='Z')
        {
            copy[i] = copy[i] + 32;
        }
    }
    return;
}