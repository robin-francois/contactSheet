#!/usr/bin/env bash

FOLDERNAME=${PWD##*/}
SCRIPTFOLDER=`dirname "$0"`


rm -rf "PLANCHE_${FOLDERNAME}"

find . -name "*CDD*" | grep -v "CaptureOne" | rev | cut -d"." -f2- | rev | xargs -P 3 -I {} convert -sampling-factor 4:4:4 -thumbnail '400x400>' -quality 80 -layers merge -quiet -profile ${SCRIPTFOLDER}/sRGB2014.icc "{}.tif" "{}_thumb.jpg"

mkdir "PLANCHE_${FOLDERNAME}"

find -name *thumb* | xargs -I {} mv {} "PLANCHE_${FOLDERNAME}/"

cd "PLANCHE_${FOLDERNAME}"

${SCRIPTFOLDER}/generate_table.py $FOLDERNAME ${FOLDERNAME}_planche_contact.md

pandoc --self-contained "${FOLDERNAME}_planche_contact.md" -o "${FOLDERNAME}_planche_contact.html"
