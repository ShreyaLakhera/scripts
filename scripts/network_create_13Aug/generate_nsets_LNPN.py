import sys

# Initialize all input required (Number of neurons, which parameters to write, the file to write it in, the default values of these parameters)

outfilename = sys.argv[1]			# Enter the address to write nsets file to, eg: /address/nsets.isf
number_PN = int(sys.argv[2])			# Enter the number of PNs
number_LN = int(sys.argv[3])			# Enter the number of LNs
I_ext_PN = float(sys.argv[4])			# The external current that you want to add in all PNs
I_ext_LN = float(sys.argv[5])			# The external current that you want to add in all LNs

parameters_LN = ['dxdt', 'v', 'mk', 'mca', 'hca', 'nk', 'CA_DRIVE', 'I_KCA', 'I_CA', 'I_K_LN', 'iext']
parameters_PN = ['dxdt', 'v', 'm', 'h', 'n', 'ma', 'ha', 'I_NA', 'I_K', 'I_A', 'I_LEAK', 'I_KLEAK', 'I_ext', 'last_spike']

values_LN = {'dxdt' : '7',
  	  'v' : '-30',
	  'mk' : '0',
	  'mca' : '0',
	  'hca' : '0',
	  'nk' : '0',
	  'CA_DRIVE' : '0.00024',
	  'I_KCA' : '0',
	  'I_CA' : '0',
	  'I_K_LN' : '0',
	  'iext' : I_ext_LN}

values_PN = {'dxdt' : '6',
  	  'v' : '-30',
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
	  'I_ext' : I_ext_PN,
	  'last_spike' : -10}


# Write the output file:

outfile = open(outfilename, 'w')

i = 1

while i <= number_PN:
	labels = ['title'] + parameters_PN

	for p in labels:
		if p == labels[0]:
			l = '"PN ' + str(i) + '"\n'
		elif p == labels[-1]:
			p_val = values_PN[p]
			l = '\t' + p + ':' + str(p_val) + ';\n'
		else:
			p_val = values_PN[p]
			l = '\t' + p + ':' + str(p_val) + ',\n'
		
		outfile.write(l)
	i += 1

j = 1
	
while j <= number_LN:
	labels = ['title'] + parameters_LN

	for p in labels:
		if p == labels[0]:
			l = '"LN ' + str(j + number_PN) + '"\n'
		elif p == labels[-1]:
			p_val = values_LN[p]
			l = '\t' + p + ':' + str(p_val) + ';\n'
		else:
			p_val = values_LN[p]
			l = '\t' + p + ':' + str(p_val) + ',\n'
		
		outfile.write(l)
	j += 1

		
outfile.close()	


		

