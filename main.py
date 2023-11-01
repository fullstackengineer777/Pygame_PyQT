from PyQt5 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar

import sys
sys.path.append('components')
from pathlib import Path
from PyQt5.QtWidgets import QApplication

from login import Login


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text())
    
    login = Login()
    login.show()
    sys.exit(app.exec())

# app = QtWidgets.QApplication([])
# volume = PowerBar()
# volume.show()
# app.exec_()