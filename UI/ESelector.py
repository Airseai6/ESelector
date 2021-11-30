# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ESelector.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 593)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_select = QPushButton(self.centralwidget)
        self.btn_select.setObjectName(u"btn_select")

        self.gridLayout.addWidget(self.btn_select, 1, 0, 1, 1)

        self.comboBox_file = QComboBox(self.centralwidget)
        self.comboBox_file.addItem("")
        self.comboBox_file.addItem("")
        self.comboBox_file.setObjectName(u"comboBox_file")

        self.gridLayout.addWidget(self.comboBox_file, 1, 1, 1, 2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.comboBox_type = QComboBox(self.centralwidget)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.gridLayout.addWidget(self.comboBox_type, 2, 1, 1, 2)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")

        self.gridLayout.addWidget(self.btn_start, 2, 3, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.gridLayout.addWidget(self.progressBar, 2, 4, 1, 1)

        self.lab_address = QLabel(self.centralwidget)
        self.lab_address.setObjectName(u"lab_address")

        self.gridLayout.addWidget(self.lab_address, 1, 3, 1, 2)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 3)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 3, 3, 2, 2)

        self.btn_clog = QPushButton(self.centralwidget)
        self.btn_clog.setObjectName(u"btn_clog")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clog.sizePolicy().hasHeightForWidth())
        self.btn_clog.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_clog, 4, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.btn_clog.clicked.connect(self.textEdit.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.comboBox_file.setItemText(0, QCoreApplication.translate("MainWindow", u"Excel", None))
        self.comboBox_file.setItemText(1, QCoreApplication.translate("MainWindow", u"Word", None))

        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5173\u952e\u8bcd", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6587\u672c", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6570\u503c", None))

        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.lab_address.setText("")
        self.btn_clog.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
    # retranslateUi

