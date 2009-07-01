#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Based on code written by AMit Kumar (Oct 01, 2006)

Intrinsic rate of Prey Population Increase ;
b = Predation Rate Coefficient ;
p = Reproduction rate of Predators ( after eating preys );
c = Death Rate of Predators ;
Prey0 = Initial Prey Population ;
Predator0 = Initial Predator Population;
dt = Time Step;
"""

a=1.0
b=0.2
p=0.04
c=0.5
Prey0=5
Predator0=2
dt=0.01
tstart=0.0
iterations=5000

x = Prey0
y = Predator0
t = tstart

i = 0

r_string = "R, "
b_string = "B, "

def dx(x,y):
	return a*x-b*x*y

def dy(x,y):
	return p*x*y-c*y

while i < iterations:
	#print "Durchlauf %d" % i
	t = i * dt
	xnew = x + dx(x,y) * dt
	ynew = y + dy(x,y) * dt

	x = xnew
	y = ynew

	r_string += str(x)
	r_string += ", "
	
	b_string += str(y)
	b_string += ", "
	
	i += 1

print(r_string)
print(b_string)
