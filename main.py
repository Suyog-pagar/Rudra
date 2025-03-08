

import sys
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui


from openingWindowGUI import Ui_firstWindow


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        print("Inside First window")
        self.firstui = Ui_firstWindow()
        self.firstui.setupUi(self)

        self.firstui.movie = QtGui.QMovie("gui_tools\\Hero_Template.gif")
        self.firstui.jarvisIntroLabel.setMovie(self.firstui.movie)
        self.firstui.movie.start()


        self.firstui.startButton.clicked.connect(self.connectSecondWindow)
        self.firstui.loginButton.clicked.connect(self.connectLoginPage)
        self.firstui.exitButton.clicked.connect(self.close)


    def connectSecondWindow(self):
        from secondWindow import Ui_SecondWindow
        self.showSecondWindow = Ui_SecondWindow()
        ui.close()
        self.showSecondWindow.show()

    def connectLoginPage(self):
        from loginWndow import Ui_LoginPage
        self._new_window = Ui_LoginPage()
        self._new_window.show()
        ui.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
