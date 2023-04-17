from PyQt6.QtWidgets import QMainWindow, QHBoxLayout
from Loginwidget import Loginwidget


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.mywidget = Loginwidget()
        self.setCentralWidget(self.mywidget)

        self.setWindowTitle("Anmeldung")



