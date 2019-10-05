import sys
from interfaceUI import *
from utility import *


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
        self.ui.listWidget.addItems(entries)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
