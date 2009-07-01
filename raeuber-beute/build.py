#!/usr/bin/env python

import os

command = "pyuic4 -o ui_maindlg.py maindlg.ui"
command2 = "pyuic4 -o ui_werkzeuge.py werkzeuge.ui"
print "Running " + command
os.system(command)
print "Running " + command2
os.system(command2)
