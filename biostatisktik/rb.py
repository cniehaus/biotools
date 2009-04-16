#!/usr/bin/python
import random
import time
import csv
import sys
#from PyQt4 import QtCore, QtGui
#
#from beute_ui import Ui_Beute
#
#class MyForm(QtGui.QMainWindow):
#    def __init__(self, parent=None):
#        QtGui.QWidget.__init__(self, parent)
#        self.ui = Ui_Beute()
#        self.ui.setupUi(self)
#

class Spielfeld:
	def __init__(self):
		print "Starte das Spielfeld"
		# des Feld wird hier erstmals initialisiert
		self.feld = [ 
			["", "b", "b", "", "b", "b"], 
			["m", "b", "b", "m", "b", "b"], 
			["m", "", "b", "m", "b", "b"], 
			["m", "b", "", "m", "b", "b"], 
			["m", "b", "b", "m", "", "b"], 
			["", "", "b", "m", "b", "b"], 
		]

	def showField(self):
		for f in self.feld:
			print f

	def count(self):
		b = 0
		m = 0
		for f in self.feld:
			b += f.count('b')
			m += f.count('m')

		print "Blattlaus   : %i" % b
		print "Marienkaefer: %i" % m
		
		return b,m
	
	def setAnimal(self, prey, x, y):
		print "%s : %s" % ( x , y )
		f = self.feld[y-1]
		p = f[x-1]
		# Prey ( == b )
		print p
		if prey:
			if p == "":
				# Das leere Feld wird besetzt
				f[x-1] = "b"
			elif p == "b":
				# Ein leeres und angrenzendes Feld wird besetzt
				return
			else:
				# Die Laus wird gefressen
				return
		# Predator ( == m)
		else:
			if p == "":
				# Der Marienkaefer verhungert, nichts passiert
				return
			elif p == "b":
				# Aus der Laus wird ein Marienkaefer
				f[x-1] = "m"
			else:
				# Der Kaefer verhungert
				f[x-1] = "" 
feld = Spielfeld()

count = 0 

bb = []
mm = []

while count < 400:
	time.sleep(0.2)
	random.seed()
	x = random.randint(0,5)+1
	y = random.randint(0,5)+1
	count += 1
	if count%2:
		feld.setAnimal( 0, x, y)
	else:
		feld.setAnimal( 1, x, y)
	feld.showField()
	bb_,mm_ = feld.count()
	bb.append(bb_)
	mm.append(mm_)

writer = csv.writer(open("results.csv", "wb"))
writer.writerow( bb )
writer.writerow( mm )
