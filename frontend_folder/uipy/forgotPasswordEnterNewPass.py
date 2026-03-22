# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgotPasswordEnterNewPass.ui'
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

class Ui_EnterNewPass(object):
    def setupUi(self, EnterNewPass):
        if not EnterNewPass.objectName():
            EnterNewPass.setObjectName(u"EnterNewPass")
        EnterNewPass.resize(835, 550)
        EnterNewPass.setStyleSheet(u"QWidget{background-color: rgb(37, 37, 29);}\n"
"QFrame{border: none;}")
        self.verticalLayout = QVBoxLayout(EnterNewPass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(EnterNewPass)
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

        self.newPassLineEdit = QLineEdit(EnterNewPass)
        self.newPassLineEdit.setObjectName(u"newPassLineEdit")

        self.verticalLayout.addWidget(self.newPassLineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.confirmPassLineEdit = QLineEdit(EnterNewPass)
        self.confirmPassLineEdit.setObjectName(u"confirmPassLineEdit")

        self.verticalLayout.addWidget(self.confirmPassLineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_2 = QFrame(EnterNewPass)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.saveBtn = QPushButton(self.frame_2)
        self.saveBtn.setObjectName(u"saveBtn")

        self.verticalLayout_3.addWidget(self.saveBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.backBtn = QPushButton(self.frame_2)
        self.backBtn.setObjectName(u"backBtn")

        self.verticalLayout_3.addWidget(self.backBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(EnterNewPass)

        QMetaObject.connectSlotsByName(EnterNewPass)
    # setupUi

    def retranslateUi(self, EnterNewPass):
        EnterNewPass.setWindowTitle(QCoreApplication.translate("EnterNewPass", u"Form", None))
        self.label.setText(QCoreApplication.translate("EnterNewPass", u"Forgot Password", None))
        self.label_2.setText(QCoreApplication.translate("EnterNewPass", u"Create a new password", None))
        self.newPassLineEdit.setPlaceholderText(QCoreApplication.translate("EnterNewPass", u"New Password", None))
        self.confirmPassLineEdit.setPlaceholderText(QCoreApplication.translate("EnterNewPass", u"Confirm Password", None))
        self.saveBtn.setText(QCoreApplication.translate("EnterNewPass", u"Save", None))
        self.backBtn.setText(QCoreApplication.translate("EnterNewPass", u"Back", None))
    # retranslateUi

