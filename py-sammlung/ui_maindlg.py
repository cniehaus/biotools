# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maindlg.ui'
#
# Created: Mon Mar 16 15:12:23 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainDlg(object):
    def setupUi(self, MainDlg):
        MainDlg.setObjectName("MainDlg")
        MainDlg.resize(601, 761)
        self.gridLayout = QtGui.QGridLayout(MainDlg)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(MainDlg)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.klassenCombo = QtGui.QComboBox(MainDlg)
        self.klassenCombo.setObjectName("klassenCombo")
        self.klassenCombo.addItem(QtCore.QString())
        self.klassenCombo.addItem(QtCore.QString())
        self.klassenCombo.addItem(QtCore.QString())
        self.klassenCombo.addItem(QtCore.QString())
        self.horizontalLayout.addWidget(self.klassenCombo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(MainDlg)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.name_le = QtGui.QLineEdit(MainDlg)
        self.name_le.setObjectName("name_le")
        self.horizontalLayout_2.addWidget(self.name_le)
        self.such_knopf = QtGui.QPushButton(MainDlg)
        self.such_knopf.setObjectName("such_knopf")
        self.horizontalLayout_2.addWidget(self.such_knopf)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabelle = QtGui.QTableWidget(MainDlg)
        self.tabelle.setObjectName("tabelle")
        self.tabelle.setColumnCount(3)
        self.tabelle.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tabelle.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabelle.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabelle.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabelle.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tabelle, 2, 0, 1, 1)
        self.closeButton = QtGui.QPushButton(MainDlg)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 3, 0, 1, 1)

        self.retranslateUi(MainDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), MainDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(MainDlg)

    def retranslateUi(self, MainDlg):
        MainDlg.setWindowTitle(QtGui.QApplication.translate("MainDlg", "Elektronische NTW-Sammlung (KGS Rastede) (c) C. Niehaus 2009", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainDlg", "Medientyp", None, QtGui.QApplication.UnicodeUTF8))
        self.klassenCombo.setItemText(0, QtGui.QApplication.translate("MainDlg", "DVD/CD", None, QtGui.QApplication.UnicodeUTF8))
        self.klassenCombo.setItemText(1, QtGui.QApplication.translate("MainDlg", "Video (VHS)", None, QtGui.QApplication.UnicodeUTF8))
        self.klassenCombo.setItemText(2, QtGui.QApplication.translate("MainDlg", "Objektträger", None, QtGui.QApplication.UnicodeUTF8))
        self.klassenCombo.setItemText(3, QtGui.QApplication.translate("MainDlg", "Buch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainDlg", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.such_knopf.setText(QtGui.QApplication.translate("MainDlg", "&Suchen", None, QtGui.QApplication.UnicodeUTF8))
        self.tabelle.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MainDlg", "Neue Zeile", None, QtGui.QApplication.UnicodeUTF8))
        self.tabelle.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainDlg", "Neue Spalte", None, QtGui.QApplication.UnicodeUTF8))
        self.tabelle.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainDlg", "Raum", None, QtGui.QApplication.UnicodeUTF8))
        self.tabelle.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainDlg", "Unterort", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("MainDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
