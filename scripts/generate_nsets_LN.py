import sys

# Initialize all input required (Number of neurons, which parameters to write, the file to write it in, the default values of these parameters)

outfilename = sys.argv[1]			# Enter the full address, eg: /address/nsets.isf
number_N = int(sys.argv[2])			# Enter the number of neurons that you want to make the nsets file of, eg: 4

if sys.argv[3] == '1':
	parameters = ['dxdt', 'v', 'mk', 'mca', 'hca', 'nk', 'CA_DRIVE', 'I_KCA', 'I_CA', 'I_K_LN', 'iext']
else:
	parameters = sys.argv[3].split(',')	# Enter the variables that you want in that order, eg: dxdt,m,n,h   Put '1' to put default variables as in the parameter list in if condition. 

I_ext = float(sys.argv[4])			# The external current that you want to add in all neurons

values = {'dxdt' : '7',
  	  'v' : '-30',
	  'mk' : '0',
	  'mca' : '0',
	  'hca' : '0',
	  'nk' : '0',
	  'CA_DRIVE' : '0.00024',
	  'I_KCA' : '0',
	  'I_CA' : '0',
	  'I_K_LN' : '0',
	  'iext' : I_ext}


# Write the output file:

outfile = open(outfilename, 'w')
i = 1

while i <= number_N:
	labels = ['title'] + parameters

	for p in labels:
		if p == labels[0]:
			l = '"LN ' + str(i) + '"\n'
		elif p == labels[-1]:
			p_val = values[p]
			l = '\t' + p + ':' + str(p_val) + ';\n'
		else:
			p_val = values[p]
			l = '\t' + p + ':' + str(p_val) + ',\n'
		
		outfile.write(l)
	i += 1
		
		
outfile.close()	
