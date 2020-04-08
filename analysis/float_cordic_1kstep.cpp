#include "scaled.h"
#include "cordic.h"

void InitializeExperimentAnaly(Analy& a) {
    a.analysisCount = 0;
    a.currCount = 0;
    
    // analysis variables for zero ulp error cases
    a.totalZeroUlp = 0;
    a.currZeroUlp = 0;
    
    // analysis variables for maximum ulp error
    a.totalMaxUlp = 0;
    a.currMaxUlp = 0;
    
    // analysis variables for minimum ulp error
    a.totalMinUlp = 0xFFFFFFFF;
    a.currMinUlp = 0xFFFFFFFF;

    // analysis variables to see average ulp error
    a.totalUlpCombined = 0;
    a.currUlpCombined = 0;
    
    // analysis variables for maximum absolute error
    a.totalMaxAbs = 0;
    a.currMaxAbs = 0;
    
    // analysis variables for minimum absolute error
    a.totalMinAbs = 0xFFFFFFFF;
    a.currMinAbs = 0xFFFFFFFF;

	// analysis variables for average absolute error
    a.totalAvgAbsCombined = 0;
    a.currAvgAbsCombined = 0;
    a.totalAvgAbsCount = 0;
    a.currAvgAbsCount = 0;
}

unsigned long ulpf(float x, float y){
  if (x == 0) x = 0; // -0 == 0
  if (y == 0) y = 0; // -0 == 0

  /* if (x != x && y != y) return 0; */
  if (x != x) return UINT_MAX - 1; // Maximum error
  if (y != y) return UINT_MAX - 1; // Maximum error
  int xx = *((int*) &x);
  xx = xx < 0 ? INT_MIN - xx : xx;
  int yy = *((int*) &y);
  yy = yy < 0 ? INT_MIN - yy : yy;
  return xx >= yy ? xx - yy : yy - xx;
}

//correct
void UpdateCurrExperimentAnaly(Analy& a, float pRes, float pResFromMpfr, double
		mpfr_resDouble) {
    
    double posit_res = pRes;
    
	//ulp error difference
    unsigned int currUlpDiff = ulpf(pRes, pResFromMpfr);
   
	//absolute error difference
	double currAbsDiff = mpfr_resDouble - posit_res;
	if (currAbsDiff < 0) currAbsDiff *= -1;

    a.currCount++;

    // analysis variables to see average ulp error
    a.currUlpCombined += currUlpDiff;
    
    // analysis variables for zero ulp error cases
    if (currUlpDiff == 0) a.currZeroUlp++;
    
    // analysis variables for maximum ulp error
    if (currUlpDiff > a.currMaxUlp) a.currMaxUlp = currUlpDiff;

    // analysis variables for minimum ulp error
    if (currUlpDiff < a.currMinUlp) a.currMinUlp = currUlpDiff;

	// analysis variables for minimum absolute error
    if (currAbsDiff < a.currMinAbs) a.currMinAbs = currAbsDiff;

	// analysis variables for average absolute error
    if (!isnan(currAbsDiff) && !isinf(currAbsDiff)) {
        a.currAvgAbsCombined += currAbsDiff;
        a.currAvgAbsCount++;
    }
	
	// analysis variables for maximum absolute error
    if (a.currMaxAbs < currAbsDiff) a.currMaxAbs = currAbsDiff;
    return;
}

//correct
void UpdateTotalAndClearCurrExperimentAnaly(Analy& a) {
    a.analysisCount += a.currCount;
    
    // analysis variables to see average ulp error
    a.totalUlpCombined += a.currUlpCombined;
    
    // analysis variables for zero ulp error cases
    a.totalZeroUlp += a.currZeroUlp;
    
    // analysis variables for maximum ulp error
    if (a.currMaxUlp > a.totalMaxUlp) a.totalMaxUlp = a.currMaxUlp;
    
    // analysis variables for minimum ulp error
    if (a.currMinUlp < a.totalMinUlp) a.totalMinUlp = a.currMinUlp;
   
	// analysis variables for minimum absolute error
    if (a.currMinAbs < a.totalMinAbs) a.totalMinAbs = a.currMinAbs;

	// analysis variables for average absolute error
    a.totalAvgAbsCombined += a.currAvgAbsCombined;
    a.totalAvgAbsCount += a.currAvgAbsCount;
	
	// analysis variables for maximum absolute error
    if (a.currMaxAbs > a.totalMaxAbs) a.totalMaxAbs = a.currMaxAbs;

    a.currCount = 0;
    // analysis variables to see average ulp error
    a.currUlpCombined = 0;
    
    // analysis variables for zero ulp error cases
    a.currZeroUlp = 0;
    
    // analysis variables for maximum ulp error
    a.currMaxUlp = 0;
    
    // analysis variables for minimum ulp error
    a.currMinUlp = 0xFFFFFFFF;

    // analysis variables for minimum absolute error
    a.currMinAbs = pow(2, 1000);

	// analysis variables for average absolute error
    a.currAvgAbsCombined = 0;
    a.currAvgAbsCount = 0;
	
	// analysis variables for maximum absolute error
    a.currMaxAbs = 0;
    
    return;
}

void PrintExperimentAnalyInfo(FILE* ofile) {
    fprintf(ofile, "Count, 0Ulp, MaxUlp, MinUlp, AvgUlp, MaxAbs, MinAbs, AvgAbs\n");
}

