import sys
import networkx as nx
import random
import numpy as np

"""
This script will generate an sset.isf file for a given number of neurons, type of neurons, and given connection probabilities. 
This draft has properties for only 2 kind of neurons, and specific synapses between them, but this can be further modified. 

Example: If we want to create a network of 2 types of neurons, with 10 neurons in the first group, and 20 neurons in the second group, with connection probabilities as follows:

from -- g1	g2
to
g1	a	b
g2	c	d

Run the script as:
python /addreiss/script_name.py /address/output_filename 2 10,20 a,b,c,d p,q,r,s

conductances
    to PN   to LN
fPN p       q
fLN r       s

This will create an Adjacency matrix of the desired network.
Next, the script writes the synapses to a ssets file. The first group is taken as group of PNs and second is taken as LNs. 
Connections from LN to (LN and PN) are taken as GABA inhibitory connections (values of gsyn and esyn are different in case of LN-LN and LN to PN)
Connections from PN to LN are nACH excitatory connections
As we do not want PN to PN connections, ideally d = 0. But right now, PN to PN is written as nACH excitatory connections, with different values of gsyn and esyn
"""

outfilename = sys.argv[1]
nTypeNeurons = int(sys.argv[2])				# Number of types/groups of neurons
nNeurons = [int(x) for x in sys.argv[3].split(',')]	# Number of neurons in each group
p = [float(x) for x in sys.argv[4].split(',')]		# Connection probabilities
g_all = [float(x) for x in sys.argv[5].split(',')]	# Conductances
#print(p)

# Make a list of these connections:

total_neurons = sum(nNeurons)
allNeuronInfo = range(nTypeNeurons)

probs = np.zeros((nTypeNeurons, nTypeNeurons)) 		# List of probabilities of connections to and from different groups

prob_id = 0
for x in p:
	np.put(probs, prob_id, x)
	prob_id += 1

print(probs)

groupNeuron = []
nN = 0
for tN in range(nTypeNeurons):
	neurons = range(nN, nN + nNeurons[tN])
	groupNeuron.append(neurons)
	nN = nN + nNeurons[tN]

print(groupNeuron)

for tN in range(nTypeNeurons):
	allNeuronInfo[tN] = []
	nN = 0
	for x in groupNeuron[tN]:
		allNeuronInfo[tN].append([x, tN])
		neuron_neighbors = []
		for tN2 in range(nTypeNeurons):
			choose_from = list(groupNeuron[tN2])
			#print(choose_from)
			#print(x)
			if (tN2 == tN):
				if x in choose_from:
					choose_from.remove(x)
			#print(choose_from)
			prob_12 = probs[tN][tN2]
		 	nNeighbors = int(round(prob_12 * (len(groupNeuron[tN2]))))
			neighbors = random.sample(choose_from, nNeighbors)
			neuron_neighbors += neighbors
		allNeuronInfo[tN][nN].append(neuron_neighbors)
		nN += 1


# Create Adjacency matrix from the list of neuron neighbors

AM = np.zeros((total_neurons, total_neurons))

for tN in range(len(allNeuronInfo)):
	for nN in allNeuronInfo[tN]:
		preNeuron_id = nN[0]
		neighbors = nN[2] 
		for nb in neighbors:
			AM_id = preNeuron_id + (total_neurons - 1) + nb
			#np.put(AM, AM_id, 1)
			AM[preNeuron_id][nb] = 1


# Initialize all information and inputs

AdjacencyMatrix = np.ndarray.tolist(AM)

labels = ['title', 'dxdt', 'g1', 'gsyn', 'esyn', 'pre', 'post']

Values_gaba_LNs = {	'dxdt' : '1',
  	  		'g1' : '0',
			'gsyn' : str(g_all[3]),
		  	'esyn' : '-40'}

Values_gaba_LNPN = {	'dxdt' : '1',
  	  		'g1' : '0',
                        'gsyn' : str(g_all[2]),
		  	'esyn' : '-40'}

Values_ACH_PNs = {	'dxdt' : '1',
  	  		'g1' : '0',
			'gsyn' : str(g_all[0]),
		  	'esyn' : '0'}

Values_ACH_PNLN = {	'dxdt' : '1',
  	  		'g1' : '0',
			'gsyn' : str(g_all[1]),
		  	'esyn' : '0'}


# Make a graph using the above information, Neurons -> nodes, Synapses -> edges

G = nx.DiGraph()

for v in range(1, total_neurons + 1):
	G.add_node(v)

y = 1
for i in AdjacencyMatrix:
	x = 1 
	for j in i:
		if j == 1:
			G.add_edge(x,y)
		x += 1
	y += 1

Nodes = G.nodes()
Edges = G.edges()	

print('Number of neurons = ' + str(total_neurons))
print('Number of synapses = ' + str(len(Edges)))


# Write to output file:

outfile = open(outfilename, 'w')
nS_nACH = 0
nS_GABA = 0

for e in Edges:

	pre = e[0] - 1
	post = e[1] - 1

	type_pre = 0
	type_post = 0

	gN = groupNeuron
	
	for y in range(len(gN)):
	     	if pre in gN[y]:
        	     	type_pre = y
	             	break

	for y in range(len(gN)):
	     	if post in gN[y]:
        	     	type_post = y
	             	break

	if (type_pre == 0):
		nS_nACH += 1
	elif (type_pre == 1):
		nS_GABA += 1
	
	idSynapse = Edges.index(e)

	for x in labels:
		if x == 'title':
			l = '"synapse ' + str(idSynapse) + '"\n'
		elif x == 'pre':
			l = '\tpre:' + str(pre) + ',\n'
		elif x == 'post':
			l = '\tpost:' + str(post) + ';\n'
		else:
			if (type_pre == 0): 
				if (type_post == 0):
					p_val = Values_ACH_PNs[x]
				elif (type_post == 1):
					p_val = Values_ACH_PNLN[x]
			if (type_pre == 1):
				if (type_post == 0):
					p_val = Values_gaba_LNPN[x]
				elif (type_post == 1):
					p_val = Values_gaba_LNs[x]

			l = '\t' + x + ':' + p_val + ',\n'

		outfile.write(l)


outfile.close()		

print('nACH synapses written = ' + str(nS_nACH))
print('GABA synapses written = ' + str(nS_GABA))
