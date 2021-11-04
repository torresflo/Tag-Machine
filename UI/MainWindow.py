from PySide6 import QtCore, QtWidgets, QtGui
from UI.PredictionItemModel import PredictionItemModel

from Model.PredictionModel import PredictionModel
from Model.ImageWriter import ImageWriter

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Model
        self.m_predictionModel = PredictionModel()
        self.m_imageWriter = ImageWriter()

        # UI
        self.m_loadFileButton = QtWidgets.QPushButton("Load files...")
        self.m_classifyImageButton = QtWidgets.QPushButton("Classify images")
        self.m_writeTagsButton = QtWidgets.QPushButton("Write tags in images")

        self.m_fileNamesPlainTextEdit = QtWidgets.QPlainTextEdit("No files loaded...")
        self.m_fileNamesPlainTextEdit.setReadOnly(True)
        self.m_fileNamesPlainTextEdit.setMaximumHeight(100)
        self.m_fileNamesPlainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        self.m_resultTable = QtWidgets.QTableView()
        self.m_resultTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.m_resultTable.horizontalHeader().setStretchLastSection(True)
        self.m_resultTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.m_resultTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.m_loadFileButton)
        self.layout.addWidget(self.m_fileNamesPlainTextEdit)
        self.layout.addWidget(self.m_classifyImageButton)
        self.layout.addWidget(self.m_resultTable)
        self.layout.addWidget(self.m_writeTagsButton)

        self.m_loadFileButton.clicked.connect(self.onLoadFileButtonClicked)
        self.m_classifyImageButton.clicked.connect(self.onClassifyImageButtonClicked)
        self.m_writeTagsButton.clicked.connect(self.onWriteTagsButtonClicked)

    @QtCore.Slot()
    def onLoadFileButtonClicked(self):
        self.m_fileNames, selectedFilter = QtWidgets.QFileDialog.getOpenFileNames(self, "Please select images", "", "Images (*.png *.jpg)")
        fileNamesString = ""
        for fileName in self.m_fileNames:
            fileNamesString += QtCore.QFileInfo(fileName).fileName() + '\n'
        self.m_fileNamesPlainTextEdit.setPlainText(fileNamesString)

    @QtCore.Slot()
    def onClassifyImageButtonClicked(self):
        predictions = self.m_predictionModel.computePredictions(self.m_fileNames)

        if(len(predictions) > 0):
            self.m_resultTable.setModel(PredictionItemModel(predictions))
        else:
            self.m_resultTable.setModel(QtGui.QStandardItemModel(0, 0))

    @QtCore.Slot()
    def onWriteTagsButtonClicked(self):
        lastPredictions = self.m_predictionModel.getLastPredictions()
        self.m_imageWriter.writeTagsFromPredictionsInImages(lastPredictions)
        