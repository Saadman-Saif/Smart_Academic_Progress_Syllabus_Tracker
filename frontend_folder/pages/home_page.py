from PySide6.QtWidgets import (QProgressBar, QWidget, QDialog, QPushButton, QVBoxLayout, QLabel)
from PySide6.QtCore import (Qt, Signal)

from uipy.homepageWidget import Ui_HomePage
from components.study_timer import StudyTimerScreen
from components.ct_average_card import CTAverageCard
from components.syllabus_tab import SyllabusTabWrap
from dialogs.edit_marks_dialog import EditMarksDialog

class HomePageWrap(QWidget):
    sendUpdatedMarks = Signal(str, list)
    loadCTMarks = Signal(str)
    themeToggledRelay = Signal()
    # topicDeletedRelay = Signal(int) 
    # topicAddedRelay = Signal(int, str)
    progressUpdatedRelay = Signal(int, bool)
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        # self.build_dynamic_cards()
        self.active_course_tabs = []

        # --- THE CORNER WIDGET MAGIC ---
        self.theme_toggle_btn = QPushButton("☀️ Light Mode")
        self.theme_toggle_btn.setFixedSize(120, 30)
        self.theme_toggle_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.theme_toggle_btn.setStyleSheet("""
            QPushButton {
                background-color: #444444; 
                color: white; 
                border-radius: 4px;
                margin-right: 20px; /* Keeps it from touching the edge of the screen */
            }
        """)
        
        # Inject it into the top-right corner of the Tab Widget!
        self.ui.tabWidget.setCornerWidget(self.theme_toggle_btn, Qt.Corner.TopRightCorner)
        
        # Wire it up to the relay
        self.theme_toggle_btn.clicked.connect(self.themeToggledRelay.emit)

        self.avgMark = 0
        self.allMarks = []
        self.timerScreenInstance = StudyTimerScreen(parent=self)
        # self.syllabusTabInstance = CourseTabWidget(parent=self)
        self.syllabus_tab = SyllabusTabWrap()
        self.ui.courseSyllabusTabWidget.addTab(self.syllabus_tab, "Test")

    def build_dynamic_cards(self, course, avgMarks, allMarks):
        # avgMarks = {"CSE 2201": 16, 
        #             "CSE 2203": 15, 
        #             "CSE 2205": 19, 
        #             "HUM 2213": 13,
        #             "Math 2213": 17}
        # allMarks = {"CSE 2201": [16, 15, 17], 
        #             "CSE 2203": [15, 15, 15, 15], 
        #             "CSE 2205": [20, 18], 
        #             "HUM 2213": [10, 13, 16],
        #             "Math 2213": [16, 18, 17]}

        # GET MARKS FROM BACKEND, CONNECT THEM QUICKLYYYYYYY
        # for course in avgMarks:
        custom_card = CTAverageCard(
            course_name=course, 
            avg_mark=avgMarks, 
            ct_marks=allMarks
        )
        
        custom_card.cardClicked.connect(self.handle_card_clicked)
        
        self.ui.horizontalLayout_4.addWidget(custom_card)

    def set_avgMark(self, mark):
        self.avgMark = mark

    def handle_card_clicked(self, courseName):
        print("Card clicked successfully!")
        dialog = EditMarksDialog(course_name=courseName) 
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            ct1, ct2, ct3, ct4 = dialog.get_new_marks()
            print(f"User saved new marks: {ct1}, {ct2}, {ct3}, {ct4}")
            marksList = []
            if ct1 == '':
                ct1 = None
                marksList.append(ct1)
            else:
                marksList.append(int(ct1))
            if ct2 == '':
                ct2 = None
                marksList.append(ct2)
            else:
                marksList.append(int(ct2))
            if ct3 == '':
                ct3 = None
                marksList.append(ct3)
            else:
                marksList.append(int(ct3))
            if ct4 == '':
                ct4 = None
                marksList.append(ct4)
            else:
                marksList.append(int(ct4))
            self.sendUpdatedMarks.emit(courseName, marksList)
        else:
            print("User cancelled the edit.")

    def set_allMarks_avgMark(self, allMarks, avgMark):
        self.allMarks = allMarks
        self.avgMark = avgMark

    def fill_in_cardsFrame(self, syllabus):
        while self.ui.horizontalLayout_4.count():
            item = self.ui.horizontalLayout_4.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for courseList in syllabus:
            self.loadCTMarks.emit(courseList.get('course_code'))
            # success, self.ctCount = self.load_ct_marks(course.get('course_code'))
            self.build_dynamic_cards(courseList.get('course_code'), self.avgMark, self.allMarks)

    def populate_course_tabs(self, full_syllabus_data):
        # 1. Clear any existing tabs (important if the user refreshes)
        self.ui.courseSyllabusTabWidget.clear()

        # 2. Loop through the JSON array
        for course in full_syllabus_data:
            course_code = course.get('course_code', 'Unknown')
            
            # 3. Instantiate a fresh wrapper for THIS specific course
            course_tab = SyllabusTabWrap()
            
            # 4. Feed it the data
            course_tab.set_syllabus_data(course)
            
            # 5. Connect its signals to our Home Page relays
            # course_tab.topicDeleted.connect(self.topicDeletedRelay.emit)
            # course_tab.topicAdded.connect(self.topicAddedRelay.emit)
            course_tab.progressUpdated.connect(self.progressUpdatedRelay.emit)
            
            # 6. Inject it into the UI's Tab Widget!
            self.ui.courseSyllabusTabWidget.addTab(course_tab, course_code)

            self.active_course_tabs.append(course_tab)

    def update_syllabus_progress_bars(self, full_syllabus_data):
        layout = self.ui.horizontalLayout
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # 2. Loop through the courses and do the math
        for course in full_syllabus_data:
            course_code = course.get('course_code', 'Unknown')
            total_topics = 0
            completed_topics = 0

            # Dig into the nested JSON to count topics
            for module in course.get('modules', []):
                for topic in module.get('topics', []):
                    total_topics += 1
                    # Treat '1' or 'True' as completed
                    if topic.get('completed'): 
                        completed_topics += 1

            # Avoid division by zero!
            percentage = 0
            if total_topics > 0:
                percentage = int((completed_topics / total_topics) * 100)

            # 3. Build the dynamic UI elements
            bar_container = QWidget()
            v_layout = QVBoxLayout(bar_container)
            v_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # The Vertical Progress Bar
            progress_bar = QProgressBar()
            progress_bar.setOrientation(Qt.Orientation.Vertical)
            progress_bar.setMinimum(0)
            progress_bar.setMaximum(100)
            progress_bar.setValue(percentage)
            progress_bar.setTextVisible(True)
            progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
            progress_bar.setFixedSize(30, 150) # Tweak these dimensions to match your design!
            
            # Styling it to match your dark/yellow theme
            progress_bar.setStyleSheet("""
                QProgressBar {
                    background-color: #555555;
                    border-radius: 5px;
                    color: white; 
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #D4D925; /* Your Yellow */
                    border-radius: 5px;
                }
            """)

            # The Course Label beneath it
            lbl = QLabel(course_code) # e.g., turns "CSE 2201" into just "2201" to save space
            lbl.setStyleSheet("color: #AAAAAA; font-size: 10px;")
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

            v_layout.addWidget(progress_bar)
            v_layout.addWidget(lbl)

            # Add the completed container to the main horizontal layout
            layout.addWidget(bar_container)