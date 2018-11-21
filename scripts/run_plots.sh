#!/bin/bash

#g="g0-1LN0-25LNPN0-1PNLN0-175PN"
#ext="PN5LN3"

g=$1
ext=$2
t=$3

python ~/scripts/plot_raster-s.py ~/work/AL_90_30/results/oscillations/${g}_${ext}/PN90_LN30_${t}_${g}_${ext}.csv 0*89 ~/work/AL_90_30/results/oscillations/${g}_${ext}/raster_PN.png

python ~/scripts/plot_raster-s.py ~/work/AL_90_30/results/oscillations/${g}_${ext}/PN90_LN30_${t}_${g}_${ext}.csv 90*119 ~/work/AL_90_30/results/oscillations/${g}_${ext}/raster_LN.png

python ~/scripts/plot_csv_output_custom-s.py ~/work/AL_90_30/results/oscillations/${g}_${ext}/PN90_LN30_${t}_${g}_${ext}.csv n15v,n30v,n45v,n95v,n100v,n105v,n45I_PeriodicPulse ~/work/AL_90_30/results/oscillations/${g}_${ext}/sample_PNLN.png

python ~/scripts/plot_csv_output_custom_avg-s.py ~/work/AL_90_30/results/oscillations/${g}_${ext}/PN90_LN30_${t}_${g}_${ext}.csv 0*89 ~/work/AL_90_30/results/oscillations/${g}_${ext}/avg_PN.png
