#include "cordic.h"
#include "scaled.h"

int main(int argc, char** argv) {
    FILE* atan_file;
    
    if (argc == 2) {
        atan_file = fopen(argv[1], "w+");
    } else {
        atan_file = fopen("atanpow2.txt", "w+");
    }
    
    mpfr_t mrad, mxr, myr;
    mpfr_init2(mrad, 256);
    mpfr_init2(mxr, 256);
    mpfr_init2(myr, 256);
    
    posit32 xr, yr;
    xr = 1.0;
    posit32 prad;
    
    for (int i = 0; i <= 120; i++) {
        yr = pow(2, -i);
        
        fprintf(atan_file, "%d, ", i);
        
        prad = posit_vector_default(xr, yr, 50);
        fprintf(atan_file, "%.50e, ", prad.toDouble());
        
        prad = posit_vector_quirez(xr, yr, 50);
        fprintf(atan_file, "%.50e, ", prad.toDouble());

        prad = posit_vector_ff(xr, yr, 50);
        fprintf(atan_file, "%.50e, ", prad.toDouble());

        prad = posit_vector_quirez_ff(xr, yr, 50);
        fprintf(atan_file, "%.50e, ", prad.toDouble());
        
        float fxr, fyr, frad;
        
        fxr = 1.0;
        fyr = yr.toDouble();
        frad = float_vector (fxr, fyr, 50);
        fprintf(atan_file, "%.50e, ", frad);

        mpfr_set_d(mxr, 1.0, MPFR_RNDN);
        mpfr_set_d(myr, fyr, MPFR_RNDN);
        
        mpfr_atan2(mrad, myr, mxr, MPFR_RNDN);
        fprintf(atan_file, "%.50e\n", mpfr_get_d(mrad, MPFR_RNDN));
        
    }
        
    mpfr_clear(mrad);
    mpfr_clear(mxr);
    mpfr_clear(myr);
    fclose(atan_file);
    
    return 0;
}
