#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009 Carsten Niehaus. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

def allel_frequenz( a, b ):
    p = (a+b)/100*a/10000 
    q = 1-p
    
    print(a/100*b)
    print(q)
    
    pp = p**2
    pq2 = 2*p*q
    qq = q**2
    
    return pp, pq2, qq

class Tier(object):
    number = 0
    
    def __init__(self):
        Tier.number += 1
        
    def __del__(self):
        Tier.number -= 1
        
    def anzahl(self):
        print Tier.number
        
class Laus(Tier):
    def __init__(self):
        Tier.__init__(self)
    
class Bug(Tier):
    def __init__(self):
        Tier.__init__(self)

    
l1 = Laus()
l1.anzahl()
l2 = Laus()
l1.anzahl()
l3 = Laus()
l1.anzahl()
l4 = Laus()
l1.anzahl()

b1 = Bug()
b1.anzahl()