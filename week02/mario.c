#import <stdio.h>
#import <cs50.h>

int main(void)
{
    int height = 0;
    do
    {
        height = get_int("Height: ");
        if (height >= 1 && height <= 8)
        {
            for (int i = 1; i <= height; i++)
            {
                int lateral_space = height - i;
                printf("%.*s", lateral_space, "        ");
                printf("%.*s", i, "########");
                printf("  ");
                printf("%.*s", i, "########");
                printf("\n");
            }

        }
    }
    while (height < 1 || height > 8);
}
