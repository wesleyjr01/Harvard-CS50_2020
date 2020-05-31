#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum = image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed;
            int avg = round(sum / 3.0);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (sepiaRed > 255)
                sepiaRed = 255;
            if (sepiaGreen > 255)
                sepiaGreen = 255;
            if (sepiaBlue > 255)
                sepiaBlue = 255;

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int half_point = floor(width / 2);
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < half_point; j++)
        {
            RGBTRIPLE temp;

            temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    int height_lb = 0;
    int height_ub = height - 1;
    int width_lb = 0;
    int width_ub = width - 1;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int pix_height_lb = i - 1;
            if (pix_height_lb < height_lb)
            {
                pix_height_lb = height_lb;
            }


            int pix_height_ub = i + 1;
            if (pix_height_ub > height_ub)
            {
                pix_height_ub = height_ub;
            }


            int pix_width_lb = j - 1;
            if (pix_width_lb < width_lb)
            {
                pix_width_lb = width_lb;
            }


            int pix_width_ub = j + 1;
            if (pix_width_ub > width_ub)
            {
                pix_width_ub = width_ub;
            }


            int red_acum = 0;
            int blue_acum = 0;
            int green_acum = 0;
            float counter = 0.0;

            for (int k = pix_height_lb; k <= pix_height_ub; k++)
            {
                for (int p = pix_width_lb; p <= pix_width_ub; p++)
                {
                    red_acum += image[k][p].rgbtRed;
                    blue_acum += image[k][p].rgbtBlue;
                    green_acum += image[k][p].rgbtGreen;

                    counter++;
                }
            }
            temp[i][j].rgbtRed = round( red_acum / counter);
            temp[i][j].rgbtBlue = round( blue_acum / counter);
            temp[i][j].rgbtGreen = round( green_acum / counter);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}
