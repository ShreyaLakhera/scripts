#!/bin/bash

t='1000'
LL='0-15'
PP='0-175'


low_PN=0.2
low_LN=0.1
base_PN=0
base_LN=0
ampNoise_PN=0.8
ampNoise_LN=0.5
iext_LN=1.3
iext_PN=4.7

for LP in '0-3' '0-2' '0-1' '0-05'
	do
	for PL in '0-001' '0-003' '0-005'
		do
		for ext in 'PN0-8LN2' 'PN0-6LN2' 'PN0-4LN2' 'PN0-8LN2-5' 'PN0-6LN2-5' 'PN0-4LN2-5' 
			do
			g_LP=${LP/-/.}
			g_PL=${PL/-/.}
			g_PP=${PP/-/.}
			g_LL=${LL/-/.}
			g='g'${LL}'LN'${LP}'LNPN'${PL}'PNLN'${PP}'PN'
			gval=${g_PP}','${g_PL}','${g_LP}','${g_LL}

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

			python ~/scripts/network_create_13Aug/generate_ecs_template_nsets.py ~/scripts/network_create_13Aug/ecs_temp_test.txt 2 1,1 90,30 30,45,1000,100,800,20,20,${ext_PN},${base_PN},${low_PN}*10,15,1000,100,800,20,20,${ext_LN},${base_LN},${low_LN}

			python ~/scripts/network_create_13Aug/generate_nsets_LNPN_parallel_noise_pulse.py ~/work/AL_90_30/nsets/${t}/nsets_AL120_${ext}_${t}_basePN${base_PN/./-}LN${base_LN/./-}.isf 90 30 ${iext_PN} ${iext_LN} ${ampNoise_PN} ${ampNoise_LN} ~/scripts/network_create_13Aug/ecs_temp_test.txt

			python ~/scripts/network_create_13Aug/generate_ssets_custom_lower.py ~/work/AL_90_30/noPN-PN/ssets_AL120_${g}.isf 2 90,30 0,0.5,0.5,0.5 ${gval}

			time ~/work/AL_90_30/insilico_PN90_LN30_noise_noPN-PN_${t}.out -o ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv -n ~/work/AL_90_30/nsets/${t}/nsets_AL120_${ext}_${t}_basePN${base_PN/./-}LN${base_LN/./-}.isf -s ~/work/AL_90_30/noPN-PN/ssets_AL120_${g}.isf > ~/work/AL_90_30/PN90_LN30.log
	
		
			mkdir ~/work/AL_90_30/results/oscillations/${g}_${ext}/

			cp ~/work/AL_90_30/PN90_LN30_${t}_${g}_${ext}.csv ~/work/AL_90_30/results/oscillations/${g}_${ext}/

			~/scripts/run_plots.sh ${g} ${ext} ${t}

			mv ~/work/AL_90_30/results/oscillations/${g}_${ext}/ ~/work/AL_90_30/results/oscillations/${g}_${ext}_${t}_basePN${base_PN/./-}LN${base_LN/./-}_ampNoisePN${ampNoise_PN/./-}LN${ampNoise_LN/./-}_iextPN${iext_PN}LN${iext_LN}/

			done
		done
	done


