#!/usr/bin/env python

import os

command1 = "pyuic4 -o ui_maindlg.py maindlg.ui"
command2 = "pyuic4 -o ui_wortdialog.py wortdialog.ui"
print "Running " + command1
os.system(command1)
print "Running " + command2
os.system(command2)
