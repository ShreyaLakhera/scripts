import math

def f(x):
	y = (1 - math.sin(x))/(math.exp(x) + 1)
	return y

def rk4(x,d):
	k1 = f(x)*d
	k2 = f(x + (k1/2))*d
	k3 = f(x + (k2/2))*d
	k4 = f(x + k3)*d
	y = x + ((k1/6)+(k2/3)+(k3/3)+(k4/6))
	return y

x = 0
t = 0

while x < 0.99:
	x = rk4(x, 0.1)
	t = t + 0.1
	print(str(t) + '    ' + str(x))

print('\n\n\n\n\n\n\n')


print(t)
print(x)
