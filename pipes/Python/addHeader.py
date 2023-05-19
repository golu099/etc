#!/usr/bin/python
import os
import sys 
import csv
import pandas as pd

with open(sys.argv[1], "rb") as text_file, open(sys.argv[2], "wb") as outfile:
    data = pd.read_tsv(sys.argv[1], header = 0, sep="\t", error_bad_lines=False, engine ='python', skip_blank_lines=True, skipinitialspace= True)
    #grab basename of file
    basenamePath= print(os.path.splitext(sys.argv[1])[0])
    #make new empty column
    addcolumn = csv.write(outfile)
    for row in csv.reader(text_file):
        addcolumn.writerow(row+['Plasmid Name'])
        data['Plasmid Name'] =  data['Plasmid Name'].astype(str)
text_file.close()
outfile.close()
