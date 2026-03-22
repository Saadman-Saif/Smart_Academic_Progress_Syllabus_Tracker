# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepageWidgetcards.ui'
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
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

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
        self.progressBar = QProgressBar(self.progressBarsFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Orientation.Vertical)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar)

        self.progressBar_2 = QProgressBar(self.progressBarsFrame)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)
        self.progressBar_2.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar_2)

        self.progressBar_3 = QProgressBar(self.progressBarsFrame)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(24)
        self.progressBar_3.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_3.setInvertedAppearance(False)
        self.progressBar_3.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar_3)

        self.progressBar_4 = QProgressBar(self.progressBarsFrame)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setValue(24)
        self.progressBar_4.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_4.setInvertedAppearance(False)
        self.progressBar_4.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar_4)

        self.progressBar_5 = QProgressBar(self.progressBarsFrame)
        self.progressBar_5.setObjectName(u"progressBar_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar_5.sizePolicy().hasHeightForWidth())
        self.progressBar_5.setSizePolicy(sizePolicy2)
        self.progressBar_5.setValue(24)
        self.progressBar_5.setTextVisible(True)
        self.progressBar_5.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_5.setInvertedAppearance(False)
        self.progressBar_5.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar_5)


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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
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
        self.cardFrame = QFrame(self.cardsFrame)
        self.cardFrame.setObjectName(u"cardFrame")
        self.cardFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.cardFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.courseCodeLabel = QLabel(self.cardFrame)
        self.courseCodeLabel.setObjectName(u"courseCodeLabel")
        sizePolicy3.setHeightForWidth(self.courseCodeLabel.sizePolicy().hasHeightForWidth())
        self.courseCodeLabel.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.courseCodeLabel.setFont(font2)
        self.courseCodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.courseCodeLabel)

        self.markLabel = QLabel(self.cardFrame)
        self.markLabel.setObjectName(u"markLabel")
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(48)
        font3.setBold(True)
        self.markLabel.setFont(font3)
        self.markLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.markLabel)

        self.ct1Label = QLabel(self.cardFrame)
        self.ct1Label.setObjectName(u"ct1Label")
        font4 = QFont()
        font4.setFamilies([u"Inter"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.ct1Label.setFont(font4)
        self.ct1Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.ct1Label)

        self.ct2Label = QLabel(self.cardFrame)
        self.ct2Label.setObjectName(u"ct2Label")
        self.ct2Label.setFont(font4)
        self.ct2Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.ct2Label)

        self.ct3Label = QLabel(self.cardFrame)
        self.ct3Label.setObjectName(u"ct3Label")
        self.ct3Label.setFont(font4)
        self.ct3Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.ct3Label)

        self.ct4Label = QLabel(self.cardFrame)
        self.ct4Label.setObjectName(u"ct4Label")
        self.ct4Label.setFont(font4)
        self.ct4Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.ct4Label)


        self.horizontalLayout_4.addWidget(self.cardFrame)

        self.frame = QFrame(self.cardsFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.cardsFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.cardsFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.cardsFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.cardsFrame)


        self.gridLayout.addWidget(self.ctAvgFrame, 1, 1, 1, 1)

        self.weeklyReportFrame = QFrame(self.homeTab)
        self.weeklyReportFrame.setObjectName(u"weeklyReportFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.weeklyReportFrame.sizePolicy().hasHeightForWidth())
        self.weeklyReportFrame.setSizePolicy(sizePolicy4)
        self.weeklyReportFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.weeklyReportFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.weeklyReportFrame, 2, 0, 1, 2)

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
        self.horizontalLayout_2 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timerPanel = QFrame(self.tab_7)
        self.timerPanel.setObjectName(u"timerPanel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.timerPanel.sizePolicy().hasHeightForWidth())
        self.timerPanel.setSizePolicy(sizePolicy5)
        self.timerPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.timerPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.timerPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, -1, 20, 20)
        self.timerLabel = QLabel(self.timerPanel)
        self.timerLabel.setObjectName(u"timerLabel")
        sizePolicy.setHeightForWidth(self.timerLabel.sizePolicy().hasHeightForWidth())
        self.timerLabel.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamilies([u"Geist Mono"])
        font5.setPointSize(72)
        font5.setKerning(False)
        self.timerLabel.setFont(font5)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(2)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.topicsPanel.sizePolicy().hasHeightForWidth())
        self.topicsPanel.setSizePolicy(sizePolicy6)
        self.topicsPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.topicsPanel.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.topicsPanel)

        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(HomePage)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"Form", None))
        self.welcomeUserLabel.setText(QCoreApplication.translate("HomePage", u"Welcome, ", None))
        self.label.setText(QCoreApplication.translate("HomePage", u"Syllabus Completion", None))
        self.label_2.setText(QCoreApplication.translate("HomePage", u"CT Average", None))
        self.courseCodeLabel.setText(QCoreApplication.translate("HomePage", u"CSE 2201", None))
        self.markLabel.setText(QCoreApplication.translate("HomePage", u"99", None))
        self.ct1Label.setText(QCoreApplication.translate("HomePage", u"CT1: 99", None))
        self.ct2Label.setText(QCoreApplication.translate("HomePage", u"CT1: 99", None))
        self.ct3Label.setText(QCoreApplication.translate("HomePage", u"CT1: 99", None))
        self.ct4Label.setText(QCoreApplication.translate("HomePage", u"CT1: 99", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), QCoreApplication.translate("HomePage", u"Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("HomePage", u"Routine", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("HomePage", u"Syllabus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("HomePage", u"Overview", None))
        self.timerLabel.setText(QCoreApplication.translate("HomePage", u"<html><head/><body><p>0<span style=\" font-size:24pt;\">hr   </span>0<span style=\" font-size:24pt;\">min </span>0<span style=\" font-size:24pt;\">sec</span></p></body></html>", None))
        self.playBtn.setText("")
        self.pauseBtn.setText("")
        self.stopBtn.setText("")
        self.resetBtn.setText("")
        self.saveSessionBtn.setText(QCoreApplication.translate("HomePage", u"Save Session", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("HomePage", u"Study Session", None))
    # retranslateUi

