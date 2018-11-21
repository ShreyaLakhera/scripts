import sys
import networkx as nx

# Initialize all information and inputs

nNeuron = 8                       			# Number of neurons

AdjacencyMatrix = [[0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0],
 		   [0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 1, 0, 1, 0, 0, 0, 0],
		   [0, 1, 0, 1, 1, 0, 0, 0]]		# Row(h) number is the post-neuron, and column(v) number is the pre-neuron

labels = ['title', 'dxdt', 'g1', 'gsyn', 'esyn', 'pre', 'post']

Values = {'dxdt' : '1',
  	  'g1' : '0',
  	  'gsyn' : '0.35',
	  'esyn' : '0'}

pathname = '/home/shreya/work/Adi_AntennalLobe_LN/SN_HH/';
filename = 'ssets_8_ACH.isf'

# Make a graph using the above information, Neurons -> nodes, Synapses -> edges

G = nx.DiGraph()

for v in range(1, nNeuron + 1):
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

print('Number of neurons = ' + str(nNeuron))
print('Number of synapses = ' + str(len(Edges)))

print Values

print Nodes
print Edges

# Write to output file:

outfile = open(pathname + filename, 'w')

for e in Edges:

	pre = e[0] - 1
	post = e[1] - 1
	
	idSynapse = Edges.index(e)
	
	for x in labels:
		if x == 'title':
			l = '"S ' + str(idSynapse) + '"\n'
		elif x == 'pre':
			l = '\tpre:' + str(pre) + ',\n'
		elif x == 'post':
			l = '\tpost:' + str(post) + ';\n'
		else:
			p_val = Values[x]
			l = '\t' + x + ':' + p_val + ',\n'

		outfile.write(l)


outfile.close()


#AdjacencyMatrix = [[0, 0, 1, 0, 0, 0, 0, 0],
#		   [1, 0, 1, 0, 0, 0, 0, 0],
#		   [0, 0, 0, 0, 0, 1, 0, 0],
#		   [1, 0, 0, 0, 1, 1, 0, 0],
#		   [0, 0, 1, 0, 0, 0, 0, 0],
#		   [0, 1, 0, 0, 1, 0, 0, 0],
#		   [0, 1, 0, 1, 0, 0, 0, 0],
#		   [0, 1, 0, 1, 1, 0, 0, 0]]		# Row(h) number is the post-neuron, and column(v) number is the pre-neuron

#AdjacencyMatrix = [[0, 0, 0, 0, 0, 0, 0, 0],
#		   [0, 0, 0, 0, 0, 0, 0, 0],
#		   [0, 0, 0, 0, 0, 0, 0, 0],
#		   [0, 0, 0, 0, 0, 0, 0, 0],
#		   [0, 0, 0, 0, 0, 0, 0, 0],
#		   [0, 0, 0, 0, 0, 0, 0, 0],
#		   [0, 1, 0, 1, 0, 0, 0, 0],
#		   [0, 1, 0, 1, 1, 0, 0, 0]]		# Row(h) number is the post-neuron, and column(v) number is the pre-neuron
