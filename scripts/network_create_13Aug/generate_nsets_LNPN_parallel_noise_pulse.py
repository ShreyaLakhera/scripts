import sys

# Initialize all input required (Number of neurons, which parameters to write, the file to write it in, the default values of these parameters)

outfilename = sys.argv[1]			# Enter the address to write nsets file to, eg: /address/nsets.isf
number_PN = int(sys.argv[2])			# Enter the number of PNs
number_LN = int(sys.argv[3])			# Enter the number of LNs
I_ext_PN = float(sys.argv[4])			# The external current that you want to add in all PNs
I_ext_LN = float(sys.argv[5])			# The external current that you want to add in all LNs
ampNoise_PN = float(sys.argv[6])
ampNoise_LN = float(sys.argv[7])
pulsefilename = sys.argv[8]                     # The name of the file that has values for adding the pulse for all data

parameters_LN = ['dxdt', 'v', 'mk', 'mca', 'hca', 'nk', 'CA_DRIVE', 'I_KCA', 'I_CA', 'I_K_LN', 'I_LEAK', 'I_KLEAK','I_LEAK_LN', 'I_KLEAK_LN', 'iext', 'last_spike', 'ampNoise', 'I_Noise', 'PulseDuration', 'PulseStart', 'PulseEnd', 'tau_rise', 'tau_fall', 'PulseMax', 'PulseMin', 'I_PeriodicPulse']
parameters_PN = ['dxdt', 'v', 'm', 'h', 'n', 'ma', 'ha', 'I_NA', 'I_K', 'I_A', 'I_LEAK', 'I_KLEAK', 'I_LEAK_LN', 'I_KLEAK_LN','I_ext', 'last_spike', 'ampNoise', 'I_Noise', 'PulseDuration', 'PulseStart', 'PulseEnd', 'tau_rise', 'tau_fall', 'PulseMax', 'PulseMin', 'I_PeriodicPulse']

values_LN = {'dxdt' : '7',
  	  'v' : '-60',
	  'mk' : '0',
	  'mca' : '0',
	  'hca' : '0',
	  'nk' : '0',
	  'CA_DRIVE' : '0.00024',
	  'I_KCA' : '0',
	  'I_CA' : '0',
	  'I_K_LN' : '0',
	  'I_LEAK' : '0',
	  'I_KLEAK' : '0',
	  'I_LEAK_LN' : '0',
	  'I_KLEAK_LN' : '0',
	  'last_spike' : -10,
          'ampNoise' : ampNoise_LN,
          'I_Noise' : '0',
          'PulseDuration' : '0',
          'PulseStart' : '0', 
          'PulseEnd' : '0',
          'tau_rise' : '0',
          'tau_fall' : '0',
          'PulseMax' : '0', 
          'PulseMin' : '0',
          'I_PeriodicPulse' : '0',
	  'iext' : I_ext_LN}

values_PN = {'dxdt' : '6',
  	  'v' : '-60',
	  'm' : '0',
	  'h' : '0',
	  'n' : '0',
	  'ma' : '0',
	  'ha' : '0',
	  'I_NA' : '0',
	  'I_K' : '0',
	  'I_A' : '0',
	  'I_LEAK' : '0',
	  'I_KLEAK' : '0',
	  'I_LEAK_LN' : '0',
	  'I_KLEAK_LN' : '0',
	  'I_ext' : I_ext_PN,
          'ampNoise' : ampNoise_PN,
          'I_Noise' : '0',
          'PulseDuration' : '0',
          'PulseStart' : '0', 
          'PulseEnd' : '0',
          'tau_rise' : '0',
          'tau_fall' : '0',
          'PulseMax' : '0', 
          'PulseMin' : '0',
          'I_PeriodicPulse' : '0',
	  'last_spike' : -10}


# Read Pulse parameters from pulse-template-file

pulsefile = open(pulsefilename, 'r')

pulseData = []
for line in pulsefile:
        l = line.strip('\n').split(',')
        pulseData.append(l)


#print(pulseData)
#print('Pulse parameters imported for number of neurons = ' + str(len(pulseData) - 1))

# Write the output file:

outfile = open(outfilename, 'w')

i = 1

while i <= number_PN:
	labels = ['title'] + parameters_PN

        dP = pulseData[i]
        
	for p in labels:
		if p == labels[0]:
			l = '"PN ' + str(i) + '"\n'
		elif p == labels[-1]:
			p_val = values_PN[p]
			l = '\t' + p + ':' + str(p_val) + ';\n'
                elif p == 'PulseDuration': 
                        p_val = dP[1]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'PulseStart':
                        p_val = dP[2]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'PulseEnd':
                        p_val = dP[3]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'tau_rise':
                        p_val = dP[4]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'tau_fall':
                        p_val = dP[5]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'PulseMax':
                        p_val = dP[6]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'PulseMin':
                        p_val = dP[7]
			l = '\t' + p + ':' + str(p_val) + ',\n'
		else:
			p_val = values_PN[p]
			l = '\t' + p + ':' + str(p_val) + ',\n'
		
		outfile.write(l)
	i += 1

j = 1
	
while j <= number_LN:
	labels = ['title'] + parameters_LN
        i = j + number_PN
        dP = pulseData[i]
	for p in labels:
		if p == labels[0]:
			l = '"LN ' + str(j + number_PN) + '"\n'
		elif p == labels[-1]:
			p_val = values_LN[p]
			l = '\t' + p + ':' + str(p_val) + ';\n'
                elif p == 'PulseDuration': 
                        p_val = dP[1]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'PulseStart':
                        p_val = dP[2]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'PulseEnd':
                        p_val = dP[3]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'tau_rise':
                        p_val = dP[4]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'tau_fall':
                        p_val = dP[5]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'PulseMax':
                        p_val = dP[6]
			l = '\t' + p + ':' + str(p_val) + ',\n'
                elif p == 'PulseMin':
                        p_val = dP[7]
			l = '\t' + p + ':' + str(p_val) + ',\n'
		else:
                        p_val = values_LN[p]
			l = '\t' + p + ':' + str(p_val) + ',\n'
		
		outfile.write(l)
	j += 1

		
outfile.close()	


		
"""
    'PulseDuration' = '',
    'PulseStart' = '', 
    'PulseEnd' = '',
    'tau_rise' = '',
    'tau_fall' = '',
    'PulseMax' = '', 
    'PulseMin' = '',
    'I_PeriodicPulse' = '0',
"""
