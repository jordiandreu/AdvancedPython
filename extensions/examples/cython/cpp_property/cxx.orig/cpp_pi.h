#ifndef CPPPI_H
#define CPPPI_H
#include <iostream>

class PiMaker                        //1
    {
     private:                        //2
      double x, y, d, pi;
      int n, count_inside, count;
      void compute();
     public:                         //3
      PiMaker();
      ~PiMaker();
    
     void set(int n);                //4
     double get();
    };
#endif
