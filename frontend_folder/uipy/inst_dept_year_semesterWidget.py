# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inst_dept_year_semesterWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_instDeptYearSemSelection(object):
    def setupUi(self, instDeptYearSemSelection):
        if not instDeptYearSemSelection.objectName():
            instDeptYearSemSelection.setObjectName(u"instDeptYearSemSelection")
        instDeptYearSemSelection.resize(1128, 627)
        instDeptYearSemSelection.setStyleSheet(u"background-color: rgb(37, 37, 29);")
        self.verticalLayout = QVBoxLayout(instDeptYearSemSelection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.myLabel_2 = QLabel(instDeptYearSemSelection)
        self.myLabel_2.setObjectName(u"myLabel_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.myLabel_2.sizePolicy().hasHeightForWidth())
        self.myLabel_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(22)
        font.setBold(True)
        self.myLabel_2.setFont(font)
        self.myLabel_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout.addWidget(self.myLabel_2)

        self.frame = QFrame(instDeptYearSemSelection)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        self.label_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(4)
        self.yearComboBox = QComboBox(self.frame)
        self.yearComboBox.addItem("")
        self.yearComboBox.addItem("")
        self.yearComboBox.addItem("")
        self.yearComboBox.addItem("")
        self.yearComboBox.setObjectName(u"yearComboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.yearComboBox.sizePolicy().hasHeightForWidth())
        self.yearComboBox.setSizePolicy(sizePolicy3)
        self.yearComboBox.setMinimumSize(QSize(80, 26))
        self.yearComboBox.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_3.addWidget(self.yearComboBox, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.departmentComboBox = QComboBox(self.frame)
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.setObjectName(u"departmentComboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.departmentComboBox.sizePolicy().hasHeightForWidth())
        self.departmentComboBox.setSizePolicy(sizePolicy4)
        self.departmentComboBox.setMinimumSize(QSize(160, 0))
        self.departmentComboBox.setMaximumSize(QSize(160, 16777215))

        self.gridLayout_3.addWidget(self.departmentComboBox, 1, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.universityComboBox = QComboBox(self.frame)
        self.universityComboBox.addItem("")
        self.universityComboBox.addItem("")
        self.universityComboBox.addItem("")
        self.universityComboBox.addItem("")
        self.universityComboBox.setObjectName(u"universityComboBox")
        sizePolicy4.setHeightForWidth(self.universityComboBox.sizePolicy().hasHeightForWidth())
        self.universityComboBox.setSizePolicy(sizePolicy4)
        self.universityComboBox.setMinimumSize(QSize(160, 0))
        self.universityComboBox.setMaximumSize(QSize(160, 16777215))
        self.universityComboBox.setEditable(False)

        self.gridLayout_3.addWidget(self.universityComboBox, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.semesterComboBox = QComboBox(self.frame)
        self.semesterComboBox.addItem("")
        self.semesterComboBox.addItem("")
        self.semesterComboBox.setObjectName(u"semesterComboBox")
        sizePolicy3.setHeightForWidth(self.semesterComboBox.sizePolicy().hasHeightForWidth())
        self.semesterComboBox.setSizePolicy(sizePolicy3)
        self.semesterComboBox.setMinimumSize(QSize(80, 26))
        self.semesterComboBox.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_3.addWidget(self.semesterComboBox, 2, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.nextBtn = QPushButton(self.frame)
        self.nextBtn.setObjectName(u"nextBtn")
        sizePolicy3.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.nextBtn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.backBtn = QPushButton(self.frame)
        self.backBtn.setObjectName(u"backBtn")
        sizePolicy3.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.backBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame_2 = QFrame(instDeptYearSemSelection)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(instDeptYearSemSelection)

        self.departmentComboBox.setCurrentIndex(-1)
        self.universityComboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(instDeptYearSemSelection)
    # setupUi

    def retranslateUi(self, instDeptYearSemSelection):
        instDeptYearSemSelection.setWindowTitle(QCoreApplication.translate("instDeptYearSemSelection", u"Form", None))
        self.myLabel_2.setText(QCoreApplication.translate("instDeptYearSemSelection", u"App Name", None))
        self.label.setText(QCoreApplication.translate("instDeptYearSemSelection", u"Choose your institution, department, year and semester", None))
        self.label_2.setText(QCoreApplication.translate("instDeptYearSemSelection", u"Select your university, department, current year and semester", None))
        self.yearComboBox.setItemText(0, QCoreApplication.translate("instDeptYearSemSelection", u"1", None))
        self.yearComboBox.setItemText(1, QCoreApplication.translate("instDeptYearSemSelection", u"2", None))
        self.yearComboBox.setItemText(2, QCoreApplication.translate("instDeptYearSemSelection", u"3", None))
        self.yearComboBox.setItemText(3, QCoreApplication.translate("instDeptYearSemSelection", u"4", None))

        self.yearComboBox.setPlaceholderText(QCoreApplication.translate("instDeptYearSemSelection", u"Year", None))
        self.departmentComboBox.setItemText(0, QCoreApplication.translate("instDeptYearSemSelection", u"CSE", None))
        self.departmentComboBox.setItemText(1, QCoreApplication.translate("instDeptYearSemSelection", u"EEE", None))
        self.departmentComboBox.setItemText(2, QCoreApplication.translate("instDeptYearSemSelection", u"CE", None))
        self.departmentComboBox.setItemText(3, QCoreApplication.translate("instDeptYearSemSelection", u"ME", None))

        self.departmentComboBox.setPlaceholderText(QCoreApplication.translate("instDeptYearSemSelection", u"Department", None))
        self.universityComboBox.setItemText(0, QCoreApplication.translate("instDeptYearSemSelection", u"RUET", None))
        self.universityComboBox.setItemText(1, QCoreApplication.translate("instDeptYearSemSelection", u"CUET", None))
        self.universityComboBox.setItemText(2, QCoreApplication.translate("instDeptYearSemSelection", u"KUET", None))
        self.universityComboBox.setItemText(3, QCoreApplication.translate("instDeptYearSemSelection", u"BUET", None))

        self.universityComboBox.setCurrentText("")
        self.universityComboBox.setPlaceholderText(QCoreApplication.translate("instDeptYearSemSelection", u"University", None))
        self.semesterComboBox.setItemText(0, QCoreApplication.translate("instDeptYearSemSelection", u"Odd", None))
        self.semesterComboBox.setItemText(1, QCoreApplication.translate("instDeptYearSemSelection", u"Even", None))

        self.semesterComboBox.setPlaceholderText(QCoreApplication.translate("instDeptYearSemSelection", u"Semester", None))
        self.nextBtn.setText(QCoreApplication.translate("instDeptYearSemSelection", u"Next", None))
        self.backBtn.setText(QCoreApplication.translate("instDeptYearSemSelection", u"Back", None))
    # retranslateUi

