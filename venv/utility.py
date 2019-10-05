import os, subprocess, platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QDialog, QApplication, QListWidgetItem, \
    QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

# dirpath = "/Users"

dirpath = "../"


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
    entries = []
    print("------------")
    for r, d, f in os.walk(dirpath):
        for file in f:
            if userInput in file:
                entries.append(os.path.join(r, file))
    print(dirpath)
    print("------------")
    foundpath = ""
    for f in entries:
        foundpath = f
        print(userInput + ":  " + f)
    return entries


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