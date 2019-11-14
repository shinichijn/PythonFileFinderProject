import os, subprocess, platform
import scandir
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QDialog, QApplication, QListWidgetItem, \
    QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

#dirpath = "/Users"

dirpath = "../../"
entries = []


class dao:
    def __init__(self, icon, fileType, path, fileName):
        self.icon = icon
        self.fileType = fileType
        self.path = path
        self.fileName = fileName



def showMessage(self, msg = "No application knows how to open the file"):
    dlg = QDialog(self)
    dlg.setWindowTitle("Error Message")
    textField = QtWidgets.QTextEdit()
    textField.setPlainText(msg)
    textField.setReadOnly(True)
    textField.setMaximumHeight(50)
    layout = QVBoxLayout()
    okButton = QPushButton('&Ok')
    okButton.clicked.connect(dlg.accept)
    layout.addWidget(textField)
    layout.addWidget(okButton)
    dlg.setLayout(layout)
    dlg.exec_()



def fetchPath(path):
    for r, d, f in scandir.walk(path):
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
            if str(file).endswith("png") or str(file).endswith("jpg"):
                file_type = "jpg/png"
                icon = "image.png"
            path = os.path.join(r, file)
            fileName = file
            if file_type != "unkown":
                entries.append(dao(icon, file_type, path, fileName))

def getFileResult(self, userInput):
    entries1 = []
    if not entries:
        dirs = [d for d in os.listdir(dirpath) if os.path.isdir(os.path.join(dirpath, d))]
        for file in dirs:
            print(file)
            if (file == 'test'):
                fetchPath(dirpath + '/' + file)

    for file in entries:
        if userInput in file.fileName:
            entries1.append(file)
    foundpath = ""
    # for f in entries:
    #     foundpath = f
    #     print(userInput + ":  " + f)
    return entries1


def run(self, path):
    foundpath = path
    if platform.system() == 'Darwin':
        result = subprocess.call(("open", foundpath))  # macOS
        if result == 1:
            showMessage(self)
    elif platform.system() == 'Windows':
        result = os.startfile(foundpath)
    else:
        result = subprocess.call(("xdg-open", foundpath))