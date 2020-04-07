import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import sys

inputFile = ""
otuputPdf = ""

if len(sys.argv) != 3 :
    print("Expecting 2 arguments")
    print("python3 cosnearpi.py <input file name> <output pdf name>")
    exit()
else :
    inputFile = sys.argv[1]
    outputPdf = sys.argv[2]

beginIndex = 88
endIndex = 98

theta = []
sin_default = []
sin_quirez = []
sin_start_late = []
sin_quirez_start_late = []
sin_float = []
sin_mpfr = []

sin_default_abs = []
sin_quirez_abs = []
sin_start_late_abs = []
sin_quirez_start_late_abs = []
sin_float_abs = []


sinFile = open(inputFile, "r")
for line in sinFile:
    splitted = line.split(", ")
    theta.append(float(splitted[0]))
    sin_default.append(float(splitted[1]))
    sin_quirez.append(float(splitted[2]))
    sin_start_late.append(float(splitted[3]))
    sin_quirez_start_late.append(float(splitted[4]))
    sin_float.append(float(splitted[5]))
    sin_mpfr.append(float(splitted[6]))

    sin_default_abs.append(abs(float(splitted[1]) - float(splitted[6])))
    sin_quirez_abs.append(abs(float(splitted[2]) - float(splitted[6])))
    sin_start_late_abs.append(abs(float(splitted[3]) - float(splitted[6])))
    sin_quirez_start_late_abs.append(abs(float(splitted[4]) - float(splitted[6])))
    sin_float_abs.append(abs(float(splitted[5]) - float(splitted[6])))

plt.rcParams.update({'font.size': 9})

plt.scatter(theta[beginIndex:endIndex], sin_mpfr[beginIndex:endIndex], color='xkcd:grey', marker = "o", label="Real", s = 70)
plt.scatter(theta[beginIndex:endIndex], sin_quirez_start_late[beginIndex:endIndex], color='k', marker = "*", label="Our CORDIC (posit)")
plt.scatter(theta[beginIndex:endIndex], sin_float[beginIndex:endIndex], color='b', marker = "x", label="Naive CORDIC (float)")
plt.ylim(2.55 * pow(10, -6), 4 * pow(10, -6))
plt.xlim(1.57079245, 1.57079365)
plt.xticks([1.5707925, 1.5707930, 1.5707935])

f = mtick.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
#h = lambda x,pos : "$2^{{-{}}}$".format('%.f' % x)
h = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(g))
plt.gca().xaxis.set_major_formatter(mtick.FuncFormatter(h))

plt.legend()
plt.xlabel(r"$\theta$")
plt.ylabel(r"$cos(\theta)$")
plt.gcf().set_size_inches(4.2, 2)
plt.savefig(outputPdf, bbox_inches='tight', pad_inches = 0.01)
