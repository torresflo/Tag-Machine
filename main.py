import sys
from PySide6 import QtWidgets

from MainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    mainWindow = MainWindow()
    mainWindow.setWindowTitle("Hello world")
    mainWindow.show()

    sys.exit(app.exec())
