#!/bin/bash

while read line
do
  
#  python ../code-inject.py  "$nb_file"  
 # python ../code-inject.py  "$nb_file"  > log/$num.py
#   python ../call_chain.py  "$nb_file"  >> "nb-parse-info.txt"
#   python ../rule1.py  "$nb_file"  >> "rule-parse-info.txt"
#   python ../rule1.py  "$nb_file"  >> "rule-parse-info.txt"
 echo $line
 python type_annot.py $line

done < "top-100.txt"




