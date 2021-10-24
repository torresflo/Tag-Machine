import os
from PySide6 import QtCore

class ClassInformation:
    def __init__(self):
        self.m_label = ""
        self.m_priority = 0
        self.m_threshold = 0.0
        self.m_categories = []

    def loadData(self, className:str, jsonValue:QtCore.QJsonValue):
        if "label" in jsonValue.keys():
            self.m_label = jsonValue["label"]
        else:
            self.m_label = className

        if "priority" in jsonValue.keys():
            self.m_priority = jsonValue["priority"]
        if "threshold" in jsonValue.keys():
            self.m_threshold = jsonValue["threshold"] * 100.0
        if "categories" in jsonValue.keys():
            self.m_categories = jsonValue["categories"]

class ClassRules:
    def __init__(self):

        self.m_minimumThreshold = 30.0

        self.m_executionPath = os.getcwd()
        jsonFile = QtCore.QFile(os.path.join(self.m_executionPath, "Model/imagenet_class_rules.json"))
        jsonFile.open(QtCore.QIODevice.ReadOnly)
        jsonData = jsonFile.readAll()
        
        self.m_jsonClassRules = QtCore.QJsonDocument.fromJson(jsonData).object()

        self.m_rules = dict()
        for key, values in self.m_jsonClassRules.items():
            self.m_rules[key] = ClassInformation()
            if "see" in values.keys():
                className = values["see"]
                self.m_rules[key].loadData(className, self.m_jsonClassRules[className])
            else:
                self.m_rules[key].loadData(key, values)

    def isPredictionValid(self, predictionName:str, probability:float) -> bool:
        if probability < self.m_minimumThreshold:
            return False

        if predictionName not in self.m_rules.keys():
            return False

        if self.m_rules[predictionName].m_threshold > probability:
            return False

        return True

    def getClassInformation(self, predictionName:str) -> ClassInformation:
        return self.m_rules[predictionName]