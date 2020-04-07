import sys
import os
import shutil
import subprocess

binDir = "bin"
analysisDataDir = "analysisData"
accDataDir = os.path.join(analysisDataDir, "forAccuracy")
cordics = [
    "float_cordic",
    "posit_cordic_default",
    "posit_cordic_quirez",
    "posit_cordic_start_late",
    "posit_cordic_quirez_start_late"]

cordics_estimated = [
    "2 hours",
    "8 hours",
    "8 hours",
    "8 hours",
    "8 hours"]

vectors = ["float_vector",
           "posit_vector_default",
           "posit_vector_quirez",
           "posit_vector_start_late",
           "posit_vector_quirez_start_late"
           ]
    
vectors_estimated = [
    "2 hours",
    "13 hours",
    "13 hours",
    "13 hours",
    "13 hours"]

# Create analysis data folder
if not os.path.exists(analysisDataDir) :
    os.makedirs(analysisDataDir)
if not os.path.exists(accDataDir) :
    os.makedirs(accDataDir);

for (v, e) in zip(vectors, vectors_estimated) :
    # construct executable path
    exeString = os.path.join(binDir, v)
    # construct sin data path
    atanString = os.path.join(accDataDir, v + "_atan.txt")

    print("Executing " + exeString + "...")
    print("Estimated time: " + e)
    proc = subprocess.Popen(["time", exeString, atanString])
    proc.communicate()

for (c, e) in zip(cordics, cordics_estimated) :
    # construct executable path
    exeString = os.path.join(binDir, c)
    # construct sin data path
    sinString = os.path.join(accDataDir, c + "_sin.txt")
    # construct cos data path
    cosString = os.path.join(accDataDir, c + "_cos.txt")

    print("Executing " + exeString + "...")
    print("Estimated time: " + e)
    proc = subprocess.Popen(["time", exeString, sinString, cosString])
    proc.communicate()


