# -*- coding: utf-8 -*-
"""
Copyright (c) 2009 Carsten Niehaus (cniehaus@kde.org).
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  a. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.
  b. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  c. Neither the name of the Enthought nor the names of its contributors
     may be used to endorse or promote products derived from this software
     without specific prior written permission.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.
"""

class PredatorPreyCalculator(object):
    """
    a = Natural Growing Rate of prey, when there are no predators
    b = Natural Dying Rate of prey(due to predation)
    c = Natural Dying Rate of Predators, when there is no prey
    p = Reproduction rate of Predators (after eating preys, how
        many caught rabbits let create on new predator)
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




