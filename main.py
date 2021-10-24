import sys
from PySide6 import QtWidgets

from UI.MainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    mainWindow = MainWindow()
    mainWindow.setWindowTitle("Tag Machine")
    mainWindow.show()

    sys.exit(app.exec())
