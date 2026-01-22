# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inst_dept_year_semester.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_instDeptYearSemSelection(object):
    def setupUi(self, instDeptYearSemSelection):
        if not instDeptYearSemSelection.objectName():
            instDeptYearSemSelection.setObjectName(u"instDeptYearSemSelection")
        instDeptYearSemSelection.resize(800, 495)
        instDeptYearSemSelection.setStyleSheet(u"background-color: rgb(35, 35, 28);")
        self.centralwidget = QWidget(instDeptYearSemSelection)
        self.centralwidget.setObjectName(u"centralwidget")
        self.myButton = QPushButton(self.centralwidget)
        self.myButton.setObjectName(u"myButton")
        self.myButton.setGeometry(QRect(340, 310, 81, 26))
        self.myLabel = QLabel(self.centralwidget)
        self.myLabel.setObjectName(u"myLabel")
        self.myLabel.setGeometry(QRect(320, 100, 151, 31))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(22)
        font.setBold(True)
        self.myLabel.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 140, 301, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 170, 331, 16))
        self.university = QComboBox(self.centralwidget)
        self.university.addItem("")
        self.university.addItem("")
        self.university.addItem("")
        self.university.addItem("")
        self.university.setObjectName(u"university")
        self.university.setGeometry(QRect(290, 200, 181, 26))
        self.university.setEditable(False)
        self.department = QComboBox(self.centralwidget)
        self.department.addItem("")
        self.department.addItem("")
        self.department.addItem("")
        self.department.addItem("")
        self.department.setObjectName(u"department")
        self.department.setGeometry(QRect(290, 240, 181, 26))
        self.year = QComboBox(self.centralwidget)
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(290, 280, 81, 26))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(390, 280, 81, 26))
        instDeptYearSemSelection.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(instDeptYearSemSelection)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        instDeptYearSemSelection.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(instDeptYearSemSelection)
        self.statusbar.setObjectName(u"statusbar")
        instDeptYearSemSelection.setStatusBar(self.statusbar)

        self.retranslateUi(instDeptYearSemSelection)

        self.university.setCurrentIndex(-1)
        self.department.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(instDeptYearSemSelection)
    # setupUi

    def retranslateUi(self, instDeptYearSemSelection):
        instDeptYearSemSelection.setWindowTitle(QCoreApplication.translate("instDeptYearSemSelection", u"MainWindow", None))
        self.myButton.setText(QCoreApplication.translate("instDeptYearSemSelection", u"Next", None))
        self.myLabel.setText(QCoreApplication.translate("instDeptYearSemSelection", u"App Name", None))
        self.label.setText(QCoreApplication.translate("instDeptYearSemSelection", u"Choose your institution, department, year and semester", None))
        self.label_2.setText(QCoreApplication.translate("instDeptYearSemSelection", u"Select your university, department, current year and semester", None))
        self.university.setItemText(0, QCoreApplication.translate("instDeptYearSemSelection", u"RUET", None))
        self.university.setItemText(1, QCoreApplication.translate("instDeptYearSemSelection", u"CUET", None))
        self.university.setItemText(2, QCoreApplication.translate("instDeptYearSemSelection", u"KUET", None))
        self.university.setItemText(3, QCoreApplication.translate("instDeptYearSemSelection", u"BUET", None))

        self.university.setCurrentText("")
        self.university.setPlaceholderText(QCoreApplication.translate("instDeptYearSemSelection", u"Select your University", None))
        self.department.setItemText(0, QCoreApplication.translate("instDeptYearSemSelection", u"CSE", None))
        self.department.setItemText(1, QCoreApplication.translate("instDeptYearSemSelection", u"EEE", None))
        self.department.setItemText(2, QCoreApplication.translate("instDeptYearSemSelection", u"CE", None))
        self.department.setItemText(3, QCoreApplication.translate("instDeptYearSemSelection", u"ME", None))

        self.department.setPlaceholderText(QCoreApplication.translate("instDeptYearSemSelection", u"Select your Department", None))
        self.year.setItemText(0, QCoreApplication.translate("instDeptYearSemSelection", u"1", None))
        self.year.setItemText(1, QCoreApplication.translate("instDeptYearSemSelection", u"2", None))
        self.year.setItemText(2, QCoreApplication.translate("instDeptYearSemSelection", u"3", None))
        self.year.setItemText(3, QCoreApplication.translate("instDeptYearSemSelection", u"4", None))

        self.year.setPlaceholderText(QCoreApplication.translate("instDeptYearSemSelection", u"Year", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("instDeptYearSemSelection", u"Odd", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("instDeptYearSemSelection", u"Even", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("instDeptYearSemSelection", u"Semester", None))
    # retranslateUi

