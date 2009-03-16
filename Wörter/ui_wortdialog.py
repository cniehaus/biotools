# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wortdialog.ui'
#
# Created: Thu Oct  2 15:38:27 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WortDialog(object):
    def setupUi(self, WortDialog):
        WortDialog.setObjectName("WortDialog")
        WortDialog.resize(508,508)
        self.gridLayout = QtGui.QGridLayout(WortDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtGui.QTableWidget(WortDialog)
        self.tableWidget.setMinimumSize(QtCore.QSize(500,500))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator",QtCore.QVariant(False))
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget,0,0,1,1)

        self.retranslateUi(WortDialog)
        QtCore.QMetaObject.connectSlotsByName(WortDialog)

    def retranslateUi(self, WortDialog):
        WortDialog.setWindowTitle(QtGui.QApplication.translate("WortDialog", "Auflösung", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

