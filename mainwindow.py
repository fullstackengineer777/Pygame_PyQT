
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout
from PyQt5.QtCore import Qt

import sys

from GSlider import GSlider

class MainWindow(QWidget):
   
    def __init__(self, steps=5, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.resize(900,600)

        layout = QVBoxLayout()
        heading = QLabel(
            'Welcome Back',
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        layout.addWidget(heading)

        self.slider1 = GSlider()
        self.slider1.setOrientation(Qt.Horizontal)
        self.slider1.setStyle1()
        layout.addWidget(self.slider1)
        self.slider2 = GSlider()
        self.slider2.setOrientation(Qt.Horizontal)
        self.slider2.setStyle2()
        layout.addWidget(self.slider2)
        self.slider3 = GSlider()
        self.slider3.setOrientation(Qt.Horizontal)
        self.slider3.setStyle3()
        layout.addWidget(self.slider3)
        
        self.setLayout(layout)