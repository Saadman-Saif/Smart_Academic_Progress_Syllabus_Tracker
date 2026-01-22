# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepageWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QProgressBar, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

from shadow_frame import ShadowFrame

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(1061, 597)
        HomePage.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color: rgb(37, 37, 29);\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid #777777;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"	color: #000000;\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #cccc00;\n"
"    border-radius: 4px;\n"
"}")
        self.verticalLayout = QVBoxLayout(HomePage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(HomePage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tabWidget.setStyleSheet(u"QTabBar::tab:!selected:hover\n"
"{\n"
"	color: #aaaaaa;\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"	padding-right: 10px;\n"
"}\n"
"QTabBar::tab:!selected\n"
"{\n"
"    font-size: 16px;\n"
"    font-family: 'Inter';\n"
"    color: #777777;\n"
"	padding-top: 12px;\n"
"	padding-bottom: 0px;\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    font: 600 9pt \"Inter\";\n"
"    font-size: 32px;\n"
"    color: #FFFF00;\n"
"}\n"
"QTabWidget::pane, QTabBar::tab\n"
"{\n"
"    background-color: rgb(37, 37, 29);\n"
"    border: none;\n"
"}")
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.homeTab = QWidget()
        self.homeTab.setObjectName(u"homeTab")
        self.frame_2 = QFrame(self.homeTab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(520, 10, 501, 231))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 10, 289, 20))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(100, 40, 91, 151))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.homeTab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(120, 280, 611, 211))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4 = ShadowFrame(self.homeTab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 501, 231))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{border: none;}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Orientation.Vertical)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar)

        self.progressBar_2 = QProgressBar(self.frame)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)
        self.progressBar_2.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar_2)

        self.progressBar_3 = QProgressBar(self.frame)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(24)
        self.progressBar_3.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_3.setInvertedAppearance(False)
        self.progressBar_3.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar_3)

        self.progressBar_4 = QProgressBar(self.frame)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setValue(24)
        self.progressBar_4.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_4.setInvertedAppearance(False)
        self.progressBar_4.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar_4)

        self.progressBar_5 = QProgressBar(self.frame)
        self.progressBar_5.setObjectName(u"progressBar_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_5.sizePolicy().hasHeightForWidth())
        self.progressBar_5.setSizePolicy(sizePolicy)
        self.progressBar_5.setValue(24)
        self.progressBar_5.setTextVisible(True)
        self.progressBar_5.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_5.setInvertedAppearance(False)
        self.progressBar_5.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar_5)


        self.verticalLayout_2.addWidget(self.frame)

        self.tabWidget.addTab(self.homeTab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(HomePage)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("HomePage", u"CT Average", None))
        self.label.setText(QCoreApplication.translate("HomePage", u"Syllabus Completion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), QCoreApplication.translate("HomePage", u"Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("HomePage", u"Routine", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("HomePage", u"Syllabus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("HomePage", u"Overview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("HomePage", u"Study Session", None))
    # retranslateUi

