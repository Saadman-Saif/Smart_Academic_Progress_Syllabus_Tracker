# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'onboarding.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

from sliding_stacked_widget import SlidingStackedWidget

class Ui_AppName(object):
    def setupUi(self, AppName):
        if not AppName.objectName():
            AppName.setObjectName(u"AppName")
        AppName.resize(800, 600)
        AppName.setStyleSheet(u"background-color: rgb(37, 37, 29);")
        self.centralwidget = QWidget(AppName)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = SlidingStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        # self.page = QWidget()
        # self.page.setObjectName(u"page")
        # self.stackedWidget.addWidget(self.page)
        # self.page_2 = QWidget()
        # self.page_2.setObjectName(u"page_2")
        # self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        AppName.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AppName)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        AppName.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AppName)
        self.statusbar.setObjectName(u"statusbar")
        AppName.setStatusBar(self.statusbar)

        self.retranslateUi(AppName)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(AppName)
    # setupUi

    def retranslateUi(self, AppName):
        AppName.setWindowTitle(QCoreApplication.translate("AppName", u"App Name", None))
    # retranslateUi

