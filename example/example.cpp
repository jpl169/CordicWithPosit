#include "cordic.h"

int main(int argc, char** argv) {
    posit32 cosp, sinp;
    posit32 radian = 1.0;
    posit_cordic_quirez_start_late(radian, 50, cosp, sinp);
    printf("cos(1.0 rad) = %.10e", cosp.toDouble());
    printf("sin(1.0 rad) = %.10e", sinp.toDouble());
    
    posit32 xr = 1.0, yr = 2.0;
    radian = posit_vector_quirez_start_late(xr, yr, 50);
    printf("atan(2/1) = %.10e", radian.toDouble());
    
    return 0;
}
