#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Based on code written by AMit Kumar (Oct 01, 2006)

a = Intrinsic rate of Prey Population Increase ;
b = Predation Rate Coefficient ;
p = Reproduction rate of Predators ( after eating preys );
c = Death Rate of Predators ;
Prey0 = Initial Prey Population ;
Predator0 = Initial Predator Population;
dt = Time Step;
"""

class PredatorPreyCalculator(object):
    def __init__(self):
        self.a=1.0
        self.b=0.2
        self.p=0.04
        self.c=0.5
        self.Prey0=5
        self.Predator0=2
        self.dt=0.01
        self.tstart=0.0
        self.iterations=5000
    
    def setA(self, a):
        self.a = a
        
    def setB(self, b):
        self.b = b
        
    def setC(self, c):
        self.c = c

    def setP(self, p):
        self.p = p

    def setPrey0(self, p):
        self.Prey0 = p

    def setPredator0(self, p):
        self.Predator0 = p

    def dx(self, x,y):
        return self.a*x-self.b*x*y

    def dy(self, x,y):
        return self.p*x*y-self.c*y
        
    def calculate(self):
        r_string = "R, "
        b_string = "B, "
        i = 0
        x = self.Prey0
        y = self.Predator0
        t = self.tstart
    
        while i < self.iterations:
            t = i * self.dt
            xnew = x + self.dx(x,y) * self.dt
            ynew = y + self.dy(x,y) * self.dt
            
            x = xnew
            y = ynew
            
            r_string += str(x)
            r_string += ", "
            b_string += str(y)
            b_string += ", "
            i += 1
        
        print(r_string)
        print(b_string)
        
foo = PredatorPreyCalculator()
foo.calculate()






