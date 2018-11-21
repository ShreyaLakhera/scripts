import numpy as np
import matplotlib.pyplot as plt
import sys

low1 = float(sys.argv[1])
height1 = float(sys.argv[2])
low2 = float(sys.argv[3])
height2 = float(sys.argv[4])
low3 = float(sys.argv[5])
height3 = float(sys.argv[6])

mu = 45
width = 30
sig1 = np.sqrt((-1/(2*np.log(low1/height1)))*((width/2)**2))
sig2 = np.sqrt((-1/(2*np.log(low2/height2)))*((width/2)**2))
sig3 = np.sqrt((-1/(2*np.log(low3/height3)))*((width/2)**2))

print(mu)
print(sig1)

x = range(0,90)
y1 = []
y2 = []
y3 = []

for i in x:
    j = height1*np.exp((-1/(2*(sig1**2)))*((i - mu)**2))
    if (j<low1):
        j = 0
    y1.append(j)


i=0
j=0

for i in x:
    j = height2*np.exp((-1/(2*(sig2**2)))*((i - mu)**2))
    if (j<low2):
        j = 0
    y2.append(j)

i=0
j=0


for i in x:
    j = height3*np.exp((-1/(2*(sig3**2)))*((i - mu)**2))
    if (j<low3):
        j = 0
    y3.append(j)


print(y3)

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.ylabel('Amplitude of external input current')
plt.xlabel('Neuron Index')
plt.show()
