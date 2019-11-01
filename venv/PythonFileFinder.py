import sys
from interfaceUI import *
from utility import *
from QCustomWidgetList import *




class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.entries = []
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
        if self.entries:
            print(len(self.entries))
            indexNumber = self.entries[self.ui.listWidget.currentRow()].path
            run(self, indexNumber)
            # run(self, self.ui.listWidget.currentItem().text())
        else:
            showMessage(self, msg = "There is nothng to run!!!")

    def getUserInput(self):
        return self.ui.lineEdit.text()

    def clearInterface(self):
        self.ui.lineEdit.clear()
        self.ui.listWidget.clear()
        self.entries = []

    def addList(self):
        self.ui.listWidget.clear()
        text = self.getUserInput()
        self.entries = getFileResult(self, text)
        for obj in self.entries:
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp('File Type: ' + obj.fileType)
            myQCustomQWidget.setTextDown('File Name: ' + obj.fileName)
            myQCustomQWidget.setIcon("img/" + obj.icon)
            myQCustomQWidget.setTextPath('Path: ' + obj.path)
            myQListWidgetItem = QtWidgets.QListWidgetItem(self.ui.listWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.ui.listWidget.addItem(myQListWidgetItem)
            self.ui.listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())