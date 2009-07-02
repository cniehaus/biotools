#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dieses Programm dient zum Verstehen der Räuber-Beute-Beziehungen.

Carsten Niehaus (ni@kgs-rastede.de)
License: GPLv2+
Last modified: Juni und Juli 2009
"""
import sys, os, csv
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

#===========================
"""
Based on code written by Amit Kumar (Oct 01, 2006)

The code was ported from Amit Kumars JAVA-code to Python 2.6 
by Carsten Niehaus (cniehaus@kde.org) in 2009 and enhanced.

It is licenced under the GPL v2+.

a = Intrinsic rate of Prey Population Increase ;
b = Predation Rate Coefficient ;
p = Reproduction rate of Predators ( after eating preys );
c = Death Rate of Predators ;
Prey0 = Initial Prey Population ;
Predator0 = Initial Predator Population;
dt = Time Step;
"""
class PredatorPreyCalculator(object):
    def __init__(self):
        self.a=1.0
        self.b=0.2
        self.c=0.5
        self.p=0.04
        self.Prey0=5
        self.Predator0=2
        self.dt=0.01
        self.tstart=0.0
        self.iterations=5000  
    
    def dx(self, x,y):
        return self.a*x-self.b*x*y

    def dy(self, x,y):
        return self.p*x*y-self.c*y
        
    def calculate(self):
        r_string = ["R"]
        b_string = ["B"]
        
        i = 0
        x = self.Prey0
        y = self.Predator0
        t = self.tstart
    
        while i < self.iterations:
            t = i * self.dt
            xnew = x + self.dx(x,y) * self.dt
            ynew = y + self.dy(x,y) * self.dt
            
            x = xnew
            y = ynew
            
            r_string.append(x)
            b_string.append(y)
            
            i += 1
        
        
            
        return r_string, b_string



#==============================
from ui_werkzeuge import Ui_WerkzeugForm

class WerkzeugForm(QDialog, Ui_WerkzeugForm):
	def __init__(self, parent=None):
		super(WerkzeugForm, self).__init__(parent)
		self.setupUi(self)
#==============================

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle(u"Räuber und Beute Beziehungen")

        self.data = DataHolder()
        self.series_list_model = QStandardItemModel()
        
        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()
        
        self.update_ui()
        self.on_show()
        
    def update_values(self):
        self.data.simulator.a = self.tools.a.value() 
        self.data.simulator.b = self.tools.b.value()
        self.data.simulator.c = self.tools.c.value()
        self.data.simulator.p = self.tools.p.value()
        self.data.simulator.iterations = self.tools.iterations_slider.value()
        self.data.simulator.Prey0 = self.tools.Prey0.value()
        self.data.simulator.Predator0 = self.tools.Predator0.value()

    def calculate_data(self):
        self.update_values()
        self.data.calculate_from_values()
        self.update_ui()
    
    def load_file(self, filename=None):
        if not filename:
            filename = QFileDialog.getOpenFileName(self, 
                   'Open a data file', '.', 'CSV files (*.csv);;All Files (*.*)')
        
        if filename:
            self.data.load_from_file(filename)
            self.fill_series_list(self.data.series_names())
            self.status_text.setText("Loaded " + filename)
            self.update_ui()
    
    def update_ui(self):
        if self.data.series_count() > 0 and self.data.series_len() > 0:
            self.tools.from_spin.setValue(0)
            self.tools.to_spin.setValue(self.data.series_len() - 1)
            
            for w in [self.tools.from_spin, self.tools.to_spin]:
                w.setRange(0, self.data.series_len() - 1)
                w.setEnabled(True)
        else:
            for w in [self.tools.from_spin, self.tools.to_spin]:
                w.setEnabled(False)
    
    def on_show(self):
        self.calculate_data()
        
        self.axes.clear()        
        self.axes.grid(True)
        

        x_from = self.tools.from_spin.value()
        x_to = self.tools.to_spin.value()
        series_predator = self.data.get_series_data("R")[x_from:x_to + 1]
        series_prey     = self.data.get_series_data("B")[x_from:x_to + 1]
        self.axes.plot(range(len(series_predator)), series_predator, 'o-', label="Predator")
        self.axes.plot(range(len(series_prey)), series_prey, 'o-', label="Beute")
        
        if self.tools.legend_cb.isChecked():
            self.axes.legend()
        self.canvas.draw()

    def on_about(self):
        msg = __doc__
        QMessageBox.about(self, u"Über Räuber-Beute", msg.strip())

    def fill_series_list(self, names):
        self.series_list_model.clear()
        
        for name in names:
            item = QStandardItem(name)
            item.setCheckState(Qt.Unchecked)
            item.setCheckable(True)
            self.series_list_model.appendRow(item)
    
    def create_main_frame(self):
        self.main_frame = QWidget()
        
        plot_frame = QWidget()
        self.tools = WerkzeugForm()
        
        self.dpi = 100
        self.fig = Figure((6.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        
        self.axes = self.fig.add_subplot(111)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
   
        self.connect(self.tools.show_button, SIGNAL('clicked()'), self.on_show)
        
        self.fill_series_list(self.data.series_names())
        self.update_ui()


        left_vbox = QVBoxLayout()
        left_vbox.addWidget(self.canvas)
        left_vbox.addWidget(self.mpl_toolbar)
        
        hbox = QHBoxLayout()
        hbox.addLayout(left_vbox)
        hbox.addWidget(self.tools)
        self.main_frame.setLayout(hbox)

        self.setCentralWidget(self.main_frame)
    
    def create_status_bar(self):
        self.status_text = QLabel("Please load a data file")
        self.statusBar().addWidget(self.status_text, 1)

    def create_menu(self):        
        self.file_menu = self.menuBar().addMenu("&File")
        
        load_action = self.create_action("&Load file",
            shortcut="Ctrl+L", slot=self.load_file, tip="Load a file")
        quit_action = self.create_action("&Quit", slot=self.close, 
            shortcut="Ctrl+Q", tip="Close the application")
        
        self.add_actions(self.file_menu, 
            (load_action, None, quit_action))
            
        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About", 
            shortcut='F1', slot=self.on_about, 
            tip='About the demo')
        
        self.add_actions(self.help_menu, (about_action,))

    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(  self, text, slot=None, shortcut=None, 
                        icon=None, tip=None, checkable=False, 
                        signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action


class DataHolder(object):
    """ Just a thin wrapper over a dictionary that holds integer 
        data series. Each series has a name and a list of numbers 
        as its data. The length of all series is assumed to be
        the same.
        
        The series can be read from a CSV file, where each line
        is a separate series. In each series, the first item in 
        the line is the name, and the rest are data numbers.
    """
    def __init__(self, filename=None):
        self.load_from_file(filename)
        self.simulator = PredatorPreyCalculator()
    
    def calculate_from_values(self):
        self.data = {}
        self.names = ["R", "B"]
                       
        r, b = self.simulator.calculate()
        
        self.data["R"] = map(float, r[1:])
        self.data["B"] = map(float, b[1:])
        self.datalen = len(r[1:])
       
        
        
    
    def load_from_file(self, filename=None):
        self.data = {}
        self.names = ["R", "B"]
        
        if filename:
            for line in csv.reader(open(filename, 'rb')):
                self.data[line[0]] = map(float, line[1:])
                self.datalen = len(line[1:])
    
    def series_names(self):
        """ Names of the data series
        """
        return self.names
    
    def series_len(self):
        """ Length of a data series
        """
        return self.datalen
    
    def series_count(self):
        return len(self.data)

    def get_series_data(self, name):
        return self.data[name]

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    
    f = Form()
    f.show()
    if len(sys.argv) > 1:
        f.load_file(sys.argv[1])
    app.exec_()

    
   