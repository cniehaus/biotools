#!/usr/bin/python
import random
import time
import csv

class Spielfeld:
	def __init__ (self):
		self.feld = []
	def start (self):
		self.feld = [
			["m", "b", "m", "b", "m", ""],
			["", "b", "b", "m", "b", "b"],
			["b", "b", "m", "b", "", "m"],
			["b", "", "b", "b", "m", "b"],
			["", "m", "b", "", "m", "b"],
			["", "m", "b", "b", "m", "b"],
		]
	def setze (self, typ, x, y):
		#print typ
		#print position
		feld2 = self.feld[x]
		feld2[y] = typ
		self.showField()
	def showField(self):
		print "#######################"
		for f in self.feld:
			print f
		print "#######################"
		
feld = Spielfeld ()
feld.start ()

count = 0
while count < 500:
	random.seed()
	x = random.randint(0,5)
	y = random.randint(0,5)
	count += 1
	# x = random.randint (0,5)
	# print "Der Wert von x ist %i" % x
	feld.setze ("b", x, y)
	# count += 1


# for feld in ZeigeFeld:
	# self.ZeigeFeld
	# print feld