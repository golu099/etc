#!/bin/bash

# obtain a bash array of input files
inFiles=("$(ls -1 ./*.tsv | sort -V)")
echo $inFiles

outfilePath="combined.tsv"

header_printed=false
for f in ${inFiles[@]}; do 
    if [ $header_printed = false ]; then
        printf "file\t" > $outfilePath
        head -n1 $f >> $outfilePath
        header_printed=true
    fi
    awk -F\t 'NR!=1 {cmd=sprintf("basename %s",FILENAME)
        cmd | getline out
        print out,$0
        }' $f >> $outfilePath
 done
 cat $outfilePath