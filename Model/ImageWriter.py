from iptcinfo3 import IPTCInfo

class ImageWriter:
    def writeTagsFromPredictionsInImages(self, predictions):
        for data in predictions:
            filename = data[0]
            prediction = data[1]

            iptcInfo = IPTCInfo(filename, force=True)

            if prediction.m_label not in iptcInfo['keywords']: 
                iptcInfo['keywords'].append(prediction.m_label)
            
            for category in prediction.m_categories:
                if category not in iptcInfo['keywords']:
                    iptcInfo['keywords'].append(category)

            iptcInfo.save()