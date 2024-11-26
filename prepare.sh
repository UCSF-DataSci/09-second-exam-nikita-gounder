#!/bin/bash

python3 generate_dirty_data.py

#Remove comment lines, empty lines, extra commas + Extract essential columns
grep -v "#" ms_data_dirty.csv | sed -e '/^$/d' |  sed -e 's/,,/,/g' | cut -d',' -f1,2,4,5,6 > ms_data.csv 

#new file + new column insurance type
echo -e "Basic \nBetter \nBest" > insurance.lst

#Count the total number of visits/rows +  Display the first few records
wc -l ms_data.csv 
head ms_data.csv


#make script executable with: chmod +x prepare.sh
#run script: bash prepare.sh