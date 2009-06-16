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

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import re, datetime, calendar 

class Halbjahr(object):
    def __init__(self):
        print "Halbjahr"
        self.jahr = 2009
        self.haelfte = 1
        self.anfang = QDate (2009, 1,1)
        self.anfang = QDate (2009, 6,1)


class Klasse(object):
    def __init__(self, bezeichnung = ""):
        print "Klasse"
        self.schuelerListe = []
        self.bezeichnung = bezeichnung
        self.klassenlehrer = ""
        self.planung = Unterrichtsplanung()
        
        # zum Testen ein paar Testdaten laden
        self.debugData()
    
    def debugData(self):
        self.schuelerListe.append( Schueler( "Jens",  "Test",  "m"))
        self.schuelerListe.append( Schueler( "Michael",  "Test2",  "m"))
        self.schuelerListe.append( Schueler( "Marion",  "Test3",  "w"))
        
        self.klassenlehrer = "SAE"

		
class Schueler(object):
    def __init__(self,  vorname,  name,  geschlecht):
        print "Schüler"
        self.weiblich = None
        if geschlecht is "w":
            self.weiblich = True
        else:
            self.weiblich = False
            
        self.name = name
        self.vorname = vorname
        
class Unterrichtsplanung(object):
    def __init__(self):
        print "Unterrichtsplanung"
        self.termine = []
        self.debugData()
        
        #Der Unterricht soll Montags und Freitags sein
        self.tage = [1, 5]
        
    def debugData(self):
        print "debugData in Unterrichtsplanung"
        t1 = Termin( datetime.date(2009,  2, 5) )
        t2 = Termin( datetime.date(2009,  2, 6) )
        t3 = Termin( datetime.date(2009,  4, 7) )
        t4 = Termin( datetime.date(2009,  5, 12))
        
        p1 = datetime.date(2009,  5, 12)
        p2 = datetime.date(2009,  5, 13)
        #datetime.timedelta(p1, p2)
        
        self.termine = [t1, t2, t3, t4]

class Termin(object):
    def __init__(self,  date = None):
        print "Termin"
        self.raum = ""
        self.fach = ""
        self.datum = None
        if date is not None:
            self.setDate( date )
    
    def __sub__(self,  date):
        """Ich muss den Operator überladen, damit ich Termine 
        miteinander verrechnen kann."""
        return self.datum - date.datum

    def setDate(self,  datum):
        print "foo"
        print "setze Datum auf %s" % str(datum)
        self.datum = datum
        
