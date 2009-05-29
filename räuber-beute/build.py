#!/usr/bin/env python

import os

command = "pyuic4 -o ui_maindlg.py maindlg.ui"
print "Running " + command
os.system(command)
