import sys
from PySide6.QtWidgets import (QProgressBar, QApplication, QMainWindow, QWidget, QDialog, QLineEdit, QHBoxLayout, QPushButton, QMessageBox, QSizePolicy, QFrame, QVBoxLayout, QLabel, QScrollArea)
from PySide6.QtCore import (QSize, QCoreApplication, Qt, Signal, QTimer)
from PySide6.QtGui import QFont

#------ Imports ------
# Wrappers
from pages.login_page import LoginPageWrap, EnterEmailWrap, EnterCodeNewPassWrap
from pages.onboarding_pages import InstDeptYearSemPageWrap, SyllabusPreviewPageWrap
from pages.home_page import HomePageWrap
# Components
from components.ct_average_card import CTAverageCard
from components.study_timer import StudyTimerScreen
# Dialogs
from dialogs.edit_marks_dialog import EditMarksDialog

# Pyside UI elements
from uipy.onboarding import Ui_AppName
from uipy.authpageWidget import Ui_LoginScreen
from uipy.forgotPasswordEnterEmail import Ui_EnterEmail
from uipy.forgotPasswordEnterCodeNewPass_ui import Ui_EnterCodeNewPass
from uipy.inst_dept_year_semesterWidget import Ui_instDeptYearSemSelection
from uipy.syllabus_previewWidget import Ui_SyllabusPreview
from uipy.homepageWidget import Ui_HomePage
from components.syllabus_tab import SyllabusTabWrap
from backend_client import BackendClient

#------ Wrappers ------
#------ Authentication Page ------


#------ Selection Page ------


#------ Landing Page ------

   
#------ Home Tab ------




#------ Syllabus Tab ------
# class CourseTabWidget(QWidget):
#     def __init__(self, parent=None):
#         super().__init__()
#         self.parentInstance = parent

#     def handover_syllabus_to_builder(self, syllabusData):
#         for index, course in enumerate(syllabusData):
#             print(course.get('course_code', 'Unknown Code'))
#             self.tab_2 = QWidget()
#             self.tab_2.setObjectName(course.get('course_code', 'Unknown Code'))


#             self.parentInstance.ui.courseSyllabusTabWidget.addTab(self.tab_2, "")
#             self.parentInstance.ui.courseSyllabusTabWidget.setTabText(self.parentInstance.ui.courseSyllabusTabWidget.indexOf(self.tab_2), QCoreApplication.translate("HomePage", course.get('course_code', 'Unknown Code'), None))

    # def build_module_topic_cards():
        
# class 

#------ Study Timer Tab ------



#------ Forgot Password ------


