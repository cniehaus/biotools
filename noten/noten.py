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
import re, datetime, calendar 

from ui_maindlg import Ui_MainDlg 
from datenklassen import *

class MainDialog(QDialog, Ui_MainDlg):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.hj = Halbjahr()
        self.klasse = Klasse( "8A3")                
        self.termineAnzeigen()
        
    def termineAnzeigen(self):
        self.terminWidget.setText(str(datetime.date.today()))

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	form = MainDialog()
	form.show()
	app.exec_()

