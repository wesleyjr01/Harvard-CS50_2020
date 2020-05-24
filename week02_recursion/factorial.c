#import <cs50.h>
#import <stdio.h>

int factorial(int n);

int main(void)
{
    int n = get_int("Inser an intereger: ");
    printf("%i\n", factorial(n));
}

int factorial(int n)
{
    if (n == 1)
    {
        return 1;
    }
    else if (n < 1)
    {
        printf("Insert a positive integer");
        return 0;
    }
    else
    {
        return n*factorial(n-1);
    }
}