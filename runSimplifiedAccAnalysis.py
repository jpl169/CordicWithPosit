import sys
import os
import shutil
import subprocess
import itertools

PARALLEL = 4

def mygrouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e != None] for t in itertools.zip_longest(*args))

binDir = "bin"
analysisDataDir = "analysisData"
simpAccDataDir = os.path.join(analysisDataDir, "forSimpleAccuracy")
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

# Create analysis data folder
if not os.path.exists(analysisDataDir) :
    os.makedirs(analysisDataDir)
if not os.path.exists(simpAccDataDir) :
    os.makedirs(simpAccDataDir)

executeList = []
    
for v in vectors :
    # construct executable path
    exeString = os.path.join(binDir, v)
    # construct atan data path
    atanString = os.path.join(simpAccDataDir, v + "_atan.txt")
    executeList.append([exeString, atanString])

for c in cordics :
    # construct executable path
    exeString = os.path.join(binDir, c)
    # construct sin data path
    sinString = os.path.join(simpAccDataDir, c + "_sin.txt")
    # construct cos data path
    cosString = os.path.join(simpAccDataDir, c + "_cos.txt")
    executeList.append([exeString, sinString, cosString])

executeList = mygrouper(PARALLEL, executeList)
    
for sublist in executeList :
    processes = []
    for exe in sublist :
        print("Executing " + exe[0] + " ...")
        proc = subprocess.Popen(exe)
        processes.append(proc)

    for proc in processes :
        proc.wait()

