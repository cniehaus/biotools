#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_maindlg import Ui_MainDlg
import sys
import random

class MainDialog(QDialog, Ui_MainDlg):
	'''Hauptklasse fuer das Kassensystem'''
	def __init__(self, parent=None):
		print "moin moin"
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)
		self.labellist = []
		self.tierlist = []
		self.erstelleListe()
		self.feld_erstellen()
		self.stop.setEnabled(False)
		
		self.pix_k = QPixmap("./kaefer.jpg")
		self.pix_l = QPixmap("./laus.jpg")
		
		random.seed()
		
		self.aktuellesTier = "m"
			
		self.timer = QTimer( )
		
		self.connect( self.start, SIGNAL("clicked()"), self.starten )
		self.connect( self.stop, SIGNAL("clicked()"), self.stoppen )
		self.connect( self.timer, SIGNAL("timeout()"), self.zug )
		
	def zug(self):
		print "start"
		
		# Wer ist dran? L oder M
		
		
		
		#1: Zufallszahl erzeugen: eine für x, eine für y (x/y)
		
		x = random.randint(0, 5)+1
		y = random.randint(0, 5)+1
		
					
		z = (y-1)*6+x-1
		print z		
		ding = self.tierlist[z]
		
		#3: Was passiert nun
		
		self.statistik()
		
		if self.aktuellesTier == "l":
			self.aktuellesTier = "m"
			if not ding:
				self.tierlist[z] = Tier("l")
				return
			elif ding.symbol() == "l":
				# ein benachbartes Feld falls verfügbar
				# wird besetzt TODO
				return
			elif ding.symbol() == "m":
				# Die Laus wird gefressen
				return
			else:
				print "FEHLER !!! ALARM !!!"
				
		else:
			self.aktuellesTier = "l"
			if not ding:
				# Der Marienkaefer verhungert, nichts passiert
				return
			elif ding.symbol() == "l":
				# Aus der Laus wird ein Marienkaefer
				self.tierlist[z] = Tier("m")
				return
			elif ding.symbol() == "m":
				# Die Laus wird gefressen
				self.tierlist[z] = None
				return
			else:
				print "###################################"
				
		
		#4: machen
		#return self.feld()
		
		#x1, y = 0,0
		
	
	def stoppen(self):
		self.timer.stop()
		self.stop.setEnabled(False)
		self.start.setEnabled(True)
		print "Stop"
		
	def starten(self):
		self.timer.start(100)
		self.start.setEnabled(False)
		self.stop.setEnabled(True)
		print "Start"
		
	def zahlen(self):
		"""
		Diese Methode zaehlt die Teammitglieder und gibt die 
		Anzahl an Lauusen und Marienkaefern zurueck.
		"""
		l_c = 0
		m_c = 0
		for i in self.tierlist:
			if not i:
				continue
			if i.name == "l":
				l_c += 1
			elif i.name == "m":
				m_c += 1
		
		return l_c, m_c
	
	def statistik(self):
	#'''Diese Methode erzeugt eine Debug-Auskunft über
	#das akutelle Feld und setzt die Werte der LCD-Displays.'''
		print "Statistik"
				
		counter = 0
		output_string = ""
		
		for i in self.tierlist:
			if i:
				name = i.name
			
				#self.labellist[counter].setPixmap(self.pix_k)
				self.labellist[counter].setText(name)
				output_string += i.name
			else:
				output_string += "-"
			counter += 1
			
			# nun wird überprüft, ob die Zahl glatt durch
			# 6 teilbar ist.
			if counter % 6 == 0:
				output_string += "\n"
		print output_string
		
		
		l_c, m_c = self.zahlen()
		
		self.lcdNumber_l.display(l_c)
		self.lcdNumber_m.display(m_c)
		
	
	def close(self):
		print "Close"
	
		
	def feld_erstellen(self):
		print "feld_erstellen"
				
		count = 0
		for i in self.tierlist:
			random.seed()
			x = random.randint(0, 2)
			if x == 0:
				self.tierlist[count] = Tier("m")
			elif x == 1:
				self.tierlist[count] = Tier("l")
			else:
				self.tierlist[count] = None
				
			count += 1
		
		
	def erstelleListe(self):
		self.labellist.append(self.l1)
		self.labellist.append(self.l2)
		self.labellist.append(self.l3)
		self.labellist.append(self.l4)
		self.labellist.append(self.l5)
		self.labellist.append(self.l6)
		self.labellist.append(self.l7)
		self.labellist.append(self.l8)
		self.labellist.append(self.l9)
		self.labellist.append(self.l10)
		self.labellist.append(self.l11)
		self.labellist.append(self.l12)
		self.labellist.append(self.l13)
		self.labellist.append(self.l14)
		self.labellist.append(self.l15)
		self.labellist.append(self.l16)
		self.labellist.append(self.l17)
		self.labellist.append(self.l18)
		self.labellist.append(self.l19)
		self.labellist.append(self.l20)
		self.labellist.append(self.l21)
		self.labellist.append(self.l22)
		self.labellist.append(self.l23)
		self.labellist.append(self.l24)
		self.labellist.append(self.l25)
		self.labellist.append(self.l26)
		self.labellist.append(self.l27)
		self.labellist.append(self.l28)
		self.labellist.append(self.l29)
		self.labellist.append(self.l30)
		self.labellist.append(self.l31)
		self.labellist.append(self.l32)
		self.labellist.append(self.l33)
		self.labellist.append(self.l34)
		self.labellist.append(self.l35)
		self.labellist.append(self.l36)
				
		for i in range(0, 36):
			self.tierlist.insert(i, None)
	
class Tier(object):
	def __init__ (self, typ):
		self.name = typ

	def symbol(self):
		return self.name


if __name__ == "__main__":
	import sys

	app = QApplication(sys.argv)
	form = MainDialog()
	form.show()
	app.exec_()
