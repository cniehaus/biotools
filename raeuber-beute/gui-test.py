#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dieses Programm dient zum Verstehen der Räuber-Beute-Beziehungen.

Carsten Niehaus (ni@kgs-rastede.de)
License: GPLv2+
Last modified: Juni und Juli 2009
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

from dataholder import *
from predatorpreycalculator import *

from ui_werkzeuge import Ui_WerkzeugForm

class WerkzeugForm(QDialog, Ui_WerkzeugForm):
    """This class is the widget in which the user can setup 
    every aspect of the simulation.
    """
    def __init__(self, parent=None):
        super(WerkzeugForm, self).__init__(parent)
        self.setupUi(self)
        
class Form(QMainWindow):
    """This class is the application itself
    
    A very good tutorial about all this can be found here:
    http://www.scipy.org/LoktaVolterraTutorial
    """
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Predator-Prey-Simulation")

        self.data = DataHolder()

        self.create_main_frame()
        self.create_status_bar()
        
        self.on_show()
        
    def update_values(self):
        """In the GUI the user is able to change several settings of
        the simulation. This method sets those values in the simulator-
        class
        """
        self.data.simulator.a = self.tools.a.value() 
        self.data.simulator.b = self.tools.b.value()
        self.data.simulator.c = self.tools.c.value()
        self.data.simulator.p = self.tools.p.value()
        self.data.simulator.iterations = self.tools.iterations.value()
        self.data.simulator.Prey0 = self.tools.Prey0.value()
        self.data.simulator.Predator0 = self.tools.Predator0.value()

    def calculate_data(self):
        self.update_values()
        self.data.calculate_from_values()
    
    def on_show(self):
        self.calculate_data()
        
        self.axes.clear()        
        self.axes.grid(True)
        self.axes.set_xlabel("Iterations")
        self.axes.set_ylabel("Populationsize")

        x_from = 0
        x_to = self.tools.iterations.value()
        series_predator = self.data.get_series_data("Predator")[x_from:x_to + 1]
        series_prey     = self.data.get_series_data("Prey")[x_from:x_to + 1]
        
        #These seems not needed at all...
        #predator_length = range(len(series_predator))
        #prey_length = range(len(series_prey))
        
        self.axes.plot(series_predator, '-', label="Predator")
        self.axes.plot(series_prey, '-', label="Prey")
        
        #The following lines create a nice annotation box, can be used lated to
        #highlight certain aspects of the plot
        #self.axes.annotate('Test123', xy=(1000, 25), size=20, xycoords='data', textcoords='offset points',
        #                   bbox=dict(boxstyle="round4,pad=.5", fc="0.8" ), 
        #                   xytext=(-70, -60),
        #                   arrowprops=dict(arrowstyle="->", 
        #                                   connectionstyle="angle,angleA=0,angleB=-90,rad=10"))
        
        if self.tools.legend_cb.isChecked():
            self.axes.legend()
        self.canvas.draw()

    def on_about(self):
        msg = __doc__
        QMessageBox.about(self, u"Über Räuber-Beute", msg.strip())
  
    def create_main_frame(self):
        self.main_frame = QWidget()
        
        plot_frame = QWidget()
        self.tools = WerkzeugForm()
        
        dock = QDockWidget("Tools", self)
        dock.setObjectName("ToolsDockWidget")
        dock.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        dock.setWidget(self.tools)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        
        self.axes = self.fig.add_subplot(111)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
   
        self.connect(self.tools.show_button, SIGNAL('clicked()'), self.on_show)

        left_vbox = QVBoxLayout()
        left_vbox.addWidget(self.canvas)
        left_vbox.addWidget(self.mpl_toolbar)
        
        hbox = QHBoxLayout()
        hbox.addLayout(left_vbox)
        self.main_frame.setLayout(hbox)

        self.setCentralWidget(self.main_frame)
    
    def create_status_bar(self):
        self.status_text = QLabel("Predator and Prey Simulation")
        self.statusBar().addWidget(self.status_text, 1)

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

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    
    f = Form()
    f.show()

    app.exec_()

    
   