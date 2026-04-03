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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

from shadow_frame import ShadowFrame

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(1328, 667)
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
        self.gridLayout = QGridLayout(self.homeTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.welcomeUserLabel = QLabel(self.homeTab)
        self.welcomeUserLabel.setObjectName(u"welcomeUserLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeUserLabel.sizePolicy().hasHeightForWidth())
        self.welcomeUserLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(24)
        font.setBold(True)
        self.welcomeUserLabel.setFont(font)

        self.gridLayout.addWidget(self.welcomeUserLabel, 0, 0, 1, 1)

        self.syllabusCompletionFrame = ShadowFrame(self.homeTab)
        self.syllabusCompletionFrame.setObjectName(u"syllabusCompletionFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.syllabusCompletionFrame.sizePolicy().hasHeightForWidth())
        self.syllabusCompletionFrame.setSizePolicy(sizePolicy1)
        self.syllabusCompletionFrame.setMaximumSize(QSize(16777215, 271))
        self.syllabusCompletionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.syllabusCompletionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.syllabusCompletionFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.syllabusCompletionFrame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.progressBarsFrame = QFrame(self.syllabusCompletionFrame)
        self.progressBarsFrame.setObjectName(u"progressBarsFrame")
        self.progressBarsFrame.setStyleSheet(u"QFrame{border: none;}")
        self.progressBarsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.progressBarsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.progressBarsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_2.addWidget(self.progressBarsFrame)


        self.gridLayout.addWidget(self.syllabusCompletionFrame, 1, 0, 1, 1)

        self.ctAvgFrame = QFrame(self.homeTab)
        self.ctAvgFrame.setObjectName(u"ctAvgFrame")
        sizePolicy1.setHeightForWidth(self.ctAvgFrame.sizePolicy().hasHeightForWidth())
        self.ctAvgFrame.setSizePolicy(sizePolicy1)
        self.ctAvgFrame.setMinimumSize(QSize(643, 271))
        self.ctAvgFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ctAvgFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ctAvgFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.ctAvgFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.cardsFrame = QFrame(self.ctAvgFrame)
        self.cardsFrame.setObjectName(u"cardsFrame")
        self.cardsFrame.setStyleSheet(u"QFrame#cardsFrame{border:none;}")
        self.cardsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.cardsFrame)


        self.gridLayout.addWidget(self.ctAvgFrame, 1, 1, 1, 1)

        self.weeklyReportFrame = QFrame(self.homeTab)
        self.weeklyReportFrame.setObjectName(u"weeklyReportFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.weeklyReportFrame.sizePolicy().hasHeightForWidth())
        self.weeklyReportFrame.setSizePolicy(sizePolicy3)
        self.weeklyReportFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.weeklyReportFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.weeklyReportFrame, 2, 0, 1, 2)

        self.tabWidget.addTab(self.homeTab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_5 = QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.courseSyllabusTabWidget = QTabWidget(self.tab_5)
        self.courseSyllabusTabWidget.setObjectName(u"courseSyllabusTabWidget")

        self.verticalLayout_5.addWidget(self.courseSyllabusTabWidget)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timerPanel = QFrame(self.tab_7)
        self.timerPanel.setObjectName(u"timerPanel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.timerPanel.sizePolicy().hasHeightForWidth())
        self.timerPanel.setSizePolicy(sizePolicy4)
        self.timerPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.timerPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.timerPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, -1, 20, 20)
        self.timerLabel = QLabel(self.timerPanel)
        self.timerLabel.setObjectName(u"timerLabel")
        sizePolicy.setHeightForWidth(self.timerLabel.sizePolicy().hasHeightForWidth())
        self.timerLabel.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Geist Mono"])
        font2.setPointSize(72)
        font2.setKerning(False)
        self.timerLabel.setFont(font2)
        self.timerLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.timerLabel.setMargin(0)

        self.verticalLayout_3.addWidget(self.timerLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.timerControlsFrame = QFrame(self.timerPanel)
        self.timerControlsFrame.setObjectName(u"timerControlsFrame")
        self.timerControlsFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"}")
        self.timerControlsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.timerControlsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.timerControlsFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.playBtn = QPushButton(self.timerControlsFrame)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setMinimumSize(QSize(60, 60))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.playBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.playBtn)

        self.pauseBtn = QPushButton(self.timerControlsFrame)
        self.pauseBtn.setObjectName(u"pauseBtn")
        self.pauseBtn.setMinimumSize(QSize(60, 60))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.pauseBtn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pauseBtn)

        self.stopBtn = QPushButton(self.timerControlsFrame)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setMinimumSize(QSize(60, 60))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.stopBtn.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.stopBtn)

        self.resetBtn = QPushButton(self.timerControlsFrame)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setMinimumSize(QSize(60, 60))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRestore))
        self.resetBtn.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.resetBtn)


        self.verticalLayout_3.addWidget(self.timerControlsFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.saveSessionBtn = QPushButton(self.timerPanel)
        self.saveSessionBtn.setObjectName(u"saveSessionBtn")

        self.verticalLayout_3.addWidget(self.saveSessionBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_2.addWidget(self.timerPanel)

        self.topicsPanel = QFrame(self.tab_7)
        self.topicsPanel.setObjectName(u"topicsPanel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.topicsPanel.sizePolicy().hasHeightForWidth())
        self.topicsPanel.setSizePolicy(sizePolicy5)
        self.topicsPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.topicsPanel.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.topicsPanel)

        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(HomePage)

        self.tabWidget.setCurrentIndex(2)
        self.courseSyllabusTabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"Form", None))
        self.welcomeUserLabel.setText(QCoreApplication.translate("HomePage", u"Welcome, ", None))
        self.label.setText(QCoreApplication.translate("HomePage", u"Syllabus Completion", None))
        self.label_2.setText(QCoreApplication.translate("HomePage", u"CT Average", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), QCoreApplication.translate("HomePage", u"Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("HomePage", u"Syllabus", None))
        self.timerLabel.setText(QCoreApplication.translate("HomePage", u"<html><head/><body><p>0<span style=\" font-size:24pt;\">hr   </span>0<span style=\" font-size:24pt;\">min </span>0<span style=\" font-size:24pt;\">sec</span></p></body></html>", None))
        self.playBtn.setText("")
        self.pauseBtn.setText("")
        self.stopBtn.setText("")
        self.resetBtn.setText("")
        self.saveSessionBtn.setText(QCoreApplication.translate("HomePage", u"Save Session", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("HomePage", u"Study Session", None))
    # retranslateUi

