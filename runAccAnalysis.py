import sys
import os
import shutil
import subprocess
import itertools

PARALLEL = 4

def mygrouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e != None] for t in itertools.zip_longest(*args))

if len(sys.argv) == 2 :
    PARALLEL = int(sys.argv[1])
    if PARALLEL <= 0 :
        PARALLEL = 10

binDir = "bin"
analysisDataDir = "analysisData"
accDataDir = os.path.join(analysisDataDir, "forAccuracy")
cordics = [
    "float_cordic",
    "posit_cordic_default",
    "posit_cordic_quirez",
    "posit_cordic_ff",
    "posit_cordic_quirez_ff"]

vectors = ["float_vector",
           "posit_vector_default",
           "posit_vector_quirez",
           "posit_vector_ff",
           "posit_vector_quirez_ff"
           ]

# Create analysis data folder
if not os.path.exists(analysisDataDir) :
    os.makedirs(analysisDataDir)
if not os.path.exists(accDataDir) :
    os.makedirs(accDataDir);

executeList = []

for v in vectors :
    # construct executable path
    exeString = os.path.join(binDir, v)
    # construct sin data path
    atanString = os.path.join(accDataDir, v + "_atan.txt")
    executeList.append([exeString, atanString])
    
for c in cordics :
    # construct executable path
    exeString = os.path.join(binDir, c)
    # construct sin data path
    sinString = os.path.join(accDataDir, c + "_sin.txt")
    # construct cos data path
    cosString = os.path.join(accDataDir, c + "_cos.txt")
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
    print("")


