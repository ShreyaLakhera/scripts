import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal
"""
Script to plot the average of some voltage values in the network output file.
Uses the format nxv as the label for voltage reading (where x is an integer)
Use ranges of values of x, say if you want to include neurons 3 to 10, 15 to 23 and 45,99 write: 3*10,15*23,45,99
"""

# Collect the voltages

infilename = sys.argv[1] 		# The csv file in which it reads the ouutput voltage readings
plot_these1 = sys.argv[2].split(',')	# Give the range or number separated by * and commas
outfig = sys.argv[3]                    # Write the name of outfile to save the plot
t_start = float(sys.argv[4])
t_end = float(sys.argv[5])

plot_these = []
for n in plot_these1:
	if '*' in n:
		nr = n.split('*')
		ns = range(int(nr[0]), int(nr[1])+1)
		plot_these += ns
	else:
		plot_these += [int(n)]

print('\nThese are all the values to plot ---\n')
print(plot_these)

ts = []
data = []
data_pr = []
volt_ids = []

infile = open(infilename, 'r')

ln = 1
for line in infile:
	if 'time' in line:
		labels = line.strip('\n').split(',')
		print('\nThese are all the labels ---\n')
		#print(labels)

		i = 0
		for x in labels:
			if (x[0] == 'n') and (x[-1] == 'v') and (int(x[1:-1]) in plot_these):
				volt_ids.append(i)
			i +=1		
		print('\nThese indices from above list are being averaged ---\n')
		print(volt_ids)

	elif ('time' not in line) and (line != '\n'):
		l1 = line.strip('\n').split(',')
		l = [float(l1[j]) for j in volt_ids]
		l_avg = np.mean(l)
		data.append(l_avg)
                t = float(l1[0])
                if (t > t_start) and (t < t_end):
                        data_pr.append(l_avg)
		ts.append(float(l1[0]))
	ln += 1

infile.close()

print('Size of data --- \n' + str(np.size(data)))

print('Size of data for fft --- \n' + str(np.size(data_pr)))
#print(data_pr[0:10])

#data_p = np.abs(fft(data_pr)//2)

#data_p = np.abs(fft(data_pr))

#data_fft = np.array(data_pr)
#data_p = np.fft.fft(data_fft)
#n = data_fft.size
#dt = 0.01
#freq = np.fft.fftfreq(n,d=dt)

#freq_s = 100000**freq

#print(freq[1:20])

freq, pxx_spec = signal.periodogram(np.array(data_pr), 100000, scaling='spectrum')

freq1 = []
pspec1 = []

for x in freq:
    if (x > 0) and (x < 100):
        y = pxx_spec[np.ndarray.tolist(freq).index(x)]
        pspec1.append(y)
        freq1.append(x)

plt.figure()
plt.plot(freq, np.sqrt(pxx_spec))
plt.title('Power Spectrum of averaged PN activity')
plt.show()



"""
freqs, pxx_spec = signal.periodogram(np.array(data_pr), 10e5, 'flattop', scaling='spectrum' )

plt.figure()
plt.semilogy(freqs, np.sqrt(pxx_spec)) 
plt.title('PSD')
plt.ylim(1e-4, 1e1)
plt.ylabel('Power')
plt.xlabel('Frequency')
#plt.savefig(outfig)

plt.figure(2)
plt.plot(freq,data_p.real, '-')
plt.title('plot with freq')
plt.ylabel('Power')
plt.xlabel('Freq')
plt.savefig(outfig)
"""

plt.show()
