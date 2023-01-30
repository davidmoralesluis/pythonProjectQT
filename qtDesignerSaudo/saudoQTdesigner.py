#!/usr/bin/env python3

import sys

from PyQt6 import QtWidgets
from PyQt6 import uic

aplicacion= QtWidgets.QApplication(sys.argv)
fiestra = uic.loadUi("saudoQTdesigner.ui")
fiestra.show()
aplicacion.exec()