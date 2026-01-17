# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'syllabus_previewWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SyllabusPreview(object):
    def setupUi(self, SyllabusPreview):
        if not SyllabusPreview.objectName():
            SyllabusPreview.setObjectName(u"SyllabusPreview")
        SyllabusPreview.resize(1017, 740)
        SyllabusPreview.setStyleSheet(u"background-color: rgb(37, 37, 29);")
        self.verticalLayout_2 = QVBoxLayout(SyllabusPreview)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.myLabel = QLabel(SyllabusPreview)
        self.myLabel.setObjectName(u"myLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.myLabel.sizePolicy().hasHeightForWidth())
        self.myLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(22)
        font.setBold(True)
        self.myLabel.setFont(font)
        self.myLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addWidget(self.myLabel)

        self.frame_7 = QFrame(SyllabusPreview)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.gridFrame = QFrame(self.frame_7)
        self.gridFrame.setObjectName(u"gridFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(14)
        sizePolicy2.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.gridFrame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setMinimumSize(QSize(188, 359))
        self.frame_5.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_5, 1, 6, 1, 1)

        self.frame_2 = QFrame(self.gridFrame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMinimumSize(QSize(188, 359))
        self.frame_2.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_2, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.gridFrame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(188, 359))
        self.frame_4.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_4, 1, 5, 1, 1)

        self.frame_3 = QFrame(self.gridFrame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(187, 359))
        self.frame_3.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_3, 1, 4, 1, 1)

        self.CSE2101 = QFrame(self.gridFrame)
        self.CSE2101.setObjectName(u"CSE2101")
        sizePolicy3.setHeightForWidth(self.CSE2101.sizePolicy().hasHeightForWidth())
        self.CSE2101.setSizePolicy(sizePolicy3)
        self.CSE2101.setMinimumSize(QSize(188, 359))
        self.CSE2101.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.CSE2101.setFrameShape(QFrame.Shape.StyledPanel)
        self.CSE2101.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.CSE2101)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.CSE2101)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(203, 51))
        self.header.setMaximumSize(QSize(203, 51))
        self.header.setStyleSheet(u"background-color: rgb(75, 75, 75)")
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.header)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1, 1, 71, 20))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.header)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1, 27, 114, 16))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.header)

        self.frame = QFrame(self.CSE2101)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setStyleSheet(u"background-color: rgb(60, 60, 60)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 10, 161, 16))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 40, 49, 16))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 70, 81, 16))
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 110, 111, 16))
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 140, 144, 16))

        self.verticalLayout.addWidget(self.frame)


        self.gridLayout.addWidget(self.CSE2101, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.gridFrame)

        self.nextBtn = QPushButton(self.frame_7)
        self.nextBtn.setObjectName(u"nextBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.nextBtn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.backBtn = QPushButton(self.frame_7)
        self.backBtn.setObjectName(u"backBtn")
        sizePolicy5.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.backBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame_6 = QFrame(SyllabusPreview)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame_6)


        self.retranslateUi(SyllabusPreview)

        QMetaObject.connectSlotsByName(SyllabusPreview)
    # setupUi

    def retranslateUi(self, SyllabusPreview):
        SyllabusPreview.setWindowTitle(QCoreApplication.translate("SyllabusPreview", u"Form", None))
        self.myLabel.setText(QCoreApplication.translate("SyllabusPreview", u"App Name", None))
        self.label.setText(QCoreApplication.translate("SyllabusPreview", u"Theory Courses and Syllabus", None))
        self.label_2.setText(QCoreApplication.translate("SyllabusPreview", u"Preview of the theory courses and their syllabus included in your selected semester.\n"
"You can edit these later.", None))
        self.label_4.setText(QCoreApplication.translate("SyllabusPreview", u"CSE 2101", None))
        self.label_5.setText(QCoreApplication.translate("SyllabusPreview", u"Discrete Mathematics", None))
        self.label_3.setText(QCoreApplication.translate("SyllabusPreview", u"Logic and Proof", None))
        self.label_6.setText(QCoreApplication.translate("SyllabusPreview", u"Set", None))
        self.label_7.setText(QCoreApplication.translate("SyllabusPreview", u"Function", None))
        self.label_8.setText(QCoreApplication.translate("SyllabusPreview", u"Cardinality of Sets", None))
        self.label_9.setText(QCoreApplication.translate("SyllabusPreview", u"Sequences and Summation", None))
        self.nextBtn.setText(QCoreApplication.translate("SyllabusPreview", u"Next", None))
        self.backBtn.setText(QCoreApplication.translate("SyllabusPreview", u"Back", None))
    # retranslateUi

