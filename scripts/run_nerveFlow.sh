#!/bin/bash


# conductances
PP=0.0
PL=0.1
LP=1.0
LL=0.6

# external current
extPN=6
lowPN=2
basePN=1

extLN=4
lowLN=2
baseLN=1

rR_PN=10
rF_PN=10
rR_LN=10
rF_LN=10

st_PN=200
et_PN=300
st_LN=200
et_LN=300

nS_PN=30
mS_PN=15
nS_LN=29
mS_LN=15

# runtime
t=600
nreps=5
nB=4
T=3000			# t*nB


cd ~/work/nerveFlow-master/interactive/

# Create adjacency matrix file
matrix=1		# 0 for random, 1 for patterned
python ~/scripts/network_create_13Aug/generate_adjacency_matrix_AL90_patterned.py ~/dump/adjmat_AL120_patterned.txt ~/dump/ach_mat.png ~/work/nerveFlow-master/interactive/ach_mat.npy ~/work/nerveFlow-master/interactive/fgaba_mat.npy
source ~/venv/bin/activate


for x in 2 3
	do

	# create parameter file
	python gen_params_file.py ${PP},${PL},${LP},${LL} parameters.json

	# create input file
	python gen_current_input.py ${t},${nreps} 0 ${nS_PN},${mS_PN},${extPN},${lowPN},${basePN},${st_PN},${et_PN},${rR_PN},${rF_PN} 0 ${nS_LN},${mS_LN},${extLN},${lowLN},${baseLN},${st_LN},${et_LN},${rR_LN},${rF_LN}

	# run caller script
	python caller2.py ${T} ${nB} ${matrix} 		# matrix = 0 if you want to generate the matrix, anything else to take existing matrix

	# save folder name
	fname='gLN'${LL}'LNPN'${LP}'PNLN'${PL}'_extPN'${extPN}'LN'${extLN}'_pulse100ms_IPI500ms_'${x}

	# analyse and save the output files to a folder
	python output2.py ${nB} ~/work/nerveFlow-master/interactive/
	mkdir ~/work/AL_90_30/nF/results/${fname}
	mv ~/work/nerveFlow-master/interactive/current.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/current.npy ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/parameters.json ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_LN.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_PN.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/PN_LFP.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/PN_LFP_power.png ~/work/AL_90_30/nF/results/${fname}/

	done


st_PN=100
et_PN=100
st_LN=100
et_LN=100

# runtime
t=300
nreps=10
nB=4
T=3000			# t*nB


for x in 1 2 3
	do

	# create parameter file
	python gen_params_file.py ${PP},${PL},${LP},${LL} parameters.json

	# create input file
	python gen_current_input.py ${t},${nreps} 0 ${nS_PN},${mS_PN},${extPN},${lowPN},${basePN},${st_PN},${et_PN},${rR_PN},${rF_PN} 0 ${nS_LN},${mS_LN},${extLN},${lowLN},${baseLN},${st_LN},${et_LN},${rR_LN},${rF_LN}

	# run caller script
	python caller2.py ${T} ${nB} ${matrix} 		# matrix = 0 if you want to generate the matrix, anything else to take existing matrix

	# save folder name
	fname='gLN'${LL}'LNPN'${LP}'PNLN'${PL}'_extPN'${extPN}'LN'${extLN}'_pulse100ms_IPI100ms_'${x}

	# analyse and save the output files to a folder
	python output2.py ${nB} ~/work/nerveFlow-master/interactive/
	mkdir ~/work/AL_90_30/nF/results/${fname}
	mv ~/work/nerveFlow-master/interactive/current.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/current.npy ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/parameters.json ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_LN.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_PN.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/PN_LFP.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/PN_LFP_power.png ~/work/AL_90_30/nF/results/${fname}/

	for ((_i=1; _i<=$nB; _i++ ))
		do
		mv ~/work/nerveFlow-master/interactive/batch${_i}_part_1.npy ~/work/AL_90_30/nF/results/${fname}/
		mv ~/work/nerveFlow-master/interactive/batch${_i}_part_2.npy ~/work/AL_90_30/nF/results/${fname}/
		done

	done

st_PN=100
et_PN=2900
st_LN=100
et_LN=2900

# runtime
t=3000
nreps=1
nB=4
T=3000			# t*nB


for x in 1 2 3
	do

	# create parameter file
	python gen_params_file.py ${PP},${PL},${LP},${LL} parameters.json

	# create input file
	python gen_current_input.py ${t},${nreps} 0 ${nS_PN},${mS_PN},${extPN},${lowPN},${basePN},${st_PN},${et_PN},${rR_PN},${rF_PN} 0 ${nS_LN},${mS_LN},${extLN},${lowLN},${baseLN},${st_LN},${et_LN},${rR_LN},${rF_LN}

	# run caller script
	python caller2.py ${T} ${nB} ${matrix} 		# matrix = 0 if you want to generate the matrix, anything else to take existing matrix

	# save folder name
	fname='gLN'${LL}'LNPN'${LP}'PNLN'${PL}'_extPN'${extPN}'LN'${extLN}'_pulse2800ms_IPI0ms_'${x}

	# analyse and save the output files to a folder
	python output2.py ${nB} ~/work/nerveFlow-master/interactive/
	mkdir ~/work/AL_90_30/nF/results/${fname}
	mv ~/work/nerveFlow-master/interactive/current.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/current.npy ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/parameters.json ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_LN.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_PN.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/PN_LFP.png ~/work/AL_90_30/nF/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/PN_LFP_power.png ~/work/AL_90_30/nF/results/${fname}/

	for ((_i=1; _i<=$nB; _i++ ))
		do
		mv ~/work/nerveFlow-master/interactive/batch${_i}_part_1.npy ~/work/AL_90_30/nF/results/${fname}/
		mv ~/work/nerveFlow-master/interactive/batch${_i}_part_2.npy ~/work/AL_90_30/nF/results/${fname}/
		done

	done


deactivate
