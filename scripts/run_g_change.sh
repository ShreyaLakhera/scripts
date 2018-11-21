#!/bin/bash

for i in 1 05 075 025
do
	python ~/scripts/network_create_13Aug/generate_ssets_custom_lower.py ~/work/AL_90_30/noPN-PN/ssets_AL120_g0-1LN0-${i}LNPN0-075PNLN0-0875PN.isf 2 90,30 0,0.5,0.5,0.5 0.0875,0.075,0.${i},0.1

	time ~/work/AL_90_30/insilico_PN90_LN30_noise_noPN-PN_3000.out -o ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-${i}LNPN0-075PNLN0-0875PN_PN4-5LN2-5_pmin0-05.csv -n ~/work/AL_90_30/nsets_AL120_pP_PN4-5LN2-5_tauhigh_3000.isf -s ~/work/AL_90_30/noPN-PN/ssets_AL120_g0-1LN0-${i}LNPN0-075PNLN0-0875PN.isf > ~/work/AL_90_30/PN90_LN30.log

	mkdir ~/work/AL_90_30/results/with_noise/g0-1LN0-${i}LNPN0-075PNLN0-0875PN

	python ~/scripts/plot_csv_output_custom.py ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-${i}LNPN0-075PNLN0-0875PN_PN4-5LN2-5_pmin0-05.csv n40v,n45v,n50v,n55v,n65v,n75v,n95v,n105v,n45I_PeriodicPulse ~/work/AL_90_30/results/with_noise/g0-1LN0-${i}LNPN0-075PNLN0-0875PN/sample_PNLN.png 

	python ~/scripts/plot_csv_output_custom_avg2.py ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-${i}LNPN0-075PNLN0-0875PN_PN4-5LN2-5_pmin0-05.csv 0*89 ~/work/AL_90_30/results/with_noise/g0-1LN0-${i}LNPN0-075PNLN0-0875PN/avg_PN.png 

	python ~/scripts/plot_raster2.py ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-${i}LNPN0-075PNLN0-0875PN_PN4-5LN2-5_pmin0-05.csv 0*119 ~/work/AL_90_30/results/with_noise/g0-1LN0-${i}LNPN0-075PNLN0-0875PN/raster_PNLN.png 

	mv ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-${i}LNPN0-075PNLN0-0875PN_PN4-5LN2-5_pmin0-05.csv ~/work/AL_90_30/results/with_noise/g0-1LN0-${i}LNPN0-075PNLN0-0875PN/
done	
