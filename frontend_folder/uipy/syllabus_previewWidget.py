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
        SyllabusPreview.resize(1184, 740)
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

        self.bodyFrame = QFrame(SyllabusPreview)
        self.bodyFrame.setObjectName(u"bodyFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.bodyFrame.sizePolicy().hasHeightForWidth())
        self.bodyFrame.setSizePolicy(sizePolicy1)
        self.bodyFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.bodyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bodyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bodyFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.bodyFrame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.bodyFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.gridFrame = QFrame(self.bodyFrame)
        self.gridFrame.setObjectName(u"gridFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(14)
        sizePolicy2.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_3.addWidget(self.gridFrame)


        self.verticalLayout_2.addWidget(self.bodyFrame, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame_6 = QFrame(SyllabusPreview)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_6.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.nextBtn = QPushButton(self.frame)
        self.nextBtn.setObjectName(u"nextBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy5)
        self.nextBtn.setMinimumSize(QSize(81, 26))
        self.nextBtn.setMaximumSize(QSize(81, 26))

        self.verticalLayout_8.addWidget(self.nextBtn)

        self.backBtn = QPushButton(self.frame)
        self.backBtn.setObjectName(u"backBtn")
        sizePolicy5.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy5)
        self.backBtn.setMinimumSize(QSize(81, 26))
        self.backBtn.setMaximumSize(QSize(81, 26))

        self.verticalLayout_8.addWidget(self.backBtn)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


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
        self.nextBtn.setText(QCoreApplication.translate("SyllabusPreview", u"Next", None))
        self.backBtn.setText(QCoreApplication.translate("SyllabusPreview", u"Back", None))
    # retranslateUi

