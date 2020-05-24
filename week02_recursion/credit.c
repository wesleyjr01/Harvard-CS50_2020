
#import <stdio.h>
#import <cs50.h>

long int first_two_digits(long int first_two);

int digits_counter(long int cc_number);

int second_to_last_sum(long int cc_number);

int rest_sum(long int cc_number);

int main(void)
{
    long int cc_number = get_long("Number: ");

    int n_of_digits = 0;
    n_of_digits = digits_counter(cc_number);

    int first_two = 0;
    first_two =  first_two_digits(cc_number);

    int first_first = (first_two / 10);

    int checksum = 0;
    checksum = second_to_last_sum(cc_number) + rest_sum(cc_number);

    if ((n_of_digits >= 13) && (n_of_digits <= 16))
    {
        if (((first_two == 34) || (first_two == 37)) && (checksum % 10 == 0))
        {
            printf("AMEX\n");
        }
        else if ((first_two >= 51) && (first_two <= 55) && (checksum % 10 == 0))
        {
            printf("MASTERCARD\n");
        }
        else if ((first_first == 4) && (checksum % 10 == 0))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }

}


long int first_two_digits(long int first_two)
{
    while (first_two >= 100)
    {
        first_two = first_two / 10;
    }
    return first_two;
}

int digits_counter(long int cc_number)
{
    int counter = 1;
    while ((cc_number / 10) > 0)
    {
        cc_number = cc_number / 10;
        counter++;
    }
    return counter;
}

int second_to_last_sum(long int cc_number)
{
    int acumulator = 0;

    while (cc_number != 0)
    {
        int last_two = cc_number % 100;
        int firt_of_last_two = last_two / 10;
        int mult_first_of_last_two = firt_of_last_two * 2;
        int sum_of_digits = (mult_first_of_last_two / 10) + (mult_first_of_last_two % 10);
        acumulator = acumulator + sum_of_digits;
        cc_number = cc_number / 100;
    }
    return acumulator;
}

int rest_sum(long int cc_number)
{
    int acumulador = 0;

    while (cc_number != 0)
    {
        int last_two = cc_number % 100;
        int last_of_last_two = last_two % 10;
        acumulador = acumulador + last_of_last_two;
        cc_number = cc_number / 100;
    }
    return acumulador;
}
