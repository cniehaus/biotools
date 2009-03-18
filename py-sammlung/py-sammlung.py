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

import csv

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_maindlg import Ui_MainDlg 
from datenklassen import *

class MainDialog(QDialog, Ui_MainDlg):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

	self.aktuelleMedium = None
	self.klassen = [] 
	self.medien = [] 
	self.klassen.append( "Alle" )
	self.loadMedia()
	self.createUi()

	self.aktuelleSchuelerListe = []
	
	self.connect(self.medienCombo, SIGNAL("activated(QString)"), self.neueKlasse )
	self.connect(self.such_knopf, SIGNAL("clicked()"), self.suchen )

    def suchen(self):
	print "Suche "+self.name_le.text()

    def createUi(self):
	for k in self.klassen:
		self.medienCombo.addItem( k )
    
    def neueKlasse(self, klasse):
	if klasse == "Alle":
		self.aktuelleMedium = None
	else:
		self.aktuelleMedium = klasse
	  
	print "das aktuelle Medium ist nun %s." % self.aktuelleMedium
	self.updateUi()

    def medienListeErstellen(self):
	if self.aktuelleMedium == "Alle":
		print "------------------------------- Alles zurückgeben --------------------__"
		return self.medien
	
	liste = [] 

	for medium in self.medien:
		typ = medium.typ
		if typ == self.aktuelleMedium:
			liste.append( medium )

	return liste
		
    
    def updateUi(self):
	""" Diese Methode baut die Oberfläche neu auf. """
	# Ich finde keine schlauere Methode, um alle Zellen eines QTableWidgets zu löschen
	while self.tabelle.rowCount() > 0:
		self.tabelle.removeRow(0)
	
	# Ein einfacher Zähler
	counter = 0

	self.tabelle.clear()

	for medium in self.medienListeErstellen():
		self.tabelle.insertRow(counter)
		#print s.debugInfo()
		item_vn = QTableWidgetItem( medium.typ )
		item_nn = QTableWidgetItem( medium.referenznummer )
		item_un = QTableWidgetItem( medium.data[ "name" ] )
		self.tabelle.setItem( counter, 0 , item_vn )
		self.tabelle.setItem( counter, 1 , item_nn )
		self.tabelle.setItem( counter, 2 , item_un )
		
		counter += 1

    def loadMedia(self):
	""" In dieser Methode werden die Sammlungsdaten geladen"""
        
        error = None
        fh = None

        try:
            filename = "daten.csv"
            fh = QFile( filename )
            lino = 0
            if not fh.open(QIODevice.ReadOnly):
                raise IOError, unicode(fh.errorString())
            stream = QTextStream(fh)

	    print "starte die while not Schleife"
            while not stream.atEnd():
                line = stream.readLine()
                lino += 1
                content = line.split(";")
                a = content[0]
                b = content[1]
                c = content[2]
                d = content[3]
                e = content[4]
                f = content[5]
                g = content[6]

		if a not in self.klassen:
			self.klassen.append( a )
		
		s = None

		if a == "Objekttraeger":
			s = Objekttraeger( a,b,c,d,e )
		else:
			s = DVD( a,b,c,d )
			
                self.medien.append( s )


        except (IOError, OSError, ValueError), e:
            error = "Failed to load: %s on line %d" % (e, lino)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()

