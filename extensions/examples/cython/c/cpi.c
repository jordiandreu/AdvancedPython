/* file: cpi.c */

#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

double piC(int n)
        {
        int count_inside, count;
        double x, y, d, pi, rand_max;
        count_inside = 0;
        srand(time(0));
        rand_max = (double) RAND_MAX;
        for (count=0; count < n; count++)
            {
            x = rand() / rand_max;
            y = rand() / rand_max;
            // sqrt not needed beause scaled to 1
            d = sqrt(x * x + y * y);
            if (d < 1)
                count_inside +=  1;
            }
        pi = 4.0 * count_inside / n;
        return pi;
        }

int main(void)
    {
    double pi;
    pi = piC(1000000);
    printf("pi: %10.6f\n", pi);
    return 0;
    }



