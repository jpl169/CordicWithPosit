import sys
import os
import shutil
import subprocess

binDir = "bin"
analysisDir = "analysis"
analysisDataDir = "analysisData"
graphDataDir = os.path.join(analysisDataDir, "forGraph")
graphDir = "graph"
dataGen = [
    "sinpow2",
    "cosnearpi",
    "atanpow2"]
graphScript = [
    "sinpow2.py",
    "cosnearpi.py",
    "atanpow2.py"]

outputPdf = [
    "sin.pdf",
    "cos.pdf",
    "atan.pdf"
    ]


# Create analysis data folder
if not os.path.exists(analysisDataDir) :
    os.makedirs(analysisDataDir)
if not os.path.exists(graphDataDir) :
    os.makedirs(graphDataDir)
if not os.path.exists(graphDir) :
    os.makedirs(graphDir)

for i in range(3) :
    dg = dataGen[i];
    gs = graphScript[i];
    op = outputPdf[i];
    
    # construct executable path
    dataExeString = os.path.join(binDir, dg)
    # construct data txt path
    dataTxtString = os.path.join(graphDataDir, dg + ".txt")
    # construct graphScript path
    graphScriptString = os.path.join(analysisDir, gs)
    # construct output pdf path
    pdfString = os.path.join(graphDir, op)

    print("Generating " + op + " graph...")
    proc = subprocess.Popen([dataExeString, dataTxtString])
    proc.communicate()

    proc = subprocess.Popen(["python3", graphScriptString, dataTxtString, pdfString])
    proc.communicate()

    
