// file: cpp_pi.cpp

#include "cpp_pi.h"
#include <math.h>
#include <stdlib.h>
#include <time.h>


PiMaker:: PiMaker()
        {count_inside = n = 0;}

PiMaker:: ~PiMaker(){}

void PiMaker:: compute()                //1
        {
        int count;
        double x, y, d, rand_max;
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
        }

void PiMaker:: set_n(int n_)              //2
        {
        n = n_;
        compute();
        }

double PiMaker:: get_n()                 //3
        {
        return n;
        }

//void PiMaker:: set(int n_)              //2
//        {
//        n = n_;
//        compute();
//        }

double PiMaker:: get_pi()                 //3
        {
        return pi;
        }
