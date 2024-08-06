import os
from PyQt5.QtWidgets import QMainWindow, QPushButton, QFileDialog, QMessageBox, QApplication
from PyQt5.uic import loadUi
from Os.os import *
 

 
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UIConfig/onePiece.ui', self)  # 加载使用PyDesigner设计的UI文件
        self.choseFloderPushButton.clicked.connect(self.choose_folder)
 
    def choose_folder(self):
        directory = QFileDialog.getExistingDirectory(self, "Choose Directory")
        if directory:
            folder_size = OsFunc.get_folder_size(self, directory)
            QMessageBox.information(self, "Folder Size", f"The size of the folder is: {folder_size}")
 

 
if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()