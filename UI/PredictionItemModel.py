from PySide6 import QtCore, QtGui
from PIL.ImageQt import ImageQt

class PredictionItemModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.m_data = data       

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.m_data)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 4

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return None

        if orientation == QtCore.Qt.Horizontal:
            if section == 0:
                return "Image"
            elif section == 1:
                return "Filename"
            elif section == 2:
                return "Probability"
            else:
                return "Found tags"
        return None

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            row = index.row()
            if index.column() == 1:
                item = self.m_data[row][0]
                return QtCore.QFileInfo(item).fileName()
            elif index.column() == 2:
                item = self.m_data[row][2]
                return "{:4.2f} %".format(item)
            elif index.column() == 3:
                item = self.m_data[row][1]
                tags = item.m_label
                for category in item.m_categories:
                    tags += ", " + category
                return tags

        if role == QtCore.Qt.DecorationRole:
            if index.column() == 0:
                item = self.m_data[index.row()][0]
                imageQt = ImageQt(item)
                pixmap = QtGui.QPixmap()
                pixmap.convertFromImage(imageQt)
                return pixmap.scaledToHeight(100, QtCore.Qt.SmoothTransformation)
                        
        return None
