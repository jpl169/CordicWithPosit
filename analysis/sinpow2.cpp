#include "cordic.h"
#include "scaled.h"

int main(int argc, char** argv) {
    FILE* sin_file;
    
    if (argc == 2) {
        sin_file = fopen(argv[1], "w+");
    } else {
        sin_file = fopen("sinpow2.txt", "w+");
    }
    
    mpfr_t mrad, mResSin;
    mpfr_init2(mrad, 256);
    mpfr_init2(mResSin, 256);
    
    posit32 xr, yr;

    for (int i = 0; i <= 120; i++) {
        posit32 prad = pow(2, -i);
        
        //printf("%.50e, ", prad.toDouble());
        fprintf(sin_file, "%d, ", i);
        
        posit_cordic_default(prad, 50, xr, yr);
        fprintf(sin_file, "%.50e, ", yr.toDouble());
        posit_cordic_quirez(prad, 50, xr, yr);
        fprintf(sin_file, "%.50e, ", yr.toDouble());
        posit_cordic_ff(prad, 50, xr, yr);
        fprintf(sin_file, "%.50e, ", yr.toDouble());
        posit_cordic_quirez_ff(prad, 50, xr, yr);
        fprintf(sin_file, "%.50e, ", yr.toDouble());
        
        float fxr, fyr;
        float_cordic(prad.toDouble(), 50, fxr, fyr);
        fprintf(sin_file, "%.50e, ", fyr);

        mpfr_set_d(mrad, prad.toDouble(), MPFR_RNDN);
        mpfr_sin(mResSin, mrad, MPFR_RNDN);
        fprintf(sin_file, "%.50e\n", mpfr_get_d(mResSin, MPFR_RNDN));
        
    }
        
    mpfr_clear(mrad);
    mpfr_clear(mResSin);
    fclose(sin_file);
    
    return 0;
}
