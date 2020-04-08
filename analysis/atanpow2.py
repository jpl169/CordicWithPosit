import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import sys

inputFile = ""
otuputPdf = ""

if len(sys.argv) != 3 :
    print("Expecting 2 arguments")
    print("python3 atanpow2 <input file name> <output pdf name>")
    exit()
else :
    inputFile = sys.argv[1]
    outputPdf = sys.argv[2]

beginIndex = 24
endIndex = 36

theta = []
sin_default = []
sin_quirez = []
sin_ff = []
sin_quirez_ff = []
sin_float = []
sin_mpfr = []

sin_default_abs = []
sin_quirez_abs = []
sin_ff_abs = []
sin_quirez_ff_abs = []
sin_float_abs = []

sinFile = open(inputFile, "r")
for line in sinFile:
    splitted = line.split(", ")
    theta.append(float(splitted[0]))
    sin_default.append(float(splitted[1]))
    sin_quirez.append(float(splitted[2]))
    sin_ff.append(float(splitted[3]))
    sin_quirez_ff.append(float(splitted[4]))
    sin_float.append(float(splitted[5]))
    sin_mpfr.append(float(splitted[6]))

    sin_default_abs.append(abs(float(splitted[1]) - float(splitted[6])))
    sin_quirez_abs.append(abs(float(splitted[2]) - float(splitted[6])))
    sin_ff_abs.append(abs(float(splitted[3]) - float(splitted[6])))
    sin_quirez_ff_abs.append(abs(float(splitted[4]) - float(splitted[6])))
    sin_float_abs.append(abs(float(splitted[5]) - float(splitted[6])))

plt.rcParams.update({'font.size': 9})

plt.scatter(theta[beginIndex:endIndex], sin_mpfr[beginIndex:endIndex], color='xkcd:grey', marker = "o", label="Real", s = 70)
plt.scatter(theta[beginIndex:endIndex], sin_quirez_ff[beginIndex:endIndex], color='k', marker = "*", label="Our CORDIC (posit)")
plt.scatter(theta[beginIndex:endIndex], sin_float[beginIndex:endIndex], color='b', marker = "x", label="Naive CORDIC (float)")
plt.ylim(-4 * pow(10, -9), 6.2 * pow(10, -8))
plt.axhline(0, color="k", linestyle = '-', linewidth = 0.1)

f = mtick.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
h = lambda x,pos : "$2^{{-{}}}$".format('%.f' % x)
plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(g))
plt.gca().xaxis.set_major_formatter(mtick.FuncFormatter(h))
plt.legend()
plt.xlabel(r"$y$")
plt.ylabel(r"$atan(y)$")
plt.gcf().set_size_inches(4.2, 2)
plt.savefig(outputPdf, bbox_inches='tight', pad_inches = 0.01)
