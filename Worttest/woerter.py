#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2008 Carsten Niehaus. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

import math

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_maindlg import Ui_MainDlg 
from ui_wortdialog import Ui_WortDialog 

class AufdeckenDialog(QDialog, Ui_WortDialog):
'''Dieser Dialog zeigt die Wörter der aktuellen Kategorie an, 
damit die Schüler diese mit ihrem Ergebnis vergleichen können'''

    def __init__(self, parent=None, liste = []):
        super(AufdeckenDialog, self).__init__(parent)
        self.setupUi(self)
	self.liste = liste
	self.fill()

    def fill(self):
	'''Das QTableWidget erhält nun die Wörter'''
	x = 0
	y = 0
	self.tableWidget.setColumnCount( 4 )
	# Berechnen, wie viele Zeilen benötigt werden.
	self.tableWidget.setRowCount( math.ceil ( len(self.liste) / 4.0 ) )
	
	for w in self.liste:
		#print "Setze %s auf %i / %i" % ( w, x, y )
		text = self.liste.index( w ) + 1 
		i = QTableWidgetItem( "%i: %s" % (text, w) )
		self.tableWidget.setItem( y, x, i )
		x += 1
		if x > 3:
			y += 1
			x = 0

	# optimale Breite
	self.tableWidget.resizeColumnsToContents()

class MainDialog(QDialog, Ui_MainDlg):
'''Hauptdialog'''

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

	self.loadLists()

	self.timer = QTimer()
	self.counter = 0
	self.interval = 1000
	self.running = False
	self.liste = []

	self.connect(self.button, SIGNAL("clicked()"), self.start )
	self.connect(self.aufdecken, SIGNAL("clicked()"), self.begriffeAufdecken )
	QObject.connect(self.timer, SIGNAL("timeout()"), self.timeout )

    def start(self):
	if not self.running:
		self.button.setText( "&Stop" )
		self.interval = self.interval_spinbox.value()
		self.running = True
		self.counter = 0
		self.laden()
		self.timer.start(self.interval)
	else:
		self.button.setText( "&Start" )
		self.timer.stop()
		self.running = False

    def laden(self):
	'''Verbereitung der Daten'''
	katalogname = self.combo.currentText()
	print "Lade Katalog %s" % katalogname

	if katalogname == "Einsilbig 1":
		self.liste = self.einsilbig1	
	if katalogname == "Einsilbig 2":
		self.liste = self.einsilbig2	
	elif katalogname == "Zweisilbig":
		self.liste = self.zweisilbig	
	elif katalogname == "Mehrsilbig 1":
		self.liste = self.mehrsilbig1	
	elif katalogname == "Mehrsilbig 2":
		self.liste = self.mehrsilbig	
	elif katalogname == u"Ähnlicher Klang 1":
		self.liste = self.p1	
	elif katalogname == u"Ähnlicher Klang 2":
		self.liste = self.p2	
	elif katalogname == u"Ähnlicher Klang 3":
		self.liste = self.p3	
	elif katalogname == u"Ähnlicher Klang 4":
		self.liste = self.p4	
	elif katalogname == u"Ähnlicher Klang 5":
		self.liste = self.p5	
	else:
		print "KATALOG NICHT GEFUNDEN"
		return

	# der Zähler muss auf 0 gesetzt werden damit wirklich
	# vom ersten Wort an gezählt wird!
	counter = 0
	print self.liste

    def begriffeAufdecken(self):
	d = AufdeckenDialog(self, self.liste)
	d.exec_()
		
    def timeout(self):
	if self.counter >= len( self.liste ):
		print "Stoppe den Timer..."
		self.timer.stop()
		self.running = False
		self.button.setText( "&Start" )
		self.text.setText( u"--- Testende ---" )
		return

	print "%i von %i" % ( self.counter + 1, len (self.liste) ) 
	self.status.setText( "%i von %i" % ( self.counter + 1, len (self.liste) ) ) 
	
	wort = self.liste[ self.counter ]
	self.text.setText( wort )
	self.counter += 1

    def loadLists(self):
	self.mehrsilbig1 = [ "Klarinette", "Schokolade", "Aprikose", "Geschwindigkeit", "Versicherung", "Hagebutte", "Geburtstag", "Schraubenzieher", "Kugelschreiber", "Altpapier", "Trompete", "Mandarine", "Schauspieler", "Mathematik", "Australien", "Fotoapparat", "Amateur", "Tankstelle", "Geschmack", "Baustelle", "Dalmatiner", "Banane", "Moskito", "Beschreibung", "Weihnachten", "Haltestelle", "Minute", "Kassette", "Beschwerde", "Klempner" ]
	self.mehrsilbig2 = [ "Galapagos", "Buchstabe", "Tablette", "Krawatte", "Hubschrauber", "Wanderung", "Fernsteuerung", "Diamant", "Feuerwehr", "Pistole", "Operation", "Restaurant", "Schimmel", "Herberge", "September", "Gefangener", "Flughafen", "Bauernhof", "Schallplatte", "Tiefschnee", "Dezember", "Paradies", "Apotheke", "Telefon", "Kartoffel", "Rezept", "Professor", "Sauerbraten", "Seilbahn", "Monitor" ] 
	
	self.einsilbig1 = [ "Turm", "Zaun", "Uhr", "Bahn", "Weg", "Holz", "Ball", "Wort", "Keks", "Lohn", "Brot", "Flug", "Mund", "Sturm", "Bein", "Bach", "Pfahl", "Senf", "Bus", "Tuch", "Bad", "Maus", "Darm", "Ort", "Boot", "Napf", "Klee", "Band", "Zahn", "Pfand" ]
	self.einsilbig2 = ["Glut", "Hand", "Schiff", "Kuh", "Burg", "Herd", "Tal", "Kreis", "Heu", "Wand", "Pferd", "Rad", "Pilz", "Loch", "Ton", "Frau", "Kinn", "Jod", "Tanz", "Bild", "Tor", "Hof", "Teig", "Rest", "Bart", "Senf", "Neid", "Sau", "Milch", "Magd" ]
	
	self.zweisilbig = [ "Kabel", "Motor", "Angel", "Vase", "Liebe", "Gurke", "Rabe", "Bibel", "Omen", "Mutter", "Apfel", "Quelle", "Zirkus", "Hirse", "Ofen", "Ober", "Wiese", "Grotte" ]
	self.p1 = [ "Dichter", "Richter", "Lichter", "Trichter", "Schlichter", "Tischler", "Fischer", "Gesichter" ]
	self.p2 = [ "Hase", "Nase", "Vase", "Blase", "Phrase", "Gase", "Strasse", "Tasse", "Masse" ]
	self.p3 = [ "Dose", "Hose", "Lose", "Rose", u"Soße", "Moose", "Boote", "Schlote" ]
	self.p4 = [ "Ratte", "Watte", "Matte", "Latte", "Natter", "Braten", "Raten", "Garten" ]
	self.p5 = [ "Reise", "Schneise", "Weise", "Meise", "Preise", "leise", "Greise", "Zeisig" ]

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()

