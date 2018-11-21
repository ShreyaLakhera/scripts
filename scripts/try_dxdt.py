import sys
import matplotlib.pyplot as plt
import numpy as np
import math

def f(x, h1, h2):
	T = 0.5*h1*h2
	y = (10*(1 - x)*T) - (0.2*x) 
	return y

def rk4(x,d):
	k1 = f(x)*d
	k2 = f(x + (k1/2))*d
	k3 = f(x + (k2/2))*d
	k4 = f(x + k3)*d
	y = x + ((k1/6)+(k2/3)+(k3/3)+(k4/6))
	return y

n = 1000		# Number of iterations
x = 0			# Initial condition x(0)
t = 0			# Start from time = 0
dt = 0.01 		# Time step

out_t = []
out_x = []

i = 1
while i < n:
	x = rk4(x, dt)
	t = t + dt
	out_x.append(x)
	out_t.append(t)
	i += 1

plt.plot(out_t,out_x, '.k')
plt.show()
