#ifndef CPPPI_H
#define CPPPI_H
#include <iostream>

// Exercice 15.2.1.1: make n public
class PiMaker                        //1
    {
     private:                        //2
      double x, y, d, pi;
      int count_inside, count;
      void compute();
     public:                         //3
      PiMaker();
      ~PiMaker();
     int n;
    
     void set_n(int n);                //4
     double get_n();

     double get_pi();

};
#endif
