import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QVBoxLayout, QHBoxLayout, QStackedWidget)
from PySide6.QtCore import (Signal, QRect)

#------ Imports ------
# Wrappers
from pages.login_page import LoginPageWrap, EnterEmailWrap, EnterCodeNewPassWrap
from pages.onboarding_pages import InstDeptYearSemPageWrap, SyllabusPreviewPageWrap
from pages.home_page import HomePageWrap

# Pyside UI elements
from uipy.onboarding import Ui_AppName
from backend_client import BackendClient

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
        
        # Setup Main Container (The Master Stack)
        self.master_stack = QStackedWidget()
        self.setCentralWidget(self.master_stack)

        # Setup Onboarding Stack
        self.uiOnboardingStackPage = Ui_AppName()
        self.onboarding_widget = QWidget()
        self.uiOnboardingStackPage.setupUi(self.onboarding_widget)
        
        # Restore the Layout Stretcher!
        self.setStyleSheet(u"background-color: rgb(37, 37, 29);")
        onboarding_layout = QVBoxLayout(self.onboarding_widget)
        onboarding_layout.addWidget(self.uiOnboardingStackPage.centralwidget, 1)
        onboarding_layout.setContentsMargins(0, 0, 0, 0)

        # Setup Pages
        self.page_login = LoginPageWrap()
        self.page_enter_email = EnterEmailWrap()
        self.page_enter_code = EnterCodeNewPassWrap()
        self.page_selection = InstDeptYearSemPageWrap()
        self.page_syllabus = SyllabusPreviewPageWrap()

        # Setup Backend
        self.client = BackendClient()

        # Receive signals
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

        # Add to Stacks
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_login)      # Index 0
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_enter_email) # Index 1
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_enter_code)  # Index 2
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_selection)   # Index 3
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_syllabus)    # Index 4
        self.master_stack.addWidget(self.onboarding_widget) 
        
        self.resize(1100, 700)
        self.go_to_login()

        success, loggedIn, response = self.client.is_logged_in()
        if success:
            if loggedIn:
                self.current_user_id = response.get("user_id") 
                self.current_username = response.get("username", "User")
                self.go_to_home()
            else:
                self.go_to_login()
        else:
            print(f"Error occurred: {response}")

    def handle_login_success(self, user_id, username):
        self.current_user_id = user_id
        self.current_username = username
        print(f"Logged in with id: {self.current_user_id}, username: {self.current_username}")
        self.go_to_home()

    def go_to_login(self):
        # master stack shows onboarding page (selection)
        self.master_stack.setCurrentWidget(self.onboarding_widget)
        # inner stack shows loging screen
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.LOGIN_PAGE_IND)
    
    def go_to_email(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.ENTER_EMAIL_IND)

    def go_to_code(self, email):
        self.recovery_email = email
        self.page_enter_code.set_recovery_email(self.recovery_email)
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.ENTER_CODE_NEW_PASS_IND)

    def go_to_selection(self, user_id, username):
        self.current_user_id = user_id
        self.current_username = username
        print(f"Logged in as id: {self.current_user_id}, username: {self.current_username}")
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.SELECTION_PAGE_IND)

    def go_to_selection_from_preview(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.SELECTION_PAGE_IND)
        # self.page_syllabus.ui.scrollAreaWidgetContents.removeWidget()
        self.page_syllabus.reset_syllabus_cards()

    def go_to_selection_from_home(self):
        print("Switching back to Selection Page...")
        self.master_stack.setCurrentWidget(self.onboarding_widget)
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.SELECTION_PAGE_IND)
        self.page_selection.ui.backBtn.clicked.connect(self.back_from_selection)

    def load_syllabus(self):
        print("Fetching syllabus for current session...")
        success, self.current_user_syllabus = self.client.get_syllabus()
        # print(self.current_user_syllabus)
        return success

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

    def set_welcome_text(self):
        welcome = self.current_username or "User"
        self.main_app.ui.welcomeUserLabel.setText(f"Welcome, {welcome}!")

    def back_from_selection(self):
        self.master_stack.addWidget(self.main_app)
        self.master_stack.setCurrentWidget(self.main_app)
        self.page_selection.ui.backBtn.clicked.connect(self.go_to_home)

    def go_to_home(self):
        self.main_app = HomePageWrap(self.client, self.current_user_id)
        
        # use .get() in case get_me() fails
        me_success, me_data = self.client.get_me()
        if me_success:
            self.current_username = me_data.get('username', self.current_username)
            
        self.set_welcome_text()
        self.main_app.sendUpdatedMarks.connect(self.update_ct_marks_and_cardsFrame)
        self.main_app.loadCTMarks.connect(self.load_ct_marks)
        self.main_app.progressUpdatedRelay.connect(self.update_topic_progress)
        self.main_app.logoutRelay.connect(self.process_logout)
        self.main_app.selectSyllabusBtnRelay.connect(self.go_to_selection_from_home)

        # Request course code value from backend
        success = self.load_syllabus()
        if success:
            self.main_app.fill_in_cardsFrame(self.current_user_syllabus)
            self.main_app.populate_course_tabs(self.current_user_syllabus)
            self.main_app.update_syllabus_progress_bars(self.current_user_syllabus)
        
        #Add the main app to the master stack
        self.master_stack.addWidget(self.main_app)
        # Switch the screen to show it
        self.master_stack.setCurrentWidget(self.main_app)

    def update_topic_progress(self, topic_id, is_checked):
        print(f"API CALL: Setting topic {topic_id} completion to {is_checked}")
        
        success, response = self.client.update_topic_completion(topic_id, is_checked)
        
        if success:
            print("Database updated successfully!")
            if self.load_syllabus():
                self.main_app.update_syllabus_progress_bars(self.current_user_syllabus)
        else:
            print("Failed to update database:", response)

    def load_ct_marks(self, courseCode):
        success, response = self.client.get_ct_marks(courseCode)
        if success:
            self.main_app.set_allMarks_avgMark(response.get('ct_marks'), response.get('average'))
            return True, response.get('counted_ct')
        else:
            return False, None, None, None
        
    def update_ct_marks_and_cardsFrame(self, courseCode, list_ctMarks):
        for ctNo, mark in enumerate(list_ctMarks):
            if mark is None:
                continue
            success, response = self.client.set_ct_marks(courseCode, int(ctNo) + 1, mark)
            if success:
                self.main_app.set_avgMark(response.get('average'))
                print("Marks updated successfully!")
                self.main_app.fill_in_cardsFrame(self.current_user_syllabus)
            else:
                print(response)

    def process_logout(self):
        print("User logged out. Locking the app.")
        
        # delete the user data from memory
        self.current_user_id = None
        self.current_username = None
        self.current_user_syllabus = None
        
        self.master_stack.setCurrentWidget(self.onboarding_widget)
        
        # Safely destroy the Home Page to free up memory
        if getattr(self, 'main_app', None):
            self.master_stack.removeWidget(self.main_app)
            self.main_app.deleteLater()
            self.main_app = None
            
        # inner stack goes to login page
        self.go_to_login()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySoftware()
    window.show()
    sys.exit(app.exec())