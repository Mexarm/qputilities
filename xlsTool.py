#!/usr/bin/python
import sys
import openpyxl

import xlsTool_ui
              
from PyQt4 import QtGui
from PyQt4 import QtCore

class xlsToolApp(QtGui.QMainWindow, xlsTool_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.connect(self.btn_Abrir,QtCore.SIGNAL("clicked()"),self.open_file)

    def open_file(self):
        dlg = QtGui.QFileDialog()
        dlg.setWindowTitle( 'Seleccione archivo' )
        dlg.setViewMode( QtGui.QFileDialog.Detail )
        dlg.setNameFilters( [self.tr('archivo xls (*.xls)'), self.tr('archivo xlsx (*.xlsx)'), self.tr('archivo csv (*.csv)'), self.tr('archivo txt (*.txt)'), self.tr('todos los archivos (*)')] )
        
        name = dlg.getOpenFileName(self,'Open File')
        self.le_Archivo.setText(name)
        if name:
            self.read_excel_file(unicode(name))

    def read_excel_file(self,file_):
        wb=openpyxl.load_workbook(file_)
        sheets=wb.get_sheet_names()
        activeSheet=wb.active
        self.table.setColumnCount(activeSheet.max_column)
        self.table.setRowCount(3)
        print activeSheet.max_column
        for c in range(activeSheet.max_column):
            self.table.setCellWidget(0,c, QtGui.QLabel(activeSheet.cell(row=1, column=c+1).value))
        #self.prepare_comboboxes()            
def main():
    app = QtGui.QApplication(sys.argv) 
    form = xlsToolApp()                
    form.show()                        
    sys.exit(app.exec_())              


if __name__ == '__main__':             
    main()                    
