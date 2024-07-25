#!/bin/bash

echo
echo "Initial Block:"
echo
read Initial_Block

echo
echo "Final Block:"
echo
read Final_Block

echo 
echo "Quantidade de Arquivos a serem analisados:"
echo
read Qntd_Arquivos


for (( i=1; i<=$Qntd_Arquivos; i++)) do

    python3 Query.py $Initial_Block $Final_Block

    Initial_Block=$((Initial_Block+10000))
    Final_Block=$((Final_Block+10000))
done