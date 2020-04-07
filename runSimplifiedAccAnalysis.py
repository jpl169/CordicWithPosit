import sys
import os
import shutil
import subprocess

binDir = "bin"
analysisDataDir = "analysisData"
simpAccDataDir = os.path.join(analysisDataDir, "forSimpleAccuracy")
cordics = [
    "float_cordic_1kstep",
    "posit_cordic_default_1kstep",
    "posit_cordic_quirez_1kstep",
    "posit_cordic_start_late_1kstep",
    "posit_cordic_quirez_start_late_1kstep"]

vectors = [
    "float_vector_1kstep",
    "posit_vector_default_1kstep",
    "posit_vector_quirez_1kstep",
    "posit_vector_start_late_1kstep",
    "posit_vector_quirez_start_late_1kstep"]

# Create analysis data folder
if not os.path.exists(analysisDataDir) :
    os.makedirs(analysisDataDir)
if not os.path.exists(simpAccDataDir) :
    os.makedirs(simpAccDataDir)

for v in vectors :
    # construct executable path
    exeString = os.path.join(binDir, v)
    # construct atan data path
    atanString = os.path.join(simpAccDataDir, v + "_atan.txt")

    print("Executing " + exeString + "...")
    proc = subprocess.Popen(["time", exeString, atanString])
    proc.communicate()

for c in cordics :
    # construct executable path
    exeString = os.path.join(binDir, c)
    # construct sin data path
    sinString = os.path.join(simpAccDataDir, c + "_sin.txt")
    # construct cos data path
    cosString = os.path.join(simpAccDataDir, c + "_cos.txt")

    print("Executing " + exeString + "...")
    proc = subprocess.Popen(["time", exeString, sinString, cosString])
    proc.communicate()


