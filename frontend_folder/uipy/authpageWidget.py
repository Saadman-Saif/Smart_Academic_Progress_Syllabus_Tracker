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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(832, 543)
        LoginScreen.setStyleSheet(u"background-color: rgb(37, 37, 29);")
        self.gridLayout = QGridLayout(LoginScreen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.loginFrame = QFrame(LoginScreen)
        self.loginFrame.setObjectName(u"loginFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.loginFrame.sizePolicy().hasHeightForWidth())
        self.loginFrame.setSizePolicy(sizePolicy)
        self.loginFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.loginFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.loginFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.loginFrame)
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

        self.label_2 = QLabel(self.loginFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.login_email_lineedit = QLineEdit(self.loginFrame)
        self.login_email_lineedit.setObjectName(u"login_email_lineedit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.login_email_lineedit.sizePolicy().hasHeightForWidth())
        self.login_email_lineedit.setSizePolicy(sizePolicy2)
        self.login_email_lineedit.setMaximumSize(QSize(300, 16777215))
        self.login_email_lineedit.setFont(font1)
        self.login_email_lineedit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.login_email_lineedit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.login_password_lineedit = QLineEdit(self.loginFrame)
        self.login_password_lineedit.setObjectName(u"login_password_lineedit")
        sizePolicy2.setHeightForWidth(self.login_password_lineedit.sizePolicy().hasHeightForWidth())
        self.login_password_lineedit.setSizePolicy(sizePolicy2)
        self.login_password_lineedit.setMaximumSize(QSize(300, 16777215))
        self.login_password_lineedit.setFont(font1)
        self.login_password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_password_lineedit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.login_password_lineedit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.login_btn = QPushButton(self.loginFrame)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy2.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy2)
        self.login_btn.setFont(font1)

        self.verticalLayout_2.addWidget(self.login_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.forgot_password_label = QLabel(self.loginFrame)
        self.forgot_password_label.setObjectName(u"forgot_password_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.forgot_password_label.sizePolicy().hasHeightForWidth())
        self.forgot_password_label.setSizePolicy(sizePolicy3)
        self.forgot_password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.forgot_password_label.setOpenExternalLinks(False)

        self.verticalLayout_2.addWidget(self.forgot_password_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.signupLinkLabel = QLabel(self.loginFrame)
        self.signupLinkLabel.setObjectName(u"signupLinkLabel")
        sizePolicy3.setHeightForWidth(self.signupLinkLabel.sizePolicy().hasHeightForWidth())
        self.signupLinkLabel.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(11)
        self.signupLinkLabel.setFont(font2)

        self.verticalLayout_2.addWidget(self.signupLinkLabel, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.loginFrame, 1, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.signupFrame = QFrame(LoginScreen)
        self.signupFrame.setObjectName(u"signupFrame")
        sizePolicy.setHeightForWidth(self.signupFrame.sizePolicy().hasHeightForWidth())
        self.signupFrame.setSizePolicy(sizePolicy)
        self.signupFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.signupFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.signupFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.signupFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.signupFrame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_8 = QLabel(self.signupFrame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.signup_username_lineedit = QLineEdit(self.signupFrame)
        self.signup_username_lineedit.setObjectName(u"signup_username_lineedit")
        sizePolicy2.setHeightForWidth(self.signup_username_lineedit.sizePolicy().hasHeightForWidth())
        self.signup_username_lineedit.setSizePolicy(sizePolicy2)
        self.signup_username_lineedit.setMaximumSize(QSize(300, 16777215))
        self.signup_username_lineedit.setFont(font1)
        self.signup_username_lineedit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.signup_username_lineedit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.signup_email_lineedit = QLineEdit(self.signupFrame)
        self.signup_email_lineedit.setObjectName(u"signup_email_lineedit")
        sizePolicy2.setHeightForWidth(self.signup_email_lineedit.sizePolicy().hasHeightForWidth())
        self.signup_email_lineedit.setSizePolicy(sizePolicy2)
        self.signup_email_lineedit.setMaximumSize(QSize(300, 16777215))
        self.signup_email_lineedit.setFont(font1)
        self.signup_email_lineedit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.signup_email_lineedit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.signup_password_lineedit = QLineEdit(self.signupFrame)
        self.signup_password_lineedit.setObjectName(u"signup_password_lineedit")
        sizePolicy2.setHeightForWidth(self.signup_password_lineedit.sizePolicy().hasHeightForWidth())
        self.signup_password_lineedit.setSizePolicy(sizePolicy2)
        self.signup_password_lineedit.setMaximumSize(QSize(300, 16777215))
        self.signup_password_lineedit.setFont(font1)
        self.signup_password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.signup_password_lineedit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.signup_password_lineedit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.signup_btn = QPushButton(self.signupFrame)
        self.signup_btn.setObjectName(u"signup_btn")
        sizePolicy2.setHeightForWidth(self.signup_btn.sizePolicy().hasHeightForWidth())
        self.signup_btn.setSizePolicy(sizePolicy2)
        self.signup_btn.setFont(font1)

        self.verticalLayout_5.addWidget(self.signup_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.backToLoginBtn = QPushButton(self.signupFrame)
        self.backToLoginBtn.setObjectName(u"backToLoginBtn")
        sizePolicy1.setHeightForWidth(self.backToLoginBtn.sizePolicy().hasHeightForWidth())
        self.backToLoginBtn.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.backToLoginBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.signupFrame, 1, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.myLabel = QLabel(LoginScreen)
        self.myLabel.setObjectName(u"myLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.myLabel.sizePolicy().hasHeightForWidth())
        self.myLabel.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(22)
        font3.setBold(True)
        self.myLabel.setFont(font3)
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
        self.login_email_lineedit.setText("")
        self.login_email_lineedit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Email", None))
        self.login_password_lineedit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.login_btn.setText(QCoreApplication.translate("LoginScreen", u"Log In", None))
        self.forgot_password_label.setText(QCoreApplication.translate("LoginScreen", u"<a href=\"authpageWidget\">Forgot password?</a>", None))
        self.signupLinkLabel.setText(QCoreApplication.translate("LoginScreen", u"Don't have an account? <a href=\"authpageWidget\">Sign Up</a>", None))
        self.label_7.setText(QCoreApplication.translate("LoginScreen", u"Sign Up", None))
        self.label_8.setText(QCoreApplication.translate("LoginScreen", u"Create your account", None))
        self.signup_username_lineedit.setText("")
        self.signup_username_lineedit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.signup_email_lineedit.setText("")
        self.signup_email_lineedit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Email", None))
        self.signup_password_lineedit.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.signup_btn.setText(QCoreApplication.translate("LoginScreen", u"Sign Up", None))
        self.backToLoginBtn.setText(QCoreApplication.translate("LoginScreen", u"Back to Login", None))
        self.myLabel.setText(QCoreApplication.translate("LoginScreen", u"App Name", None))
    # retranslateUi

