#include "softposit_cpp.h"
#include <mpfr.h>

typedef struct _analy {
    unsigned int analysisCount;
    unsigned int currCount;
    
    // analysis variables for zero ulp error cases
    unsigned int totalZeroUlp;
    unsigned int currZeroUlp;
    
    // analysis variables for maximum ulp error
    unsigned int totalMaxUlp;
    unsigned int currMaxUlp;
    
    // analysis variables for minimum ulp error
    unsigned int totalMinUlp;
    unsigned int currMinUlp;

    // analysis variables to see average ulp error
    unsigned long long int totalUlpCombined;
    unsigned long long int currUlpCombined;
    
    // analysis variables for maximum absolute error
    double totalMaxAbs;
    double currMaxAbs;

    // analysis variables for minimum absolute error
    double totalMinAbs;
    double currMinAbs;

	// analysis variables for average absolute error
    double totalAvgAbsCombined;
    double currAvgAbsCombined;
    unsigned long long int totalAvgAbsCount;
    unsigned long long int currAvgAbsCount;
} Analy;
