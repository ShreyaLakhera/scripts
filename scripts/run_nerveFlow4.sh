#!/bin/bash

#  random + k-partite network

# conductances
PP=0.0
PL=0.1
LP=1.0
LL=0.6

# external current
extPN=9
lowPN=5.5
basePN=4
thPN=7.5

extLN=4
lowLN=2
baseLN=1
thLN=2.5

rR_PN=10
rF_PN=10
rR_LN=10
rF_LN=10

st_PN=25
et_PN=1050
st_LN=25
et_LN=1050

nS_PN=30
mS_PN=45
nS_LN=30
mS_LN=15

# runtime
t=3000
nreps=8
nB=8
T=3000			# t*nB
offset_time=500

cd ~/work/nerveFlow-master/interactive/

# Create adjacency matrix file
matrix=1		# 0 for random, 1 for patterned
#python ~/scripts/network_create_13Aug/generate_adjacency_matrix_AL90_k-part_random.py ~/dump/adjmat_AL120_patterned.txt ~/dump/AM_k-part_random.png ~/work/nerveFlow-master/interactive/ach_mat.npy ~/work/nerveFlow-master/interactive/fgaba_mat.npy
source ~/venv/bin/activate

# Type of input
inpPN=1			# 0 for constant input to a subgroup, 1 for gaussian distributed
inpLN=0			# 0 for constant input to a subgroup, 1 for gaussian distributed

x=2
pd=50
IPI=100
for IPI in 450
	do

	et_PN=$(( $st_PN + $pd ))
	et_LN=${et_PN}
	t=$(( $pd + $IPI ))
	T=$(( $t * $nreps + ${offset_time} ))

	echo $t

	# create parameter file
	python gen_params_file.py ${PP},${PL},${LP},${LL} parameters.json

	# create input file
	python gen_current_input.py ${t},${nreps} ${inpPN} ${nS_PN},${mS_PN},${extPN},${lowPN},${basePN},${thPN},${st_PN},${et_PN},${rR_PN},${rF_PN} ${inpLN} ${nS_LN},${mS_LN},${extLN},${lowLN},${baseLN},${thLN},${st_LN},${et_LN},${rR_LN},${rF_LN} ${offset_time}

	# run caller script
	python caller2.py ${T} ${nB} ${matrix}

	# save folder name
	fname='gLN'${LL}'LNPN'${LP}'PNLN'${PL}'_extPN'${extPN}'LN'${extLN}'_lowPN'${lowPN}'LN'${lowLN}'_k-part_pd'${pd}'_thPN'${thPN}'LN'${thLN}'_IPI'${IPI}'ms_'${x}

	# analyse and save the output files to a folder
	python output2.py ${nB} ~/work/nerveFlow-master/interactive/ ${offset_time}
	mkdir ~/work/AL_90_30/nF1/results/${fname}
	mv ~/work/nerveFlow-master/interactive/current.png ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/current.npy ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/parameters.json ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_LN.png ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_PN.png ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_LN_o.png ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/raster_PN_o.png ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/PN_LFP.png ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/PN_LFP_power.png ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/spiketimes_PN.json ~/work/AL_90_30/nF1/results/${fname}/
	mv ~/work/nerveFlow-master/interactive/spiketimes_LN.json ~/work/AL_90_30/nF1/results/${fname}/
	cp ~/work/nerveFlow-master/interactive/ach_mat.npy ~/work/AL_90_30/nF1/results/${fname}/
	cp ~/work/nerveFlow-master/interactive/fgaba_mat.npy ~/work/AL_90_30/nF1/results/${fname}/

	for ((_i=1; _i<=$nB; _i++ ))
		do
		mv ~/work/nerveFlow-master/interactive/batch${_i}_part_1.npy ~/work/AL_90_30/nF1/results/${fname}/
		mv ~/work/nerveFlow-master/interactive/batch${_i}_part_2.npy ~/work/AL_90_30/nF1/results/${fname}/
		done
	done

deactivate
