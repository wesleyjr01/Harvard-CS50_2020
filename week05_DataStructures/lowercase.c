#include <stdio.h>
#include <string.h>
#define MAX_SIZE 100 // Maximum string size

void makelower(const char* str, char* copy);

int main()
{
    char str[MAX_SIZE] = "BANANA";
    char copy[strlen(str)];
    int i;
 
    /* Input string from user */
    printf("Enter any string: ");
    // str = "BANANA";

    makelower(str, copy);

    printf("Lower case string: %s", copy);

    return 0;
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