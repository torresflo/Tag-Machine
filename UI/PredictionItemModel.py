from PySide6 import QtCore, QtWidgets, QtGui

class PredictionItemModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.m_data = data       

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.m_data)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 3

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return None

        if orientation == QtCore.Qt.Horizontal:
            if section == 0:
                return "Filename"
            elif section == 1:
                return "Found tags"
            else:
                return "Probability"
        return None

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            item = self.m_data[index.row()][index.column()]
            if index.column() == 0:
                return QtCore.QFileInfo(item).fileName()
            elif index.column() == 1:
                tags = item.m_label
                for category in item.m_categories:
                    tags += ", " + category
                return tags
            elif index.column() == 2:
                return "{:4.2f} %".format(item)
            return item
        return None
