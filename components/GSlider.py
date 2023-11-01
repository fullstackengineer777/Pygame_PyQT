# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QSlider

class GSlider(QSlider):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.style1 = """
                QSlider::groove::horizontal{
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f4ed19, stop:1 #f4ed19);
                    height: 8px;
                    border-radius: 4px;
                }

                QSlider::handle:horizontal {
                    background: #f4ed19;
                    border: 2px solid #fff;
                    width: 20px;
                    height: 20px;
                    margin: -10px 0;
                    border-radius: 20px;
                }
                """
        self.style2 = """
                QSlider::groove::horizontal{
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f35556, stop:1 #f35556);
                    height: 8px;
                    border-radius: 4px;
                }

                QSlider::handle:horizontal {
                    background: #f35556;
                    border: 2px solid #fff;
                    width: 20px;
                    height: 20px;
                    margin: -10px 0;
                    border-radius: 20px;
                }
                """
        self.style3 = """
                QSlider::groove::horizontal{
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5073f0, stop:1 #5073f0);
                    height: 8px;
                    border-radius: 4px;
                }

                QSlider::handle:horizontal {
                    background: #5073f0;
                    border: 2px solid #ffffff;
                    width: 20px;
                    height: 20px;
                    margin: -10px 0;
                    hollow-radius: 10px;
                }
                """
    
    def setStyle1(self):
        super().setStyleSheet(self.style1)
        #pass

    def setStyle2(self):
        super().setStyleSheet(self.style2)

    def setStyle3(self):
        super().setStyleSheet(self.style3)
