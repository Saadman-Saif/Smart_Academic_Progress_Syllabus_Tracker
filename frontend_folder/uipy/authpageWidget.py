# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authpageWidget.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(832, 543)
        LoginScreen.setStyleSheet(u"background-color: rgb(37, 37, 29);")
        self.gridLayout = QGridLayout(LoginScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(LoginScreen)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        self.lineEdit.setFont(font1)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lineEdit_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.myButton = QPushButton(self.frame)
        self.myButton.setObjectName(u"myButton")
        sizePolicy2.setHeightForWidth(self.myButton.sizePolicy().hasHeightForWidth())
        self.myButton.setSizePolicy(sizePolicy2)
        self.myButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.myButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.frame_3 = QFrame(LoginScreen)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_7 = QLineEdit(self.frame_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy2.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy2)
        self.lineEdit_7.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_7.setFont(font1)
        self.lineEdit_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.lineEdit_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_8 = QLineEdit(self.frame_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy2.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy2)
        self.lineEdit_8.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_8.setFont(font1)
        self.lineEdit_8.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.lineEdit_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.myButton_4 = QPushButton(self.frame_3)
        self.myButton_4.setObjectName(u"myButton_4")
        sizePolicy2.setHeightForWidth(self.myButton_4.sizePolicy().hasHeightForWidth())
        self.myButton_4.setSizePolicy(sizePolicy2)
        self.myButton_4.setFont(font1)

        self.verticalLayout_5.addWidget(self.myButton_4, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.myLabel = QLabel(LoginScreen)
        self.myLabel.setObjectName(u"myLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.myLabel.sizePolicy().hasHeightForWidth())
        self.myLabel.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(22)
        font2.setBold(True)
        self.myLabel.setFont(font2)
        self.myLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout.addWidget(self.myLabel, 0, 0, 1, 2)

        self.frame_2 = QFrame(LoginScreen)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 2)


        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoginScreen", u"Log In", None))
        self.label_2.setText(QCoreApplication.translate("LoginScreen", u"Enter your email and password", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.myButton.setText(QCoreApplication.translate("LoginScreen", u"Log In", None))
        self.label_9.setText(QCoreApplication.translate("LoginScreen", u"<a href=\"authpageWidget\">Forgot password?</a>", None))
        self.label_7.setText(QCoreApplication.translate("LoginScreen", u"Sign Up", None))
        self.label_8.setText(QCoreApplication.translate("LoginScreen", u"Create your account", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.myButton_4.setText(QCoreApplication.translate("LoginScreen", u"Create", None))
        self.myLabel.setText(QCoreApplication.translate("LoginScreen", u"App Name", None))
    # retranslateUi

