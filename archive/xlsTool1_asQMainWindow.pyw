import sys
import openpyxl

from PyQt4 import QtCore, QtGui


class Form(QtGui.QMainWindow):

    def __init__(self):
        super(Form,self).__init__()
        self.setup_ui()
        

    def setup_ui(self):
        widget = QtGui.QWidget()
        vbox = QtGui.QVBoxLayout(widget)
        self.setCentralWidget(widget)
        
        grid= QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel("Archivo"),0,0)
        self.fileLE=QtGui.QLineEdit()
        grid.addWidget(self.fileLE,0,1)
        btn_open=QtGui.QPushButton("&Abrir")
        grid.addWidget(btn_open,0,2)
        vbox.addLayout(grid)
        
        
       
def main():
    app = QtGui.QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
