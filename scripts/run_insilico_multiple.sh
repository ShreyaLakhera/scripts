#!/bin/bash

g=''
ext='PN5LN3'
t=''

time ./insilico_PN90_LN30_noise_noPN-PN_${t}.out -o ./PN90_LN30_${t}_${g}_${ext}.csv -n ./nsets/${t}/nsets_AL120_${ext}_${t}.isf -s ./noPN-PN/ssets_AL120_${g}.isf > ./PN90_LN30.log
