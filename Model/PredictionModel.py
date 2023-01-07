from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification
import torch

from Model.ClassRules import ClassRules

class PredictionModel:
    def __init__(self):
        self.m_predictions = []
        self.m_classRules = ClassRules()

        self.m_featureExtractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
        self.m_model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

        #self.m_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        #self.m_model.to(self.m_device)

    def computePredictions(self, fileNames):
        self.m_predictions = []

        for fileName in fileNames:
            with Image.open(fileName) as image:
                inputs = self.m_featureExtractor(images=image, return_tensors="pt")
                outputs = self.m_model(**inputs)
                logits = outputs.logits
                
                predictedClass = logits.argmax().item()
                predictionProbability = logits.softmax(dim=1).max().item() * 100.0

                classNames = self.m_model.config.id2label[predictedClass]
                className = classNames.split(",")[0]

                if self.m_classRules.isPredictionValid(className, predictionProbability):
                    information =  self.m_classRules.getClassInformation(className)
                    self.m_predictions.append([fileName, information, predictionProbability])
        
        return self.m_predictions
    
    def getLastPredictions(self):
        return self.m_predictions