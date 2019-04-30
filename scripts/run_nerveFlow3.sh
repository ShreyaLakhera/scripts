#!/bin/bash

# ordered network

# conductances
PP=0.0
PL=0.1
LP=1.0
LL=0.6

# external current
extPN=5.5
lowPN=4.5
basePN=4
thPN=3

extLN=4
lowLN=3.5
baseLN=1
thLN=3

rR_PN=10
rF_PN=10
rR_LN=10
rF_LN=10

st_PN=25
et_PN=75
st_LN=25
et_LN=75

nS_PN=30
mS_PN=15
nS_LN=10
mS_LN=5

# runtime
t=350
nreps=8
nB=4
T=2100			# t*nreps
offset_time=500

cd ~/work/nerveFlow-master/interactive/

# Create adjacency matrix file
matrix=1		# 0 for random, 1 for patterned
python ~/scripts/network_create_13Aug/generate_adjacency_matrix_AL90_patterned.py ~/dump/adjmat_AL120_patterned.txt ~/dump/ach_mat.png ~/work/nerveFlow-master/interactive/ach_mat.npy ~/work/nerveFlow-master/interactive/fgaba_mat.npy    #----commented so that only 1 given matrix is used. 

# Type of input
inpPN=0			# 0 for constant input to a subgroup, 1 for gaussian distributed
inpLN=0			# 0 for constant input to a subgroup, 1 for gaussian distributed

mkdir ~/work/AL_90_30/nF1/results_pat_${extPN}

source ~/venv/bin/activate

for x in 2
	do
	for t in 100 150 250 500
		do

		T=$(( $t * $nreps + ${offset_time}))
		echo $T
		IPI=$(( $t - 50))
		echo $IPI
	
		# create parameter file
		python gen_params_file.py ${PP},${PL},${LP},${LL} parameters.json
	
		# create input file
		python gen_current_input.py ${t},${nreps} ${inpPN} ${nS_PN},${mS_PN},${extPN},${lowPN},${basePN},${thPN},${st_PN},${et_PN},${rR_PN},${rF_PN} ${inpLN} ${nS_LN},${mS_LN},${extLN},${lowLN},${baseLN},${thLN},${st_LN},${et_LN},${rR_LN},${rF_LN} ${offset_time}

		# run caller script
		python caller2.py ${T} ${nB} ${matrix} 		# matrix = 0 if you want to generate the matrix, anything else to take existing matrix

		# save folder name
		fname='gLN'${LL}'LNPN'${LP}'PNLN'${PL}'_extPN'${extPN}'LN'${extLN}'_lowPN'${lowPN}'LN'${lowLN}'_pulse50ms_IPI'${IPI}'ms_'${x}

		# analyse and save the output files to a folder
		python output2.py ${nB} ~/work/nerveFlow-master/interactive/ ${offset_time}
		mkdir ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}
		mv ~/work/nerveFlow-master/interactive/current.png ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/current.npy ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/parameters.json ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/raster_LN.png ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/raster_PN.png ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/raster_LN_o.png ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/raster_PN_o.png ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/PN_LFP.png ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/PN_LFP_power.png ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/spiketimes_PN.json ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
		mv ~/work/nerveFlow-master/interactive/spiketimes_LN.json ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/	

		for ((_i=1; _i<=$nB; _i++ ))
			do
			mv ~/work/nerveFlow-master/interactive/batch${_i}_part_1.npy ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
			mv ~/work/nerveFlow-master/interactive/batch${_i}_part_2.npy ~/work/AL_90_30/nF1/results_pat_${extPN}/${fname}/
			done
	
		done

	cp ~/work/nerveFlow-master/interactive/ach_mat.npy ~/work/AL_90_30/nF1/results_pat_${extPN}/
	cp ~/work/nerveFlow-master/interactive/fgaba_mat.npy ~/work/AL_90_30/nF1/results_pat_${extPN}/
	
	done

deactivate
