#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("Insert one command-line-argument!\n");
        return 1;
    }

    // number of bytes to read at a time
    int number = 512;

    // Read number bytes from file
    unsigned char bytes[number];

    // loop counter variable
    int loop_counter = 0;

    // flag to detect first jpeg
    int first_jpg = 0;

    // create filename string
    char filename[8];

    // Open memory card file
    FILE *f = fopen(argv[1], "r");

    sprintf(filename, "%03i.jpg", 0); // Result: 000.jpg into filename

    // After creating filename, we can open a new file by calling fopen
    FILE *img = fopen(filename, "w");


    int bytes_read = number;
    do
    {
        bytes_read = fread(bytes, sizeof(char), number, f);

        // The beggining of the blocks represents the beggining of a JPEG file?
        if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] & 0xf0) == 0xe0)
        {
            // Once found the beggining, create a new file to write this data to
            // Filenames: ###.jpg, starting at 000.jpg
            sprintf(filename, "%03i.jpg", loop_counter); // Result: <loop_counter>.jpg into filename

            if (first_jpg == 0)
            {
                // Write data to the file
                fwrite(bytes, sizeof(char), bytes_read, img);
            }
            else
            {
                // close last JPEG file.
                fclose(img);

                // open new JPEG file to continue writing to.
                img = fopen(filename, "w");

                // Write data to the file
                fwrite(bytes, sizeof(char), bytes_read, img);
            }

            // found a new jpg, increment loop_counter and first_jpg flag
            loop_counter++;
            first_jpg++;
        }
        else
        {
            if (first_jpg != 0)
            {
                // keep writing this block to it.
                fwrite(bytes, sizeof(char), bytes_read, img);
            }
        }
    }
    while (bytes_read == number);
}
