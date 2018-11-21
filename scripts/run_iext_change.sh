#!/bin/bash

# for conductances 

gLN = 0.1
gLNPN = 0.2
gPNLN = 0.075
gPN = 0.085

for i in 3 3.5
do
	python ~/scripts/network_create_13Aug/generate_ecs_template_nsets.py ~/dump/ecs_temp_test_gen.txt 2 1,1 90,30 20,40,3000,100,2800,20,20,4.5,0.5*7,15,3000,100,2800,20,20,${i},0.5

	python ~/scripts/network_create_13Aug/generate_nsets_LNPN_parallel_noise_pulse.py ~/work/AL_90_30/nsets_AL120_pP_PN4-5LN${i}_tauhigh_3000.isf 90 30 0 0 ~/dump/ecs_temp_test_gen.txt

	time ~/work/AL_90_30/insilico_PN90_LN30_noise_noPN-PN_3000.out -o ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-2LNPN0-075PNLN0-0875PN_PN4-5LN${1}_pmin0-05.csv -n ~/work/AL_90_30/nsets_AL120_pP_PN4-5LN${i}_tauhigh_3000.isf -s ~/work/AL_90_30/noPN-PN/ssets_AL120_g0-1LN0-2LNPN0-075PNLN0-0875PN.isf > ~/work/AL_90_30/PN90_LN30.log

	mkdir ~/work/AL_90_30/results/with_noise/g0-1LN0-2LNPN0-075PNLN0-0875PN_${i}LNext

	python ~/scripts/plot_csv_output_custom.py ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-2LNPN0-075PNLN0-0875PN_PN4-5LN${i}_pmin0-05.csv n40v,n45v,n50v,n55v,n65v,n75v,n95v,n105v,n45I_PeriodicPulse ~/work/AL_90_30/results/with_noise/g0-1LN0-2LNPN0-075PNLN0-0875PN_${i}LNext/sample_PNLN.png 

	python ~/scripts/plot_csv_output_custom_avg2.py ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-2LNPN0-075PNLN0-0875PN_PN4-5LN${i}_pmin0-05.csv 0*89 ~/work/AL_90_30/results/with_noise/g0-1LN0-2LNPN0-075PNLN0-0875PN_${i}LNext/avg_PN.png 

	python ~/scripts/plot_raster2.py ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-2LNPN0-075PNLN0-0875PN_PN4-5LN${i}_pmin0-05.csv 0*119 ~/work/AL_90_30/results/with_noise/g0-1LN0-2LNPN0-075PNLN0-0875PN_${i}LNext/raster_PNLN.png 

	mv ~/work/AL_90_30/PN90_LN30_3000_NpP_noPN-PN_g0-1LN0-2LNPN0-075PNLN0-0875PN_PN4-5LN${i}_pmin0-05.csv ~/work/AL_90_30/results/with_noise/g0-1LN0-2LNPN0-075PNLN0-0875PN_${i}LNext/
done	
