# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xlsTool.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(515, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn_Abrir = QtGui.QPushButton(self.centralwidget)
        self.btn_Abrir.setObjectName(_fromUtf8("btn_Abrir"))
        self.gridLayout.addWidget(self.btn_Abrir, 0, 2, 1, 1)
        self.le_Remesa = QtGui.QLineEdit(self.centralwidget)
        self.le_Remesa.setObjectName(_fromUtf8("le_Remesa"))
        self.gridLayout.addWidget(self.le_Remesa, 3, 1, 1, 1)
        self.le_Archivo = QtGui.QLineEdit(self.centralwidget)
        self.le_Archivo.setObjectName(_fromUtf8("le_Archivo"))
        self.gridLayout.addWidget(self.le_Archivo, 0, 1, 1, 1)
        self.label_OT = QtGui.QLabel(self.centralwidget)
        self.label_OT.setObjectName(_fromUtf8("label_OT"))
        self.gridLayout.addWidget(self.label_OT, 1, 0, 1, 1)
        self.de_Entrega = QtGui.QDateEdit(self.centralwidget)
        self.de_Entrega.setObjectName(_fromUtf8("de_Entrega"))
        self.gridLayout.addWidget(self.de_Entrega, 4, 1, 1, 1)
        self.le_Proyecto = QtGui.QLineEdit(self.centralwidget)
        self.le_Proyecto.setObjectName(_fromUtf8("le_Proyecto"))
        self.gridLayout.addWidget(self.le_Proyecto, 2, 1, 1, 1)
        self.cb_SkipFirstRow = QtGui.QCheckBox(self.centralwidget)
        self.cb_SkipFirstRow.setChecked(True)
        self.cb_SkipFirstRow.setObjectName(_fromUtf8("cb_SkipFirstRow"))
        self.gridLayout.addWidget(self.cb_SkipFirstRow, 6, 1, 1, 1)
        self.label_Remesa = QtGui.QLabel(self.centralwidget)
        self.label_Remesa.setObjectName(_fromUtf8("label_Remesa"))
        self.gridLayout.addWidget(self.label_Remesa, 3, 0, 1, 1)
        self.label_Proyecto = QtGui.QLabel(self.centralwidget)
        self.label_Proyecto.setObjectName(_fromUtf8("label_Proyecto"))
        self.gridLayout.addWidget(self.label_Proyecto, 2, 0, 1, 1)
        self.btn_ToExtra = QtGui.QPushButton(self.centralwidget)
        self.btn_ToExtra.setObjectName(_fromUtf8("btn_ToExtra"))
        self.gridLayout.addWidget(self.btn_ToExtra, 8, 0, 1, 1)
        self.label_entrega = QtGui.QLabel(self.centralwidget)
        self.label_entrega.setObjectName(_fromUtf8("label_entrega"))
        self.gridLayout.addWidget(self.label_entrega, 4, 0, 1, 1)
        self.le_OT = QtGui.QLineEdit(self.centralwidget)
        self.le_OT.setObjectName(_fromUtf8("le_OT"))
        self.gridLayout.addWidget(self.le_OT, 1, 1, 1, 1)
        self.label_Archivo = QtGui.QLabel(self.centralwidget)
        self.label_Archivo.setObjectName(_fromUtf8("label_Archivo"))
        self.gridLayout.addWidget(self.label_Archivo, 0, 0, 1, 1)
        self.btn_ToRemove = QtGui.QPushButton(self.centralwidget)
        self.btn_ToRemove.setObjectName(_fromUtf8("btn_ToRemove"))
        self.gridLayout.addWidget(self.btn_ToRemove, 7, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout_2.addWidget(self.table, 1, 0, 1, 1)
        self.btn_generar = QtGui.QPushButton(self.centralwidget)
        self.btn_generar.setObjectName(_fromUtf8("btn_generar"))
        self.gridLayout_2.addWidget(self.btn_generar, 2, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Archivo = QtGui.QMenu(self.menubar)
        self.menu_Archivo.setObjectName(_fromUtf8("menu_Archivo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Abrir = QtGui.QAction(MainWindow)
        self.action_Abrir.setObjectName(_fromUtf8("action_Abrir"))
        self.action_Salir = QtGui.QAction(MainWindow)
        self.action_Salir.setObjectName(_fromUtf8("action_Salir"))
        self.menu_Archivo.addAction(self.action_Abrir)
        self.menu_Archivo.addSeparator()
        self.menu_Archivo.addAction(self.action_Salir)
        self.menubar.addAction(self.menu_Archivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_Abrir, self.le_Archivo)
        MainWindow.setTabOrder(self.le_Archivo, self.le_OT)
        MainWindow.setTabOrder(self.le_OT, self.le_Proyecto)
        MainWindow.setTabOrder(self.le_Proyecto, self.le_Remesa)
        MainWindow.setTabOrder(self.le_Remesa, self.de_Entrega)
        MainWindow.setTabOrder(self.de_Entrega, self.cb_SkipFirstRow)
        MainWindow.setTabOrder(self.cb_SkipFirstRow, self.btn_ToRemove)
        MainWindow.setTabOrder(self.btn_ToRemove, self.btn_ToExtra)
        MainWindow.setTabOrder(self.btn_ToExtra, self.table)
        MainWindow.setTabOrder(self.table, self.btn_generar)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "xlsTool Layout", None))
        self.btn_Abrir.setText(_translate("MainWindow", "&Abrir", None))
        self.label_OT.setText(_translate("MainWindow", "OT", None))
        self.cb_SkipFirstRow.setText(_translate("MainWindow", "Primera Linea es Encabezado", None))
        self.label_Remesa.setText(_translate("MainWindow", "Remesa", None))
        self.label_Proyecto.setText(_translate("MainWindow", "Nombre del Proyecto", None))
        self.btn_ToExtra.setText(_translate("MainWindow", "Quitar->Extra", None))
        self.label_entrega.setText(_translate("MainWindow", "Fecha de Entrega", None))
        self.label_Archivo.setText(_translate("MainWindow", "Archivo", None))
        self.btn_ToRemove.setText(_translate("MainWindow", "Extra->Quitar", None))
        self.btn_generar.setText(_translate("MainWindow", "&Generar", None))
        self.menu_Archivo.setTitle(_translate("MainWindow", "&Archivo", None))
        self.action_Abrir.setText(_translate("MainWindow", "&Abrir", None))
        self.action_Salir.setText(_translate("MainWindow", "&Salir", None))

