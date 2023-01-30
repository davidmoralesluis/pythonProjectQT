import sys
from PyQt6 import QtWidgets
from PyQt6.QtUiTools import QUiLoader

cardador = QUiLoader()

aplicacion = QtWidgets.QApplication(sys.argv)
fiestra = cardador.load("saudoDesigner.ui", None)
fiestra.show()
aplicacion.exec()