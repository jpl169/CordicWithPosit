import sys
import os
import shutil
import subprocess
import filecmp

def GetData(filename) :
    with open(filename, "r") as f:
        totalData = f.readlines()[-2]
        data = totalData.split(',')
        return data[0:8]

def FormatData(data) :
    data[0] = int(data[0])
    data[1] = int(data[1])
    data[2] = int(data[2])
    data[3] = int(data[3])
    data[4] = float(data[4])
    data[5] = float(data[5])
    data[6] = float(data[6])
    data[7] = float(data[7])
    return data

binDir = "bin"
analysisDataDir = "analysisData"
simpAccDataDir = os.path.join(analysisDataDir, "forSimpleAccuracy")
tableDataDir = "table"
tableDataFile = os.path.join(tableDataDir, "simpleTable2table3.txt");
expectedFile = "expected/simpleTable2table3.txt"

cordics = [
    "float_cordic_1kstep",
    "posit_cordic_default_1kstep",
    "posit_cordic_quirez_1kstep",
    "posit_cordic_ff_1kstep",
    "posit_cordic_quirez_ff_1kstep"]

vectors = [
    "float_vector_1kstep",
    "posit_vector_default_1kstep",
    "posit_vector_quirez_1kstep",
    "posit_vector_ff_1kstep",
    "posit_vector_quirez_ff_1kstep"]

if not os.path.exists(tableDataDir) :
    os.makedirs(tableDataDir)

f = open(tableDataFile, "w+");

ocs = FormatData(GetData(os.path.join(simpAccDataDir, cordics[4] + "_sin.txt")))
occ = FormatData(GetData(os.path.join(simpAccDataDir, cordics[4] + "_cos.txt")))
oca = FormatData(GetData(os.path.join(simpAccDataDir, vectors[4] + "_atan.txt")))
ncs = FormatData(GetData(os.path.join(simpAccDataDir, cordics[0] + "_sin.txt")))
ncc = FormatData(GetData(os.path.join(simpAccDataDir, cordics[0] + "_cos.txt")))
nca = FormatData(GetData(os.path.join(simpAccDataDir, vectors[0] + "_atan.txt")))

f.write("Table 2\n")
f.write("-" * (15 * 7) + "\n")
f.write("{:<15}{:<45}{:<45}\n".format("", "(a) our CORDIC(posit)", "(b) naive CORDIC (float)"))
f.write("-" * (15 * 7) + "\n")
f.write("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format("", "sin", "cos", "atan", "sin", "cos", "atan"))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("max abs", ocs[5], occ[5], oca[5], ncs[5], ncc[5], nca[5]))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("min abs", ocs[6], occ[6], oca[6], ncs[6], ncc[6], nca[6]))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("avg abs", ocs[7], occ[7], oca[7], ncs[7], ncc[7], nca[7]))
f.write("{:<15}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n".format("max ulp", ocs[2], occ[2], oca[2], ncs[2], ncc[2], nca[2]))
f.write("{:<15}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n".format("min ulp", ocs[3], occ[3], oca[3], ncs[3], ncc[3], nca[3]))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("avg ulp", ocs[4], occ[4], oca[4], ncs[4], ncc[4], nca[4]))
f.write("{:<15}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n".format("# 0 ulp", ocs[1], occ[1], oca[1], ncs[1], ncc[1], nca[1]))
f.write("{:<15}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n".format("# input", ocs[0], occ[0], oca[0], ncs[0], ncc[0], nca[0]))

f.write("\n")
f.write("\n")

ocs = FormatData(GetData(os.path.join(simpAccDataDir, cordics[4] + "_sin.txt")))
occ = FormatData(GetData(os.path.join(simpAccDataDir, cordics[4] + "_cos.txt")))
oca = FormatData(GetData(os.path.join(simpAccDataDir, vectors[4] + "_atan.txt")))

ncs = FormatData(GetData(os.path.join(simpAccDataDir, cordics[1] + "_sin.txt")))
ncc = FormatData(GetData(os.path.join(simpAccDataDir, cordics[1] + "_cos.txt")))
nca = FormatData(GetData(os.path.join(simpAccDataDir, vectors[1] + "_atan.txt")))

qcs = FormatData(GetData(os.path.join(simpAccDataDir, cordics[2] + "_sin.txt")))
qcc = FormatData(GetData(os.path.join(simpAccDataDir, cordics[2] + "_cos.txt")))
qca = FormatData(GetData(os.path.join(simpAccDataDir, vectors[2] + "_atan.txt")))

fcs = FormatData(GetData(os.path.join(simpAccDataDir, cordics[3] + "_sin.txt")))
fcc = FormatData(GetData(os.path.join(simpAccDataDir, cordics[3] + "_cos.txt")))
fca = FormatData(GetData(os.path.join(simpAccDataDir, vectors[3] + "_atan.txt")))

f.write("Table 3\n")
f.write("-" * (15 * 7) + "\n")
f.write("{:<15}{:<45}{:<45}\n".format("", "(a) our CORDIC", "(b) naive CORDIC"))
f.write("-" * (15 * 7) + "\n")
f.write("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format("", "sin", "cos", "atan", "sin", "cos", "atan"))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("max abs", ocs[5], occ[5], oca[5], ncs[5], ncc[5], nca[5]))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("avg abs", ocs[7], occ[7], oca[7], ncs[7], ncc[7], nca[7]))
f.write("{:<15}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n".format("max ulp", ocs[2], occ[2], oca[2], ncs[2], ncc[2], nca[2]))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("avg ulp", ocs[4], occ[4], oca[4], ncs[4], ncc[4], nca[4]))
f.write("{:<15}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n".format("# 0 ulp", ocs[1], occ[1], oca[1], ncs[1], ncc[1], nca[1]))
f.write("-" * (15 * 7) + "\n")
f.write("{:<15}{:<45}{:<45}\n".format("", "(c) Fast-Forwarded Iter.", "(d) Compute zi With Quire"))
f.write("-" * (15 * 7) + "\n")
f.write("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format("", "sin", "cos", "atan", "sin", "cos", "atan"))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("max abs", fcs[5], fcc[5], fca[5], qcs[5], qcc[5], qca[5]))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("avg abs", fcs[7], fcc[7], fca[7], qcs[7], qcc[7], qca[7]))
f.write("{:<15}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n".format("max ulp", fcs[2], fcc[2], fca[2], qcs[2], qcc[2], qca[2]))
f.write("{:<15}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}{:<15.2E}\n".format("avg ulp", fcs[4], fcc[4], fca[4], qcs[4], qcc[4], qca[4]))
f.write("{:<15}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n".format("# 0 ulp", fcs[1], fcc[1], fca[1], qcs[1], qcc[1], qca[1]))
f.write("\n")

f.close()
print("Table data output to " + tableDataFile)

# Make sure file is the same as expected file:
print("Comparing " + " to the expected table data in " + expectedFile)
contentSame = filecmp.cmp(tableDataFile, expectedFile, shallow=False)
if contentSame:
    print("The generated data is the same")
else :
    print("The generated data does not match. Please view " + tableDataFile + " and " + expectedFile + " to view the difference. There may be slight differences between the numbers")
