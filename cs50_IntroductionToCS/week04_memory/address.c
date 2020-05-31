#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    // &n means the address of n.
    // * means go to the address.
    printf("variable n addres(pointer): %p\n", p);
    printf("variable n addres(pointer), then go to the address: %i\n", *p);
    printf("\n");

    char *s = "EMMA";
    printf("%s\n", s);
    printf("%p\n", s);
    printf("Adress of the first char %p\n", &s[0]);
}