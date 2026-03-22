# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgotPasswordEnterCode.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_EnterCode(object):
    def setupUi(self, EnterCode):
        if not EnterCode.objectName():
            EnterCode.setObjectName(u"EnterCode")
        EnterCode.resize(835, 550)
        EnterCode.setStyleSheet(u"QWidget{background-color: rgb(37, 37, 29);}\n"
"QFrame{border: none;}")
        self.verticalLayout = QVBoxLayout(EnterCode)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(EnterCode)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignBottom)

        self.codeInputLineEdit = QLineEdit(EnterCode)
        self.codeInputLineEdit.setObjectName(u"codeInputLineEdit")

        self.verticalLayout.addWidget(self.codeInputLineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_2 = QFrame(EnterCode)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.nextBtn = QPushButton(self.frame_2)
        self.nextBtn.setObjectName(u"nextBtn")

        self.verticalLayout_3.addWidget(self.nextBtn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.backBtn = QPushButton(self.frame_2)
        self.backBtn.setObjectName(u"backBtn")

        self.verticalLayout_3.addWidget(self.backBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(EnterCode)

        QMetaObject.connectSlotsByName(EnterCode)
    # setupUi

    def retranslateUi(self, EnterCode):
        EnterCode.setWindowTitle(QCoreApplication.translate("EnterCode", u"Form", None))
        self.label.setText(QCoreApplication.translate("EnterCode", u"Forgot Password", None))
        self.label_2.setText(QCoreApplication.translate("EnterCode", u"Enter the verification code sent to the email", None))
        self.codeInputLineEdit.setPlaceholderText(QCoreApplication.translate("EnterCode", u"Code", None))
        self.nextBtn.setText(QCoreApplication.translate("EnterCode", u"Next", None))
        self.backBtn.setText(QCoreApplication.translate("EnterCode", u"Back", None))
    # retranslateUi

