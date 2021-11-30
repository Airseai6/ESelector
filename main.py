# -*- coding: utf-8 -*-

import sys, os
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIcon
from UI.ESelector import Ui_MainWindow
from UI import ico
import SignalsAndSlots


# form File list
def formFileList(dir,fileType):
    fileList = []
    if fileType == 'Word':
        suffix1,suffix2 = '.docx', '.DOCX'
    else:
        suffix1,suffix2 = '.xlsx', '.xls'

    for root, _, files in os.walk(dir):
        for fn in files:
            if (fn.endswith(suffix1) or fn.endswith(suffix2)) and fn[:2] != '~$':
                fileList.append(os.path.join(root.replace('/', '\\'), fn))
    return fileList


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.directory = ''
        self.key = ''
        self.fileList = []
        self.result = []
        

    def select_floder(self):
        folder = QFileDialog.getExistingDirectory(None,"选取文件夹",self.directory)
        if folder:
            self.directory = folder
            folder = folder.replace('/', '\\')
            self.ui.lab_address.setText(folder)
            self.ui.textEdit.append(f"选定文件夹 {folder}.")
    
    def dealt_filter_type(self,index):
        """ index: 0:Excel, 1:Word """
        if index == 0:
            self.ui.comboBox_type.setDisabled(False)
        elif index == 1:
            self.ui.comboBox_type.setCurrentIndex(0)    # 文本
            self.ui.comboBox_type.setDisabled(True)

    def key_change(self):
        self.key = self.ui.lineEdit.text()
        try:
            _ = float(self.key)
        except ValueError:
            if self.ui.comboBox_type.currentIndex() == 1:
                self.ui.comboBox_type.setCurrentIndex(0)
                self.ui.textEdit.append(f"非数值类型自动切换成文本查找")

    def key_type_change(self,index):
        """ index: 0:文本, 1:数值 """
        if self.key:
            try:
                _ = float(self.key)
            except ValueError:
                if index == 1:
                    self.ui.comboBox_type.setCurrentIndex(0)
                    self.ui.textEdit.append("非数值类型自动切换成文本查找")
        

    def initSignalsAndSlots(self):
        # 主页面帮助信息
        self.ui.textEdit.append("目前word只支持.docx格式,不支持.doc格式")
        self.ui.textEdit.append("文本支持模糊查找,数值仅支持精确查找")
        # 主页面运行的信号和槽
        self.ui.btn_select.clicked.connect(self.select_floder)
        self.ui.comboBox_file.currentIndexChanged.connect(self.dealt_filter_type)
        self.ui.lineEdit.editingFinished.connect(self.key_change)
        self.ui.comboBox_type.currentIndexChanged.connect(self.key_type_change)
        # 线程运行的信号和槽
        self.ui.btn_start.clicked.connect(self.start_ckick)
        self.ui.listWidget.doubleClicked.connect(self.result_double_click)


    def start_ckick(self):
        if not self.directory:
            self.ui.textEdit.append("请选择适当的文件夹")
        elif not self.key:
            self.ui.textEdit.append("请填写关键词")
        else:
            file_type = self.ui.comboBox_file.currentText()
            self.fileList = formFileList(self.directory,file_type)
            if not self.fileList:
                self.ui.textEdit.append(f'该文件夹未包含{file_type}文件，请重新选择.')
            elif file_type == 'Excel':
                self.dealt_excel_thread = SignalsAndSlots.DealtExcelThread(self)
                self.dealt_excel_thread.start()
            elif file_type == 'Word':
                self.dealt_word_thread = SignalsAndSlots.DealtWordThread(self)
                self.dealt_word_thread.start()

    def result_double_click(self,qModelIndex):
        index = qModelIndex.row()
        self.open_excel_thread = SignalsAndSlots.OpenFileThread(self,index)
        self.open_excel_thread.start()

    
    @Slot(str)
    def log_add(self, msg):
        self.ui.textEdit.append(msg)

    @Slot(str)
    def result_add(self, msg):
        self.ui.listWidget.addItem(msg)

    @Slot(str)
    def result_clear(self):
        self.ui.listWidget.clear()

    @Slot(int)
    def pbar_change(self, num):
        self.ui.progressBar.setValue(num)

    @Slot(int)
    def btn_start_enable(self, b):
        self.ui.btn_start.setEnabled(b)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    window = MainWindow()

    window.setWindowTitle('Excel&Word内容查找工具')
    window.setWindowIcon(QIcon(":/t.ico"))
    window.initSignalsAndSlots()
    window.show()

    sys.exit(app.exec())
