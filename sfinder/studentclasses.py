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

class Schueler(object):
        """ Basisklasse für das Programm. Alle Infos eines Schülers
        sind hier gespeichert. über debugInfo() erhält man einen kurzen
        Überblick über den Schüler """
        def setData( self, nachname, vorname, klasse, nutzername, passwort, uid ):
                self.data = {"nachname" : nachname, "vorname": vorname, "klasse" : klasse, "nutzername" : nutzername, "passwort" : passwort, "uid" : uid  }

        def debugInfo(self):
            '''Gibt wesentliche Informationen über den Schüler nett formiertiert aus.'''
            return "Schueler: %s %s aus der \t %s." % (self.data["vorname"], self.data["nachname"], self.data["klasse"])

        def name(self):
            '''Gibt den nett formatierten Namen des Schülers aus'''
			return "%s %s" % ( self.data["vorname"], self.data["nachname"] )
		
        def hatDatensatz(self, suche):
            '''Die Funktion gibt True zurück, wenn ein Datenfeld
            eines Schülers den Suchwert beinhaltet. Es wird nicht
            nach genauer Übereinstimmung gesucht!'''
                for item in self.data.itervalues():
                        #print "Item: %s mit suche: %s" % (item, suche)
                        if item.contains(suche):
                                return True

                return False

        def toolTipString(self):
                '''Gibt die drei wichtigsten Eigenschaften eines Schülers zurück:
                        * Name
                        * Benutzername
                        * Passwort
                '''
                return "<html><body><b>Name:</b> %s %s<br /> <b>Nutzername:</b> \t%s<br /><b>Passwort:</b>\t%s</body></html>" % (self.data["vorname"], self.data["nachname"], self.data["nutzername"], self.data["passwort"] )

