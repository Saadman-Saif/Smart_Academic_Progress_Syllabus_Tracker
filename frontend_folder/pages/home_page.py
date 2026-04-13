from PySide6.QtWidgets import (QApplication, QFileDialog, QProgressBar, QWidget, QDialog, QVBoxLayout, QLabel)
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
    progressUpdatedRelay = Signal(int, bool)
    changeSyllabusRelay = Signal()
    logoutRelay = Signal()
    selectSyllabusBtnRelay = Signal()
    def __init__(self, api_client, user_id):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        self.client = api_client
        self.user_id = user_id # Save id
        self.setup_routine_tab()
        self.load_saved_routine()
        self.active_course_tabs = []

        # --- CORNER WIDGET ---
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
        
        # add the corner widget
        self.ui.courseSyllabusTabWidget.setCornerWidget(self.ui.frame, Qt.Corner.TopRightCorner)
        self.ui.changeSyllabusBtn.clicked.connect(self.selectSyllabusBtnRelay.emit)

        self.avgMark = 0
        self.allMarks = []
        self.timerScreenInstance = StudyTimerScreen(parent=self)
        self.profile_tab = ProfileTabWrap(self.client, self.user_id)
        self.ui.label_4.setVisible(False)
        self.ui.verticalLayout_9.addWidget(self.profile_tab)

        self.profile_tab.logoutRelay.connect(self.logoutRelay.emit)
        self.profile_tab.selectSyllabusBtnSignal.connect(self.selectSyllabusBtnRelay.emit)

    def build_dynamic_cards(self, course, avgMarks, allMarks):
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
            self.build_dynamic_cards(courseList.get('course_code'), self.avgMark, self.allMarks)

    def setup_routine_tab(self):
        self.ui.uploadRoutineBtn.clicked.connect(self.handle_file_upload)
        
        self.routine_display = QLabel("No routine uploaded yet.")
        self.routine_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.routine_display.setStyleSheet("border: 2px dashed #555555; color: #777777;")
        self.routine_display.setMinimumSize(400, 500)
        
        # Add
        self.ui.verticalLayout_6.addWidget(self.routine_display)

        self.routine_display.mousePressEvent = self.open_external_routine

    def load_saved_routine(self):
        success, data = self.client.get_routine_info(self.user_id)
        if success:
            db_file_path = data.get("file_path")
            file_type = data.get("file_type")

            # __file__ is in: frontend_folder/pages/home_page.py
            pages_folder = os.path.dirname(os.path.abspath(__file__))
            frontend_folder = os.path.dirname(pages_folder)
            master_project_folder = os.path.dirname(frontend_folder) 

            clean_db_path = os.path.normpath(db_file_path.strip())

            paths_to_test = [
                os.path.join(master_project_folder, "backend", clean_db_path), # Scenario A: backend is next to frontend
                os.path.join(master_project_folder, clean_db_path),            # Scenario B: uploads are in the master folder
                os.path.join(frontend_folder, clean_db_path)                   # Scenario C: what i tried last time
            ]

            actual_path = None
            
            # Check all paths
            for test_path in paths_to_test:
                if os.path.exists(test_path):
                    actual_path = test_path
                    break

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
        # Move existing display logic here to keep things DRY (Don't Repeat Yourself)
        self.current_routine_path = file_path
        self.current_routine_ext = file_extension
        if file_extension in ['image', '.png', '.jpg', '.jpeg']:
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaled(self.routine_display.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.routine_display.setPixmap(scaled_pixmap)
            
        elif file_extension in ['pdf', '.pdf']:
            file_name = os.path.basename(file_path)
            self.routine_display.setText(f"📄 PDF Routine:\n\n{file_name}")
            

    def open_external_routine(self, event):
        if hasattr(self, 'current_routine_path') and self.current_routine_path:
            if self.current_routine_ext in ['pdf', '.pdf']:
                print(f"Openning external file: {self.current_routine_path}")
                os.startfile(self.current_routine_path)
                

    def handle_file_upload(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Your Routine", "", "Supported Files (*.png *.jpg *.jpeg *.pdf)")
        
        if file_path:
            file_extension = os.path.splitext(file_path)[1].lower()
            
            # Show it instantly
            self.display_routine_file(file_path, file_extension)
            
            # Upload to database
            self.ui.uploadRoutineBtn.setText("Uploading...")
            QApplication.processEvents() # Force UI to update
            
            success, response = self.client.upload_routine(self.user_id, file_path)
            
            self.ui.uploadRoutineBtn.setText("Upload Routine")
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
        # Clear any existing tabs (when user refreshes)
        self.ui.courseSyllabusTabWidget.clear()

        for course in full_syllabus_data:
            course_code = course.get('course_code', 'Unknown')
            
            # new instance for new course
            course_tab = SyllabusTabWrap()
            course_tab.isEditingRelay.connect(self.change_updateProgressBtn_text)
            self.ui.updateProgressBtn.clicked.connect(course_tab.toggle_all_cards)
            course_tab.set_syllabus_data(course)
            
            course_tab.progressUpdated.connect(self.progressUpdatedRelay.emit)

            self.ui.courseSyllabusTabWidget.addTab(course_tab, course_code)

            self.active_course_tabs.append(course_tab)

    def update_syllabus_progress_bars(self, full_syllabus_data):
        layout = self.ui.horizontalLayout
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for course in full_syllabus_data:
            course_code = course.get('course_code', 'Unknown')
            total_topics = 0
            completed_topics = 0

            for module in course.get('modules', []):
                for topic in module.get('topics', []):
                    total_topics += 1
                    if topic.get('completed'): 
                        completed_topics += 1

            percentage = 0
            if total_topics > 0:
                percentage = int((completed_topics / total_topics) * 100)

            bar_container = QWidget()
            v_layout = QVBoxLayout(bar_container)
            v_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            progress_bar = QProgressBar()
            progress_bar.setOrientation(Qt.Orientation.Vertical)
            progress_bar.setMinimum(0)
            progress_bar.setMaximum(100)
            progress_bar.setValue(percentage)
            progress_bar.setTextVisible(True)
            progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
            progress_bar.setFixedSize(30, 150)

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
            lbl = QLabel(course_code)
            lbl.setStyleSheet("color: #AAAAAA; font-size: 10px;")
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

            v_layout.addWidget(progress_bar)
            v_layout.addWidget(lbl)

            layout.addWidget(bar_container)