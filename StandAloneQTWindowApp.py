import sys
from PySide2 import QtWidgets

class StandAloneWindow(QtWidgets.QWidget):
    def __init__(self):
        super(StandAloneWindow, self).__init__(parent=None)
        self.setWindowTitle("StandAlone App")
        self.setMinimumSize(400, 300)

        self.close_btn = QtWidgets.QPushButton("Close", self)
        self.close_btn.clicked.connect(self.close)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = StandAloneWindow()
    win.show()
    app.exec_()