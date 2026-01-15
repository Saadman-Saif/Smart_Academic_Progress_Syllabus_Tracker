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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(654, 398)
        HomePage.setStyleSheet(u"background-color: rgb(37, 37, 29);")
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
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("HomePage", u"Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("HomePage", u"Routine", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("HomePage", u"Syllabus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("HomePage", u"Overview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("HomePage", u"Study Session", None))
    # retranslateUi

