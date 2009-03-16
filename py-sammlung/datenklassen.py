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

class Medium:
	def __init__(self, typ, referenznummer = ""):
		self.typ = typ
		self.referenznummer = referenznummer
	
	def debugInfo(self):
		return "Medium: %s (Typ %s)" % (self.referenznummer, self.typ)

class Objekttraeger(Medium):
	def __init__(self, typ, name, bezeichnung, beschreibung, referenznummer = 0):
		print "def Objekttraeger.__init__"
		Medium.__init__(self,typ, referenznummer)
		self.setData(name, bezeichnung, beschreibung)

	def setData( self, name, bezeichnung, beschreibung ):
		print "Objekttraeger.setData()"
        	self.data = { "name" : name,
			"bezeichnung" : bezeichnung,
			"beschreibung" : beschreibung
		}
		self.debugInfo()

	def debugInfo(self):
		print "=== debug: %s == %s ==  %s ==  %s == %s" % (self.typ , self.data["name"], self.data["beschreibung"], 
			self.data["bezeichnung"], self.referenznummer )

class DVD(Medium):
	def setData( self, klasse, nutzername, passwort, uid ):
        	self.data = {"klasse" : klasse, 
			"nutzername" : nutzername, 
			"passwort" : passwort, 
			"uid" : uid  
		}

	def debugInfo(self):
		return "DVD/CD: %s aus der \t %s." % (self.name, self.data["klasse"])

class Klasse:
    def __init__(self, name, lehrer):
	self.data = { "name" : name, 
		"lehrer" : lehrer 
	}