//add fprintf files for cosine and sin
void PrintCurrExperimentAnaly(Analy& a, posit32 stepLB, posit32 stepUB, FILE* ofile) {
    fprintf(ofile, "Analysis Step Info (%.10e ~ %.10e):\n",
           stepLB.toDouble(), stepUB.toDouble());
    fprintf(ofile, "%u, ", a.currCount);
    fprintf(ofile, "%u, ", a.currZeroUlp);
    fprintf(ofile, "%u, ", a.currMaxUlp);
    fprintf(ofile, "%u, ", a.currMinUlp);
    fprintf(ofile, "%.10e, ", a.currUlpCombined * 1.0 / a.currCount);
    fprintf(ofile, "%.10e, ", a.currMaxAbs);
    fprintf(ofile, "%.10e, ", a.currMinAbs);
    fprintf(ofile, "%.10e, ", a.currAvgAbsCombined * 1.0 / a.currAvgAbsCount);
    fprintf(ofile, "\n\n");
    fflush(ofile);
}

void PrintTotalExperimentAnaly(Analy& a, FILE* ofile) {
    fprintf(ofile, "Total Analysis Info:\n");
    PrintExperimentAnalyInfo(ofile);
    fprintf(ofile, "%u, ", a.analysisCount);
    fprintf(ofile, "%u, ", a.totalZeroUlp);
    fprintf(ofile, "%u, ", a.totalMaxUlp);
    fprintf(ofile, "%u, ", a.totalMinUlp);
    fprintf(ofile, "%.10e, ", a.totalUlpCombined * 1.0 / a.analysisCount);
    fprintf(ofile, "%.10e, ", a.totalMaxAbs);
    fprintf(ofile, "%.10e, ", a.totalMinAbs);
    fprintf(ofile, "%.10e, ", a.totalAvgAbsCombined * 1.0 / a.totalAvgAbsCount);
    fprintf(ofile, "\n\n");
    fflush(ofile);
}

typedef union __float_x{
    float f;
    unsigned int x;
} float_x;

int main(int argc, char** argv) {
    FILE* posit_sin_file;
    FILE* posit_cos_file;
    
    if (argc == 3) {
        posit_sin_file = fopen(argv[1], "w+");
        posit_cos_file = fopen(argv[2], "w+");
    } else {
        posit_sin_file = fopen("posit_default_sin.txt", "w+");
        posit_cos_file = fopen("posit_default_cos.txt", "w+");
    }

    unsigned int analysisStep = 32768;
    mpfr_t mrad, mResSin, mResCos;
    mpfr_init2(mrad, 256);
    mpfr_init2(mResSin, 256);
    mpfr_init2(mResCos, 256);

    float stepLB;
    float_x rad;

    Analy a;
    Analy b;
    InitializeExperimentAnaly(a);
    InitializeExperimentAnaly(b);
    PrintExperimentAnalyInfo(posit_sin_file);
    PrintExperimentAnalyInfo(posit_cos_file);

    for (rad.f = 0.0;
         rad.f <= 1.5707963267948965579989817342720925807952880859375;
         rad.x = rad.x + 100) {
        
        if (a.currCount == 0) stepLB = rad.f;
        
        float dx, dy;
        float_cordic(rad.f, 50, dx, dy);
        
        mpfr_set_d(mrad, rad.f, MPFR_RNDN);
        mpfr_sin(mResSin, mrad, MPFR_RNDN);
        mpfr_cos(mResCos, mrad, MPFR_RNDN);
        double mpfr_resDoubleSin = mpfr_get_d(mResSin, MPFR_RNDN);
        double mpfr_resDoubleCos = mpfr_get_d(mResCos, MPFR_RNDN);
        float pResFromMpfrSin = mpfr_resDoubleSin;
        float pResFromMpfrCos = mpfr_resDoubleCos;
        UpdateCurrExperimentAnaly(a, dy, pResFromMpfrSin, mpfr_resDoubleSin);
        UpdateCurrExperimentAnaly(b, dx, pResFromMpfrCos, mpfr_resDoubleCos);

        if (a.currCount == analysisStep) {
            PrintCurrExperimentAnaly(a, stepLB, rad.f, posit_sin_file);
            UpdateTotalAndClearCurrExperimentAnaly(a);
            PrintCurrExperimentAnaly(b, stepLB, rad.f, posit_cos_file);
            UpdateTotalAndClearCurrExperimentAnaly(b);
        }
    }
    
    // Final leftover partial analysis:
    if (a.currCount > 0) {
        PrintCurrExperimentAnaly(a, stepLB, rad.f, posit_sin_file);
        UpdateTotalAndClearCurrExperimentAnaly(a);
        PrintCurrExperimentAnaly(b, stepLB, rad.f, posit_cos_file);
        UpdateTotalAndClearCurrExperimentAnaly(b);
    }
    
    PrintTotalExperimentAnaly(a, posit_sin_file);
    PrintTotalExperimentAnaly(b, posit_cos_file);

    mpfr_clear(mrad);
    mpfr_clear(mResSin);
    mpfr_clear(mResCos);

    fclose(posit_sin_file);
    fclose(posit_cos_file);
    
    return 0;
}