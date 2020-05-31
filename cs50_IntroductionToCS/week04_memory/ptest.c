#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char* s = malloc(5);
    printf("%p\n", s);
    printf("%p\n", s+512);

}