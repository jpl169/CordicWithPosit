#include "cordic.h"
#include "scaled.h"

int main(int argc, char** argv) {
    FILE* cos_file;
    
    if (argc == 2) {
        cos_file = fopen(argv[1], "w+");
    } else {
        cos_file = fopen("cosnearpi.txt", "w+");
    }
    
    mpfr_t mrad, mResSin;
    mpfr_init2(mrad, 256);
    mpfr_init2(mResSin, 256);
    
    posit32 xr, yr;
    
    posit32 prad = 1.5707963267948965579989817342720925807952880859375;
    prad.value -= 121 * 16;

    for (int i = 0; i <= 120; i++) {
        prad.value += 16;
        
        //printf("%.50e, ", prad.toDouble());
        fprintf(cos_file, "%.50e, ", prad.toDouble());
        
        posit_cordic_default(prad, 50, xr, yr);
        fprintf(cos_file, "%.50e, ", xr.toDouble());
        posit_cordic_quirez(prad, 50, xr, yr);
        fprintf(cos_file, "%.50e, ", xr.toDouble());
        posit_cordic_ff(prad, 50, xr, yr);
        fprintf(cos_file, "%.50e, ", xr.toDouble());
        posit_cordic_quirez_ff(prad, 50, xr, yr);
        fprintf(cos_file, "%.50e, ", xr.toDouble());
        
        float fxr, fyr;
        float_cordic(prad.toDouble(), 50, fxr, fyr);
        fprintf(cos_file, "%.50e, ", fxr);

        mpfr_set_d(mrad, prad.toDouble(), MPFR_RNDN);
        mpfr_cos(mResSin, mrad, MPFR_RNDN);
        fprintf(cos_file, "%.50e\n", mpfr_get_d(mResSin, MPFR_RNDN));
        
    }
        
    mpfr_clear(mrad);
    mpfr_clear(mResSin);
    fclose(cos_file);
    
    return 0;
}
