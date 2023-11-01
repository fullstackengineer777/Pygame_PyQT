from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from mainwindow import MainWindow

class Login(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon('./assets/lock.png'))
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(600,400)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setObjectName("login_window")

        heading = QLabel(
            'Circle Shot',
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        heading.setObjectName('heading')

        subheading = QLabel(
            'Please enter your email and password to log in.',
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        subheading.setObjectName('subheading')

        self.email = QLineEdit(self)
        self.email.setPlaceholderText('Enter your email')

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText('Enter your password')

        self.btn_login = QPushButton('Login')
        self.btn_login.setObjectName('btn_login')

        layout.addStretch()
        layout.addWidget(heading)
        layout.addWidget(subheading)

        layoutEmail = QHBoxLayout()
        emailLbl = QLabel('Email:        ')
        emailLbl.setObjectName('email_lbl')
        layoutEmail.addWidget(emailLbl)
        layoutEmail.addWidget(self.email)
        layout.addLayout(layoutEmail)

        layoutPass = QHBoxLayout()
        passLbl = QLabel('Password:')
        passLbl.setObjectName('pass_lbl')
        layoutPass.addWidget(passLbl)
        layoutPass.addWidget(self.password)
        layout.addLayout(layoutPass)
        
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btn_login)

        layout.addLayout(layoutBtn)
        layout.addStretch()

        self.btn_login.clicked.connect(self.openMainWindow)

    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()