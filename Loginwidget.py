from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox


class Loginwidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout()

        self.bn = QLineEdit()
        self.pw = QLineEdit()
        self.btn = QPushButton()

        self.layout.addWidget(self.bn)
        self.layout.addWidget(self.pw)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)
        self.bn.setPlaceholderText("Benutzername")
        self.pw.setPlaceholderText("Passwort")
        self.btn.setText("Login")

        self.btn.clicked.connect(self.controll)

        self.bn.setInputMask("Nnnnnn")
        self.pw.setInputMask("XXXXXX")
        self.pw.setEchoMode(QLineEdit.EchoMode.Password)

        self.benutzer = ["Vincen", "Nadja", "Adrian", "Domi"]
        self.passwort = ["VG1234", "NM1234", "AP1234", "DG1234"]

        self.msgbox = QMessageBox()

    def controll(self):
        for i in range (4):
            if self.bn.text() == self.benutzer[i]:
                self.bncheck = True

            else:
                self.msgbox.setText("Benutzername falsch")
                self.msgbox.show()

            if self.bncheck == True:
                if self.pw.text() == self.passwort[i]:
                    self.pwcheck = True
                    print("Login mit:", self.pw.text(), self.bn.text())
                    break
                else:
                    self.msgbox.setText("Passwort falsch")
                    self.msgbox.show()
                    print("pw falsch")
                    break
