#!/bin/bash

ext='PN7LN5'
t='1000'

g='g0-1LN0-25LNPN0-08PNLN0-175PN'
gval='0.175,0.08,0.25,0.1'
mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/
cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/
~/scripts/run_plots.sh ${g} ${ext}

g='g0-1LN0-25LNPN0-06PNLN0-175PN'
gval='0.175,0.06,0.25,0.1'
mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/
cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/
~/scripts/run_plots.sh ${g} ${ext}

g='g0-13LN0-25LNPN0-1PNLN0-175PN'
gval='0.175,0.1,0.25,0.13'

mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/
cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/
~/scripts/run_plots.sh ${g} ${ext}

g='g0-15LN0-25LNPN0-1PNLN0-175PN'
gval='0.175,0.1,0.25,0.15'
mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/
cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/
~/scripts/run_plots.sh ${g} ${ext}

g='g0-17LN0-25LNPN0-1PNLN0-175PN'
gval='0.175,0.1,0.25,0.17'
mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/
cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/
~/scripts/run_plots.sh ${g} ${ext}

g='g0-13LN0-25LNPN0-08PNLN0-175PN'
gval='0.175,0.08,0.25,0.13'
mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/
cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/
~/scripts/run_plots.sh ${g} ${ext}

g='g0-13LN0-25LNPN0-06PNLN0-175PN'
gval='0.175,0.06,0.25,0.13'
mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/
cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/
~/scripts/run_plots.sh ${g} ${ext}

