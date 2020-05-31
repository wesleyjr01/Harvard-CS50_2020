#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH 45
#define BUCKETS 5

unsigned long hash(unsigned char *str);

int main(void)
{
    FILE *fp = fopen("text.txt", "r");
    char buffer[LENGTH + 1];

    int acum = 0;
    while (fscanf(fp, "%s", buffer) != EOF)
    {
        // int hash_val = hashfunc(buffer);
        unsigned long hash_val = hash(buffer) % BUCKETS;
        printf("iteration: %i\n", acum);
        printf("buffer content: %s\n", buffer);
        printf("hash: %li\n\n", hash_val);
        acum++;
    }

}

// int hashfunc(char word[])
// {
//     int sum = 0;
//     for(int j = 0; word[j] != '\0'; j++)
//     {
//         sum += word[j];
//     }
//     return sum % BUCKETS;
// }

unsigned long hash(unsigned char *str)
{
    unsigned long hash = 5381;
    int c;

    while (c = *str++)
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    return hash;
}