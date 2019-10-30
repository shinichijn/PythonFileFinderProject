import sys
from interfaceUI import *
from utility import *


class QCustomQWidget (QtWidgets.QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUpQLabel    = QtWidgets.QLabel()
        self.textDownQLabel  = QtWidgets.QLabel()
        self.textPath = QtWidgets.QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.textQVBoxLayout.addWidget(self.textPath)
        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
        self.iconQLabel      = QtWidgets.QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))

    def setTextPath (self, text):
        self.textPath.setText(text)

    def getTextPath (self):
        return self.textPath.text()

class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Form()
        self.setupUI()

    def setupUI(self):
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.addList)
        self.ui.pushButton_2.clicked.connect(self.clearInterface)
        self.ui.pushButton.clicked.connect(self.runShell)
        self.ui.listWidget.doubleClicked.connect(self.runShell)




        self.show()

    def runShell(self):
        run(self, self.ui.listWidget.currentItem().text())

    def getUserInput(self):
        return self.ui.lineEdit.text()

    def clearInterface(self):
        self.ui.lineEdit.clear()
        self.ui.listWidget.clear()

    def addList(self):
        self.ui.listWidget.clear()
        text = self.getUserInput()
        entries = getFileResult(self, text)
        #self.ui.listWidget.addItems(entries)
        for number in entries:
            print("info")
            print(number.fileType)
        # for index, name, icon in [
        #     ('No.1', 'Meyoko', 'sample.png'),
        #     ('No.2', 'Nyaruko', 'sample.png'),
        #     ('No.3', 'Louise', 'sample.png')]:
        for obj in entries:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp('File Type: ' + obj.fileType)
            myQCustomQWidget.setTextDown('File Name: ' + obj.fileName)
            myQCustomQWidget.setIcon(obj.icon)
            myQCustomQWidget.setTextPath('Path: ' + obj.path)
            # Create QListWidgetItem
            myQListWidgetItem = QtWidgets.QListWidgetItem(self.ui.listWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.ui.listWidget.addItem(myQListWidgetItem)
            self.ui.listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
