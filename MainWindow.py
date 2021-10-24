
import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
from iptcinfo3 import IPTCInfo
from PySide6 import QtCore, QtWidgets, QtGui

from ClassRules import ClassInformation, ClassRules

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Model
        self.m_featureExtractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
        self.m_model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

        #self.m_device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        #self.m_model.to(self.m_device)

        self.m_classRules = ClassRules()

        # UI
        self.m_loadFileButton = QtWidgets.QPushButton("Load file...")
        self.m_classifyImageButton = QtWidgets.QPushButton("Classify image")
        self.m_writeTagsButton = QtWidgets.QPushButton("Write tags in images")
        self.m_fileNamesPlainTextEdit = QtWidgets.QPlainTextEdit("No file loaded...")
        self.m_resultPlainTextEdit = QtWidgets.QPlainTextEdit("No data yet...")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.m_loadFileButton)
        self.layout.addWidget(self.m_fileNamesPlainTextEdit)
        self.layout.addWidget(self.m_classifyImageButton)
        self.layout.addWidget(self.m_resultPlainTextEdit)
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
        resultString = ""
        self.m_predictions = []

        for fileName in self.m_fileNames:
            imageClassificationString = ""

            fileNameWithouPathString = QtCore.QFileInfo(fileName).fileName()
            image = Image.open(fileName)
            inputs = self.m_featureExtractor(images=image, return_tensors="pt")
            outputs = self.m_model(**inputs)
            logits = outputs.logits
            
            predictedClass = logits.argmax().item()
            predictionProbability = logits.softmax(dim=1).max().item()

            classNames = self.m_model.config.id2label[predictedClass]
            className = classNames.split(",")[0]

            if self.m_classRules.isPredictionValid(className, predictionProbability):
                information =  self.m_classRules.getClassInformation(className)
                self.m_predictions.append([fileName, information])

                imageClassificationString += fileNameWithouPathString + ' -> ' + className + ' = ' + information.m_label
                if information.m_categories:
                    imageClassificationString += str(information.m_categories)
                imageClassificationString += ' (' + "{:4.2f}".format(predictionProbability * 100) + '%)\n'

            if imageClassificationString == "":
                resultString += fileNameWithouPathString + " : Nothing usefull found...\n"
            else:
                resultString += imageClassificationString

        self.m_resultPlainTextEdit.setPlainText(resultString)

    @QtCore.Slot()
    def onWriteTagsButtonClicked(self):
        for data in self.m_predictions:
            filename = data[0]
            prediction = data[1]

            iptcInfo = IPTCInfo(filename, force=True)

            if prediction.m_label not in iptcInfo['keywords']: 
                iptcInfo['keywords'].append(prediction.m_label)
            
            for category in prediction.m_categories:
                if category not in iptcInfo['keywords']:
                    iptcInfo['keywords'].append(category)

            iptcInfo.save()