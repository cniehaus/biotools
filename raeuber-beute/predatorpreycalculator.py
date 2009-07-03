# -*- coding: utf-8 -*-
"""
Based on code written by Amit Kumar (Oct 01, 2006)

The code was ported from Amit Kumars JAVA-code to Python 2.6 
by Carsten Niehaus (cniehaus@kde.org) in 2009 and enhanced.

It is licenced under the GPL v2+.
"""

class PredatorPreyCalculator(object):
    """
    a = Intrinsic rate of Prey Population Increase ;
    b = Predation Rate Coefficient ;
    p = Reproduction rate of Predators ( after eating preys );
    c = Death Rate of Predators ;
    Prey0 = Initial Prey Population ;
    Predator0 = Initial Predator Population;
    dt = Time Step;
    """
    def __init__(self):
        self.a=1.0
        self.b=0.2
        self.c=0.5
        self.p=0.04
        self.Prey0=5
        self.Predator0=2
        self.dt=0.01
        self.tstart=0.0
        self.iterations=5000  
    
    def dx(self, x,y):
        return self.a*x-self.b*x*y

    def dy(self, x,y):
        return self.p*x*y-self.c*y
        
    def calculate(self):
        """
        This method calculates the number of predators and prey after each timestep.
        It returns two lists, one for prey, one of predator. An example would be:    
        ['Predator', 5.0300000000000002, 5.0602403599999999, 5.0907228235971242]
        ['Prey', 1.994, 1.9880419279999999, 1.9821257063605751 ]
        """
        r_string = ["Predator"]
        b_string = ["Prey"]
        
        i = 0
        x = self.Prey0
        y = self.Predator0
        t = self.tstart
    
        while i < self.iterations:
            t = i * self.dt
            
            #One way to integrate would be the Euler-Method,
            #but that would lead to a growth of both populations
            #as with each step the error would be quite big. The 
            #following four lines show the Eurler-integration for
            #educational puposes:
            
            #xnew = x + self.dx(x,y) * self.dt
            #ynew = y + self.dy(x,y) * self.dt
            #x = xnew
            #y = ynew
            
            #Using an Runga-Kutta 2nd order integrator, c.f.
            #http://mathworld.wolfram.com/Runge-KuttaMethod.html
            xk_1 = self.dx(x,y) * self.dt
            yk_1 = self.dy(x,y) * self.dt
            xk_2 = self.dt * self.dx(x+xk_1,y+yk_1)
            yk_2 = self.dt * self.dy(x+xk_1,y+yk_1)
            
            x = x + (xk_1 + xk_2)/2
            y = y + (yk_1 + yk_2)/2
            
            r_string.append(x)
            b_string.append(y)
            
            i += 1
        
        return r_string, b_string




