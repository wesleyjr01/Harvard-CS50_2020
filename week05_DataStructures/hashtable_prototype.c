#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH 45
#define BUCKETS 5

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

int main(void)
{
    // Initializes a hashtable
    node* table[BUCKETS];

    // Set all hash indexes to NULL at first
    for (int i = 0; i < BUCKETS; i++)
    {
        table[i] = NULL;
    }

    // Allocate memory for a new node
    node* n = malloc(sizeof(node));

    // Fill the content of that node
    // strcpy((*n).word, "ALAL");
    strcpy(n->word, "ALAL");
    // (*n).next = NULL;
    n->next = NULL;

    for (int i = 0; i < BUCKETS; i++)
    {
        printf("table[%i]: %p\n", i, table[i]);
    }
    printf("new node n mem address: %p\n", n);
    printf("new node n word: %s\n", (*n).word);
    printf("new node n points to: %p\n", (*n).next);

    free(n);
}