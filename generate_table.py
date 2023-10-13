#!/usr/bin/env python3

import sys
import glob
import pathlib
import os
import re

import sys, os, pathlib
from pathlib import Path


srcFolder = sys.argv[1]
outputFilePath = sys.argv[2]

regexCallNumber= r"CSZ.[0-9-a-z]*"

srcPath = os.path.dirname(os.path.abspath(srcFolder))


def generate_all_files(root: Path, only_files: bool = True):
    for p in root.rglob("*_thumb.jpg"):
        if only_files and not p.is_file():
            continue
        yield p

filelist_path = generate_all_files(Path(srcPath), only_files=True)
fileList = list()

for file_path in filelist_path:
    fileList.append(file_path.as_posix())

fileList.sort()

with open(outputFilePath,"w") as outputFile:
    for i in range(0,int(len(fileList)/3+1)):
        filelist_slice = fileList[i*3:(i+1)*3]
        if len(filelist_slice)>1:
            headerTotal = ""
            sepTotal = ""
            imgTotal = ""
            for elePath in filelist_slice: 
                ele = pathlib.Path(elePath).name
                width = len(ele)+5
                cote = re.search(regexCallNumber,ele)
                header = "| " + cote.group().ljust(width) + " |"
                img = "| ![]("+ ele + ") |"
                sep = "|:" + "".ljust(width,"-") + ":|"
                imgTotal += img
                sepTotal += sep
                headerTotal += header
            headerTotal = headerTotal.replace("||","|")
            sepTotal = sepTotal.replace("||","|")
            imgTotal = imgTotal.replace("||","|")
            outputFile.write(headerTotal+"\n")
            outputFile.write(sepTotal+"\n")
            outputFile.write(imgTotal+"\n")
            outputFile.write("\n")
            outputFile.write("---\n")
            outputFile.write("\n")
        if len(filelist_slice)==1:
            ele = pathlib.Path(filelist_slice[0]).name
            cote = re.search(regexCallNumber,ele)
            outputFile.write("!["+cote.group()+"]("+ele+")\n")
            outputFile.write("\n---\n")
        else:
            continue
