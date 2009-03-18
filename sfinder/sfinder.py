#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2008-2009 Carsten Niehaus. All rights reserved.
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
from studentclasses import *

class MainDialog(QDialog, Ui_MainDlg):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

	self.aktuelleKlasse = None
	self.klassen = [] 
	self.schueler = [] 
	self.klassen.append( "Alle" )
	self.loadStudents()
	self.createUi()

	self.aktuelleSchuelerListe = []
	
	self.connect(self.klassenCombo, SIGNAL("activated(QString)"), self.neueKlasse )
	self.connect(self.such_knopf, SIGNAL("clicked()"), self.suchen )
	self.connect(self.verdeckenCheckBox, SIGNAL("clicked()"), self.updateUi )

    def suchen(self):
	print "Suche "+self.name_le.text()

    def createUi(self):
	for k in self.klassen:
		self.klassenCombo.addItem( k )
    
    def neueKlasse(self, klasse):
	print "neueKlasse mit klasse == "+klasse
	if klasse is "Alle":
		#Das geht nicht... Warum nur?
		self.aktuelleKlasse = None
		print "Alle!!!!!!!!!!!!!!!!!!!"
	else:
		print "in der else-Schleife"
		self.aktuelleKlasse = klasse
		
	self.updateUi()
    
    def updateUi(self):
	""" Diese Methode baut die Oberfläche neu auf. """
	self.tabelle.clear()
	
	# Ein einfacher Zähler
	counter = 0

	for s in self.schueler:
		k = str(s.data["klasse"])
		if k == self.aktuelleKlasse or k == self.aktuelleKlasse:
			print s.debugInfo()
			item_kl = QTableWidgetItem( s.data["klasse"] )
			item_vn = QTableWidgetItem( s.vorname )
			item_nn = QTableWidgetItem( s.nachname )
			item_un = QTableWidgetItem( s.data[ "nutzername" ] )
			item_pw = QTableWidgetItem( s.data[ "passwort" ] )

			# Nun bekommt jede Zelle einen passenden Tooltip verpasst
			item_nn.setToolTip( s.toolTipString() )
			item_kl.setToolTip( s.toolTipString() )
			item_vn.setToolTip( s.toolTipString() )
			item_un.setToolTip( s.toolTipString() )
			item_pw.setToolTip( s.toolTipString() )
			
			self.tabelle.setItem( counter, 0 , item_kl )
			self.tabelle.setItem( counter, 1 , item_vn )
			self.tabelle.setItem( counter, 2 , item_nn )
			if not self.verdeckenCheckBox.isChecked():
				self.tabelle.setItem( counter, 3 , item_un )
				self.tabelle.setItem( counter, 4 , item_pw )
			else:
				self.tabelle.setItem( counter, 3, QTableWidgetItem( "verdeckt" ) )
				self.tabelle.setItem( counter, 4, QTableWidgetItem( "verdeckt" ) )
			
			counter += 1

    def loadStudents(self):
	""" In dieser Methode werden die Schuelerdaten geladen"""
        
        error = None
        fh = None

        try:
            filename = "daten.csv"
            fh = QFile( filename )
            lino = 0
            if not fh.open(QIODevice.ReadOnly):
                raise IOError, unicode(fh.errorString())
            stream = QTextStream(fh)

            while not stream.atEnd():
                line = stream.readLine()
                lino += 1
                content = line.split(";")
                nutzername = content[0]
                passwort = content[1]
                uid = content[2]
                vorname = content[3]
                nachname = content[4]
                klasse = content[5]

		if klasse not in self.klassen:
			self.klassen.append( klasse )

		s = Schueler( nachname, vorname )
		s.setData( klasse, nutzername, passwort, uid )
                #self.schueler.append( Schueler( nachname, vorname, klasse, nutzername, \
                #        passwort, uid ) )
                self.schueler.append( s )


        except (IOError, OSError, ValueError), e:
            error = "Failed to load: %s on line %d" % (e, lino)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()

