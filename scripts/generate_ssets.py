import sys
import networkx as nx

# Initialize all information and inputs

gNeuron = [5, 5]                       	# Number of neurons per color group
nNeuron = sum(gNeuron)

AdjacencyMatrix = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
		   [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
		   [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
		   [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
		   [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
		   [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
		   [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

labels = ['title', 'dxdt', 'g1', 'esyn', 'pre', 'post']

Values = {'dxdt' : '1',
  	  'g1' : '5',
	  'esyn' : '-40'}

pathname = '/home/shreya/work/Adi_AntennalLobe_LN/10N_50S/';
filename = 'ssets_10_40esyn5g1.isf'

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
			l = '"synapse ' + str(idSynapse) + '"\n'
		elif x == 'pre':
			l = '\tpre:' + str(pre) + ',\n'
		elif x == 'post':
			l = '\tpost:' + str(post) + ';\n'
		else:
			p_val = Values[x]
			l = '\t' + x + ':' + p_val + ',\n'

		outfile.write(l)


outfile.close()