#------ MAIN WINDOW ------
class MySoftware(QMainWindow):
    emitRecoveryEmailSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.current_user_id = None
        self.recovery_email = None
        self.current_user_syllabus = None
        self.is_dark_mode = True

        self.LOGIN_PAGE_IND = 0
        self.ENTER_EMAIL_IND = 1
        self.ENTER_CODE_NEW_PASS_IND = 2
        self.SELECTION_PAGE_IND = 3
        self.PREVIEW_PAGE_IND = 4
        
        # Setup Main Container (The Stack)
        self.uiOnboardingStackPage = Ui_AppName()
        self.onboarding_widget = QWidget()
        self.uiOnboardingStackPage.setupUi(self.onboarding_widget)
        self.setStyleSheet(u"background-color: rgb(37, 37, 29);")
        onboarding_layout = QVBoxLayout(self.onboarding_widget)
        onboarding_layout.addWidget(self.uiOnboardingStackPage.centralwidget, 1)

        # Setup Pages
        self.page_login = LoginPageWrap()
        self.page_enter_email = EnterEmailWrap()
        self.page_enter_code = EnterCodeNewPassWrap()
        self.page_selection = InstDeptYearSemPageWrap()
        self.page_syllabus = SyllabusPreviewPageWrap()

        # Setup Backened
        self.client = BackendClient()

        # Recieve signals
        self.page_login.loginSuccess.connect(self.handle_login_success)
        self.page_login.forgotPassword.connect(self.go_to_email)
        self.page_login.signupSuccess.connect(self.go_to_selection)
        self.current_username = None
        self.page_enter_email.sendValidEmailToParent.connect(self.go_to_code)
        self.page_enter_email.goBack.connect(self.go_to_login)
        self.page_enter_code.codeValid.connect(self.go_to_login)
        self.page_enter_code.goBack.connect(self.go_to_email)
        self.page_selection.selectionValid.connect(self.go_to_preview)
        self.page_selection.goBack.connect(self.go_to_login)
        self.page_syllabus.goNext.connect(self.go_to_home)
        self.page_syllabus.goBack.connect(self.go_to_selection_from_preview)

        self.setCentralWidget(self.onboarding_widget)
        self.resize(1100, 700)

        # Add to stack
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_login)      # Index 0
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_enter_email) # Index 1
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_enter_code) # Index 2
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_selection)  # Index 3
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_syllabus)   # Index 4
        self.go_to_login()

        success, loggedIn, response = self.client.is_logged_in()
        if success:
            if loggedIn:
                self.go_to_home()
            else:
                self.go_to_login()
        else:
            print(f"Error occurred: {response}")

    def toggle_application_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        theme_file = "styles/dark_theme.qss" if self.is_dark_mode else "styles/light_theme.qss"
        
        with open(theme_file, "r") as f:
            self.setStyleSheet(f.read())
        
        if self.is_dark_mode:
            print("Switching to Dark Mode...")
            self.main_app.theme_toggle_btn.setText("☀️ Light Mode")
            # Apply your global Dark stylesheet here
            self.setStyleSheet()
        else:
            print("Switching to Bright Mode...")
            self.main_app.theme_toggle_btn.setText("🌙 Dark Mode")
            # Apply your global Light stylesheet here
            self.setStyleSheet()

    def handle_login_success(self, user_id, username):
        self.current_user_id = user_id
        self.current_username = username
        print(f"Logged in with id: {self.current_user_id}, username: {self.current_username}")
        self.go_to_home()

    def go_to_login(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.LOGIN_PAGE_IND)
    
    def go_to_email(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.ENTER_EMAIL_IND)

    def go_to_code(self, email):
        self.recovery_email = email
        # Send the recovery email to EnterCodeNewPassWrap
        self.page_enter_code.set_recovery_email(self.recovery_email)
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.ENTER_CODE_NEW_PASS_IND)

    def go_to_selection(self, user_id, username):
        self.current_user_id = user_id
        self.current_username = username
        print(f"Logged in as id: {self.current_user_id}, username: {self.current_username}")
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.SELECTION_PAGE_IND)

    def go_to_selection_from_preview(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.SELECTION_PAGE_IND)


    def load_syllabus(self):
        print("Fetching syllabus for current session...")
        success, self.current_user_syllabus = self.client.get_syllabus()
        # print(self.current_user_syllabus)

        return success
        # Backend GET /syllabus returns a JSON array of courses (not {"syllabus": [...]})
        # if success and isinstance(self.current_user_syllabus, list):
        #     syllabus_list = self.current_user_syllabus
        #     print("Syllabus loaded:", len(syllabus_list)) 
        # else:
        #     print(self.current_user_syllabus)
        #     return False

    def go_to_preview(self):
        data = self.page_selection.preference_payload() 
        sem_val = 1 if data['semester'] == "Odd" else 2
        
        self.client.set_academic_context(
            self.current_user_id,
            data['university'],
            data['department'],
            data['year'],
            sem_val
        )

        syllabus_found = self.load_syllabus()
        
        if syllabus_found:
            self.page_syllabus.build_and_place_cards(self.current_user_syllabus)
            self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.PREVIEW_PAGE_IND)
        else:
            QMessageBox.warning(self, "Syllabus not found", "No syllabus was found corresponding to the selected information.")

    # def set_current_user_syllabus(self, syllabusData):
    #     self.current_user_syllabus = syllabusData

    def go_to_home(self):
        self.main_app = HomePageWrap()
        self.client.get_me()
        # Relay Signal connections
        self.main_app.sendUpdatedMarks.connect(self.update_ct_marks_and_cardsFrame)
        self.main_app.loadCTMarks.connect(self.load_ct_marks)
        self.main_app.themeToggledRelay.connect(self.toggle_application_theme)
        # self.main_app.topicAddedRelay.connect(self.add_new_topic)
        # self.main_app.topicDeletedRelay.connect(self.delete_topic)
        self.main_app.progressUpdatedRelay.connect(self.update_topic_progress)

        self.setCentralWidget(self.main_app)
        welcome = self.current_username or "User"
        self.main_app.ui.welcomeUserLabel.setText(f"Welcome, {welcome}!")

        # Request course code value from backend to then request ct marks from the backend against those courses
        success = self.load_syllabus()
        # self.build_syllabus_preview_for_home_page()
        # print(self.current_user_syllabus)
        if success:
            self.main_app.fill_in_cardsFrame(self.current_user_syllabus)
            # for course in self.current_user_syllabus:
            #     success, allMarks, avgMark, ctCount = self.load_ct_marks(course.get('course_code'))
            #     self.main_app.build_dynamic_cards(course.get('course_code'), avgMark, allMarks)
            self.main_app.populate_course_tabs(self.current_user_syllabus)

            self.main_app.update_syllabus_progress_bars(self.current_user_syllabus)
        
        # Clean up memory by destroying the onboarding views
        self.onboarding_widget.deleteLater()
        self.onboarding_widget = None

    # --- THE SMART METHOD ---
    def update_topic_progress(self, topic_id, is_checked):
        print(f"API CALL: Setting topic {topic_id} completion to {is_checked}")
        
        success, response = self.client.update_topic_completion(topic_id, is_checked)
        
        if success:
            print("Database updated successfully!")
            # Optional: Write a quick loop here to update self.current_user_syllabus 
            # so the checkbox stays checked if the user navigates away and comes back.
            # Fetch the fresh data from the database with the new completion status
            if self.load_syllabus():
                # Re-calculate and redraw the progress bars!
                self.main_app.update_syllabus_progress_bars(self.current_user_syllabus)
        else:
            print("Failed to update database:", response)

    # def fill_in_cardsFrame(self):
    #     while self.ui.horizontalLayout_4.count():
    #     item = self.ui.horizontalLayout_4.takeAt(0)
    #     widget = item.widget()
    #     if widget:
    #         widget.deleteLater()
    #     for course in self.current_user_syllabus:
    #         success, allMarks, avgMark, ctCount = self.load_ct_marks(course.get('course_code'))
    #         self.main_app.build_dynamic_cards(course.get('course_code'), avgMark, allMarks)

    def load_ct_marks(self, courseCode):
        success, response = self.client.get_ct_marks(courseCode)
        if success:
            self.main_app.set_allMarks_avgMark(response.get('ct_marks'), response.get('average'))
            return True, response.get('counted_ct')
        else:
            return False, None, None, None
        
    def update_ct_marks_and_cardsFrame(self, courseCode, list_ctMarks):
        for ctNo, mark in enumerate(list_ctMarks):
            print(ctNo)
            if mark == None:
                continue
            success, response = self.client.set_ct_marks(courseCode, int(ctNo) + 1, mark)
            if success:
                self.main_app.set_avgMark(response.get('average'))
                print("Marks updated successfully!")
                self.main_app.fill_in_cardsFrame(self.current_user_syllabus)
            else:
                print(response)

    # def build_syllabus_preview_for_home_page(self):
    #     self.main_app.syllabusTabInstance.handover_syllabus_to_builder(self.current_user_syllabus)

    # def load_home_page(self):
    #     # Pass the data DOWN when the user logs in
    #     # (Assuming self.master_syllabus contains the list of courses. 
    #     # Here we just pass the first course as an example).
    #     if self.current_user_syllabus:
    #         first_course = self.current_user_syllabus[0]
    #         self.main_app.syllabus_tab.set_syllabus_data(first_course)
            
    #     self.stackedWidget.setCurrentIndex(self.HOME_PAGE_IND)

    # def add_new_topic(self, module_name, new_topic):
    #     print(f"API CALL: Adding '{new_topic}' to '{module_name}'")
    #     # success, resp = self.client.add_topic(module_name, new_topic)
    #     # if success: update self.master_syllabus and refresh!
        
    # def delete_topic(self, module_name, topic_name):
    #     print(f"API CALL: Deleting '{topic_name}' from '{module_name}'")
    #     # success, resp = self.client.delete_topic(module_name, topic_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySoftware()
    window.show()
    sys.exit(app.exec())