#!/bin/bash

t='1000'

g='g0-15LN4-0LNPN0-0005PNLN0-175PN'
gval='0.175,0.0005,4.0,0.15'
ext='PN4-75LN4'

ep=$(echo `expr index "$ext" P`)
el=$(echo `expr index "$ext" L`)
gt1=$(echo `expr $ep + 2`)
gt2=$(echo `expr $el - 1`)
gt3=$(echo `expr $el + 1`)
ext_PN1=$(echo ${ext} | cut -c$gt1-$gt2)
ext_LN1=${ext:gt3}
ext_PN=${ext_PN1/-/.}
ext_LN=${ext_LN1/-/.}

echo $ext_PN
echo $ext_LN


base_PN=1.5
base_LN=1
low_PN=1.5
low_LN=1
ampNoise_PN=1.2
ampNoise_LN=0.4
iext_PN=0.9
iext_LN=0.5

python ~/scripts/network_create_13Aug/generate_ecs_template_nsets.py ~/scripts/network_create_13Aug/ecs_temp_test.txt 2 1,1 90,30 30,45,1000,100,800,20,20,${ext_PN},${base_PN},${low_PN}*10,15,1000,100,800,20,20,${ext_LN},${base_LN},${low_LN}

python ~/scripts/network_create_13Aug/generate_nsets_LNPN_parallel_noise_pulse.py ~/work/AL_90_30/nsets/1000/nsets_AL120_${ext}_${t}_basePN${base_PN/./-}LN${base_LN/./-}.isf 90 30 ${iext_PN} ${iext_LN} ${ampNoise_PN} ${ampNoise_LN} ~/scripts/network_create_13Aug/ecs_temp_test.txt

python ~/scripts/network_create_13Aug/generate_ssets_custom_lower.py ~/work/AL_90_30/noPN-PN/ssets_AL120_${g}.isf 2 90,30 0,0.5,0.5,0.5 ${gval}

time ~/work/AL_90_30/insilico_PN90_LN30_noise_noPN-PN_${t}.out -o ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv -n ~/work/AL_90_30/nsets/${t}/nsets_AL120_${ext}_${t}_basePN${base_PN/./-}LN${base_LN/./-}.isf -s ~/work/AL_90_30/noPN-PN/ssets_AL120_${g}.isf > ~/work/AL_90_30/PN90_LN30.log

mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/

cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/

~/scripts/run_plots.sh ${g} ${ext}

mv ~/work/AL_90_30/results/oscillations/${g}_${ext}/ ~/work/AL_90_30/results/oscillations/${g}_${ext}_basePN${base_PN/./-}LN${base_LN/./-}_ampNoisePN${ampNoise_PN/./-}LN${ampNoise_LN/./-}_iextPN${iext_PN}LN${iext_LN}/


base_PN=1.5
base_LN=1
low_PN=1.5
low_LN=1
ampNoise_PN=1.2
ampNoise_LN=0.4
iext_PN=0.875
iext_LN=0.5

python ~/scripts/network_create_13Aug/generate_ecs_template_nsets.py ~/scripts/network_create_13Aug/ecs_temp_test.txt 2 1,1 90,30 30,45,1000,100,800,20,20,${ext_PN},${base_PN},${low_PN}*10,15,1000,100,800,20,20,${ext_LN},${base_LN},${low_LN}

python ~/scripts/network_create_13Aug/generate_nsets_LNPN_parallel_noise_pulse.py ~/work/AL_90_30/nsets/1000/nsets_AL120_${ext}_${t}_basePN${base_PN/./-}LN${base_LN/./-}.isf 90 30 ${iext_PN} ${iext_LN} ${ampNoise_PN} ${ampNoise_LN} ~/scripts/network_create_13Aug/ecs_temp_test.txt

python ~/scripts/network_create_13Aug/generate_ssets_custom_lower.py ~/work/AL_90_30/noPN-PN/ssets_AL120_${g}.isf 2 90,30 0,0.5,0.5,0.5 ${gval}

time ~/work/AL_90_30/insilico_PN90_LN30_noise_noPN-PN_${t}.out -o ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv -n ~/work/AL_90_30/nsets/${t}/nsets_AL120_${ext}_${t}_basePN${base_PN/./-}LN${base_LN/./-}.isf -s ~/work/AL_90_30/noPN-PN/ssets_AL120_${g}.isf > ~/work/AL_90_30/PN90_LN30.log

mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/

cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/

~/scripts/run_plots.sh ${g} ${ext}

mv ~/work/AL_90_30/results/oscillations/${g}_${ext}/ ~/work/AL_90_30/results/oscillations/${g}_${ext}_basePN${base_PN/./-}LN${base_LN/./-}_ampNoisePN${ampNoise_PN/./-}LN${ampNoise_LN/./-}_iextPN${iext_PN}LN${iext_LN}/


base_PN=1.5
base_LN=1
low_PN=1.5
low_LN=1
ampNoise_PN=1.2
ampNoise_LN=0.4
iext_PN=0.95
iext_LN=0.5

python ~/scripts/network_create_13Aug/generate_ecs_template_nsets.py ~/scripts/network_create_13Aug/ecs_temp_test.txt 2 1,1 90,30 30,45,1000,100,800,20,20,${ext_PN},${base_PN},${low_PN}*10,15,1000,100,800,20,20,${ext_LN},${base_LN},${low_LN}

python ~/scripts/network_create_13Aug/generate_nsets_LNPN_parallel_noise_pulse.py ~/work/AL_90_30/nsets/1000/nsets_AL120_${ext}_${t}_basePN${base_PN/./-}LN${base_LN/./-}.isf 90 30 ${iext_PN} ${iext_LN} ${ampNoise_PN} ${ampNoise_LN} ~/scripts/network_create_13Aug/ecs_temp_test.txt

python ~/scripts/network_create_13Aug/generate_ssets_custom_lower.py ~/work/AL_90_30/noPN-PN/ssets_AL120_${g}.isf 2 90,30 0,0.5,0.5,0.5 ${gval}

time ~/work/AL_90_30/insilico_PN90_LN30_noise_noPN-PN_${t}.out -o ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv -n ~/work/AL_90_30/nsets/${t}/nsets_AL120_${ext}_${t}_basePN${base_PN/./-}LN${base_LN/./-}.isf -s ~/work/AL_90_30/noPN-PN/ssets_AL120_${g}.isf > ~/work/AL_90_30/PN90_LN30.log

mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/

cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/

~/scripts/run_plots.sh ${g} ${ext}

mv ~/work/AL_90_30/results/oscillations/${g}_${ext}/ ~/work/AL_90_30/results/oscillations/${g}_${ext}_basePN${base_PN/./-}LN${base_LN/./-}_ampNoisePN${ampNoise_PN/./-}LN${ampNoise_LN/./-}_iextPN${iext_PN}LN${iext_LN}/


