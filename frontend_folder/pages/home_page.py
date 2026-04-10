from PySide6.QtWidgets import (QApplication, QFileDialog, QProgressBar, QWidget, QDialog, QPushButton, QVBoxLayout, QLabel)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import (Qt, Signal)
import os

from uipy.homepageWidget import Ui_HomePage
from components.study_timer import StudyTimerScreen
from components.ct_average_card import CTAverageCard
from components.syllabus_tab import SyllabusTabWrap
from components.profile_tab import ProfileTabWrap
from dialogs.edit_marks_dialog import EditMarksDialog

class HomePageWrap(QWidget):
    sendUpdatedMarks = Signal(str, list)
    loadCTMarks = Signal(str)
    # themeToggledRelay = Signal()
    # topicDeletedRelay = Signal(int) 
    # topicAddedRelay = Signal(int, str)
    progressUpdatedRelay = Signal(int, bool)
    changeSyllabusRelay = Signal()
    logoutRelay = Signal()
    def __init__(self, api_client, user_id):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        self.client = api_client
        self.user_id = user_id # Save the ID!
        self.setup_routine_tab()
        self.load_saved_routine()
        # self.build_dynamic_cards()
        self.active_course_tabs = []

        # # --- THE CORNER WIDGET MAGIC ---
        # self.theme_toggle_btn = QPushButton("☀️ Light Mode")
        # self.theme_toggle_btn.setFixedSize(120, 30)
        self.ui.changeSyllabusBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.updateProgressBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.updateProgressBtn.setStyleSheet("""
            QPushButton {
                background-color: #444444; 
                color: white; 
                border-radius: 4px;
                margin-right: 20px; /* Keeps it from touching the edge of the screen */
            }
        """)
        self.ui.changeSyllabusBtn.setStyleSheet("""
            QPushButton {
                background-color: #444444; 
                color: white; 
                border-radius: 4px;
                margin-right: 0px;
            }
        """)
        
        # Inject it into the top-right corner of the Tab Widget!
        self.ui.courseSyllabusTabWidget.setCornerWidget(self.ui.frame, Qt.Corner.TopRightCorner)
        
        # # Wire it up to the relay
        # self.ui.updateProgressBtn.clicked.connect(self.themeToggledRelay.emit)

        self.avgMark = 0
        self.allMarks = []
        self.timerScreenInstance = StudyTimerScreen(parent=self)
        self.profile_tab = ProfileTabWrap(self.client, self.user_id)
        self.ui.label_4.setVisible(False)
        self.ui.verticalLayout_9.addWidget(self.profile_tab)

        self.profile_tab.logoutRelay.connect(self.logoutRelay.emit)
        # self.syllabusTabInstance = CourseTabWidget(parent=self)
        # self.syllabus_tab = SyllabusTabWrap()
        # self.ui.courseSyllabusTabWidget.addTab(self.syllabus_tab, "Test")

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

    def setup_routine_tab(self):
        # Assuming you have an empty layout in your Routine Tab called `routineLayout`
        # self.routine_layout = self.ui.routineLayout 
        
        # self.upload_btn = QPushButton("📁 Upload Routine (Image/PDF)")
        # self.upload_btn.setFixedSize(250, 40)
        # self.upload_btn.setStyleSheet("background-color: #005f73; color: white; font-weight: bold;")
        self.ui.uploadRoutineBtn.clicked.connect(self.handle_file_upload)
        
        # This label will hold the actual image of the routine
        self.routine_display = QLabel("No routine uploaded yet.")
        self.routine_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.routine_display.setStyleSheet("border: 2px dashed #555555; color: #777777;")
        self.routine_display.setMinimumSize(400, 500)
        
        # Add them to the tab
        # self.routine_layout.addWidget(self.upload_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.ui.verticalLayout_6.addWidget(self.routine_display)

    def load_saved_routine(self):
        success, data = self.client.get_routine_info(self.user_id)
        if success:
            db_file_path = data.get("file_path")
            file_type = data.get("file_type")

            # 1. Take the elevator up to the Master Folder
            # __file__ is in: frontend_folder/pages/home_page.py
            pages_folder = os.path.dirname(os.path.abspath(__file__))
            frontend_folder = os.path.dirname(pages_folder)
            master_project_folder = os.path.dirname(frontend_folder) 

            # 2. Clean the database string
            clean_db_path = os.path.normpath(db_file_path.strip())

            # 3. Build a net to catch the file no matter where it is
            paths_to_test = [
                os.path.join(master_project_folder, "backend", clean_db_path), # Scenario A: backend is next to frontend
                os.path.join(master_project_folder, clean_db_path),            # Scenario B: uploads are in the master folder
                os.path.join(frontend_folder, clean_db_path)                   # Scenario C: what we tried last time
            ]

            actual_path = None
            
            # 4. Check all possible timelines
            for test_path in paths_to_test:
                if os.path.exists(test_path):
                    actual_path = test_path
                    break # Stop looking, we found it!

            if actual_path:
                print(f"DEBUG: Found routine file at -> {actual_path}")
                self.display_routine_file(actual_path, file_type)
            else:
                print(f"DEBUG: Still missing. I checked all of these:")
                for p in paths_to_test:
                    print(f" - {p}")
                self.routine_display.setText("Routine file missing from disk.")
                self.routine_display.setStyleSheet("border: 2px dashed red; color: red;")
        else:
            print("No saved routine found.")

    def display_routine_file(self, file_path, file_extension):
        # Move your existing display logic here to keep things DRY (Don't Repeat Yourself)
        if file_extension in ['image', '.png', '.jpg', '.jpeg']:
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaled(self.routine_display.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.routine_display.setPixmap(scaled_pixmap)
            
        elif file_extension in ['pdf', '.pdf']:
            file_name = os.path.basename(file_path)
            self.routine_display.setText(f"📄 PDF Routine:\n\n{file_name}")

    def handle_file_upload(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Your Routine", "", "Supported Files (*.png *.jpg *.jpeg *.pdf)")
        
        if file_path:
            file_extension = os.path.splitext(file_path)[1].lower()
            
            # 1. Show it instantly
            self.display_routine_file(file_path, file_extension)
            
            # 2. Upload to database
            self.ui.uploadRoutineBtn.setText("Uploading...")
            QApplication.processEvents() # Force UI to update
            
            success, response = self.client.upload_routine(self.user_id, file_path)
            
            self.ui.uploadRoutineBtn.setText("📁 Upload Routine (Image/PDF)")
            if not success:
                print("Failed to save routine to cloud:", response)

    def change_updateProgressBtn_text(self, is_editing):
        if is_editing:
            self.ui.updateProgressBtn.setText("Close Progress Editor")
            self.ui.updateProgressBtn.setStyleSheet("background-color: #005f73; color: white; border-radius: 5px;") # Nice teal color
        else:
            self.ui.updateProgressBtn.setText("✎ Update Progress")
            self.ui.updateProgressBtn.setStyleSheet("background-color: #444444; color: white; border-radius: 5px;")

    def populate_course_tabs(self, full_syllabus_data):
        # 1. Clear any existing tabs (important if the user refreshes)
        self.ui.courseSyllabusTabWidget.clear()

        # 2. Loop through the JSON array
        for course in full_syllabus_data:
            course_code = course.get('course_code', 'Unknown')
            
            # 3. Instantiate a fresh wrapper for THIS specific course
            course_tab = SyllabusTabWrap()
            course_tab.isEditingRelay.connect(self.change_updateProgressBtn_text)
            self.ui.updateProgressBtn.clicked.connect(course_tab.toggle_all_cards)
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