import os, subprocess, platform
import scandir
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QDialog, QApplication, QListWidgetItem, \
    QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

#dirpath = "/Users"

dirpath = "../"
entries = []

class dao:
    def __init__(self, icon, fileType, path, fileName):
        self.icon = icon
        self.fileType = fileType
        self.path = path
        self.fileName = fileName



def showMessage(self):
    dlg = QDialog(self)
    dlg.setWindowTitle("Error Message")
    textField = QtWidgets.QTextEdit()
    textField.setPlainText("No application knows how to open the file")
    textField.setReadOnly(True)
    textField.setMaximumHeight(50)
    layout = QVBoxLayout()
    okButton = QPushButton('&Ok')
    okButton.clicked.connect(dlg.accept)
    layout.addWidget(textField)
    layout.addWidget(okButton)
    dlg.setLayout(layout)
    dlg.exec_()


def getFileResult(self, userInput):
    entries1 = []
    print("------------")
    if not entries:
        for r, d, f in scandir.walk(dirpath):
            for file in f:
                icon = "sample.png"
                file_type = "unkown"
                if str(file).endswith("py"):
                    file_type = "py"
                    icon = "py.png"
                if str(file).endswith("docx"):
                    file_type = "docx"
                    icon = "word.png"
                if str(file).endswith("doc"):
                    file_type = "doc"
                    icon = "word.png"
                if str(file).endswith("txt"):
                    file_type = "txt"
                    icon = "txt.png"
                if str(file).endswith("pdf"):
                    file_type = "pdf"
                    icon = "pdf.png"
                if str(file).endswith("png"):
                    file_type = "png"
                    icon = "sample.png"
                path = os.path.join(r, file)
                fileName = file
                if file_type != "unkown":
                    entries.append(dao(icon, file_type, path, fileName))




    for file in entries:



        print(file.fileType)
        if userInput in file.fileName:
            entries1.append(file)

    print(entries1.count)
    print(dirpath)
    print("------------")


    foundpath = ""
    # for f in entries:
    #     foundpath = f
    #     print(userInput + ":  " + f)
    return entries1


def run(self, path):
    foundpath = path
    if platform.system() == 'Darwin':
        result = subprocess.call(("open", foundpath))  # macOS
        print(result)
        if result == 1:
            showMessage(self)
    elif platform.system() == 'Windows':
        result = os.startfile(foundpath)
        print(result)
    else:
        result = subprocess.call(("xdg-open", foundpath))
        print(result)