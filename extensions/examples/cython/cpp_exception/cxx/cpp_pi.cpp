// file: cpp_pi.cpp

#include "cpp_pi.h"
#include <math.h>
#include <stdlib.h>
#include <stdexcept>
#include <time.h>
using namespace std;


PiMaker:: PiMaker()
        {count_inside = n = 0;}

PiMaker:: ~PiMaker(){}

void PiMaker:: compute()
        {
        int count_inside, count;
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

void PiMaker:: set(int n_)
        {
        if (n_ < 1000) {
        throw invalid_argument("n must be larger than 1000"); //1
        }
        n = n_;
        compute();
        }

double PiMaker:: get()
        {
        return pi;
        }
