import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QSizePolicy, QFrame, QVBoxLayout, QLabel, QScrollArea)
from PySide6.QtCore import (QSize, QCoreApplication, Qt, Signal, QTimer)
from PySide6.QtGui import QFont

# Imports
from onboarding import Ui_AppName
from authpageWidget import Ui_LoginScreen
from forgotPasswordEnterEmail import Ui_EnterEmail
from forgotPasswordEnterCodeNewPass_ui import Ui_EnterCodeNewPass
from inst_dept_year_semesterWidget import Ui_instDeptYearSemSelection
from syllabus_previewWidget import Ui_SyllabusPreview
from homepageWidget import Ui_HomePage
from backend_client import BackendClient

# --- WRAPPERS ---

class LoginPageWrap(QWidget):
    loginSuccess = Signal(int, str)
    forgotPassword = Signal()
    signupSuccess = Signal(int, str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.client = BackendClient()

        # Connect the buttons
        self.ui.login_btn.clicked.connect(self.handle_login_click)
        self.ui.forgot_password_label.linkActivated.connect(self.handle_link_click)
        self.ui.signup_btn.clicked.connect(self.handle_signup_click)
    
    def handle_login_click(self):
        user_text = self.ui.login_email_lineedit.text()
        pass_text = self.ui.login_password_lineedit.text()

        self.ui.login_btn.setText("Connecting...")
        self.ui.login_btn.setEnabled(False)
        QApplication.processEvents()

        success, message, user_id, username = self.client.login(user_text, pass_text)

        self.ui.login_btn.setText("Login")
        self.ui.login_btn.setEnabled(True)

        if success:
            print("Login worked!")
            self.loginSuccess.emit(user_id, username or "")
        else:
            QMessageBox.warning(self, "Login Failed", message)

    def handle_link_click(self):        
        self.forgotPassword.emit()

    def handle_signup_click(self):
        username = self.ui.signup_username_lineedit.text()
        email = self.ui.signup_email_lineedit.text()
        password = self.ui.signup_password_lineedit.text()

        success, response, user_id, uname = self.client.signup(username, email, password)

        if success:
            print("Signup worked!")
            self.signupSuccess.emit(user_id, uname or username)
        else:
            QMessageBox.warning(self, "Signup Failed", response)


class InstDeptYearSemPageWrap(QWidget):
    selectionValid = Signal()
    goBack = Signal()
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_instDeptYearSemSelection()
        self.ui.setupUi(self)
        self.ui.nextBtn.clicked.connect(self.handle_nextBtn_click)
        self.ui.backBtn.clicked.connect(self.handle_backBtn_click)

    def handle_nextBtn_click(self):
        self.selectionValid.emit()

    def handle_backBtn_click(self):
        self.goBack.emit()

    def preference_payload(self):        
        return {
            "university": self.ui.universityComboBox.currentText(),
            "department": self.ui.departmentComboBox.currentText(),
            "year": self.ui.yearComboBox.currentText(),
            "semester": self.ui.semesterComboBox.currentText()
        }


class SyllabusPreviewPageWrap(QWidget):
    goNext = Signal()
    goBack = Signal()
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_SyllabusPreview()
        self.ui.setupUi(self)
        self.client = BackendClient()
        self.ui.nextBtn.clicked.connect(self.handle_nextBtn_click)
        self.ui.backBtn.clicked.connect(self.handle_backBtn_click)

    def handle_nextBtn_click(self):
        self.goNext.emit()

    def handle_backBtn_click(self):
        self.goBack.emit()

    def load_data(self):
        print("Fetching syllabus for current session...")
        success, data = self.client.get_syllabus()
        print(data)
        # Backend GET /syllabus returns a JSON array of courses (not {"syllabus": [...]})
        if success and isinstance(data, list):
            syllabus_list = data
            print("Syllabus loaded:", len(syllabus_list)) 

            for col_idx, course in enumerate(syllabus_list):
                self._create_course_card(course, col_idx)
            return True
        else:
            print(data)
            return False

    def _create_course_card(self, course, col_idx):
        # Main Card Frame
        card_frame = QFrame(self.ui.gridFrame)
        card_frame.setMinimumSize(QSize(188, 359))
        card_frame.setStyleSheet("background-color: rgb(50, 50, 50);")
        card_frame.setFrameShape(QFrame.Shape.StyledPanel)
        card_frame.setFrameShadow(QFrame.Shadow.Raised)
        
        # Policy setup
        size_policy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        card_frame.setSizePolicy(size_policy)
        
        card_layout = QVBoxLayout(card_frame)

        # Header
        header = QFrame(card_frame)
        header.setStyleSheet("background-color: rgb(75, 75, 75)")
        header.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        header.setMaximumHeight(80)
        header_layout = QVBoxLayout(header)

        # Header Texts
        course_code_lbl = QLabel(course.get('course_code', 'Unknown Code'), header)
        font1 = QFont()
        font1.setFamilies(["Inter"])
        font1.setPointSize(12)
        font1.setBold(True)
        course_code_lbl.setFont(font1)

        course_title_lbl = QLabel(course.get('course_name', 'Unknown Title'), header)
        font2 = QFont()
        font2.setFamilies(["Inter"])
        course_title_lbl.setFont(font2)
        course_title_lbl.setWordWrap(True)

        header_layout.addWidget(course_code_lbl)
        header_layout.addWidget(course_title_lbl)
        card_layout.addWidget(header)

        # Body (Scroll Area)
        body_scroll = QScrollArea(card_frame)
        body_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        body_scroll.setWidgetResizable(True)
        body_scroll.setStyleSheet("background-color: rgb(60, 60, 60)")
        
        scroll_content = QWidget()
        body_scroll.setWidget(scroll_content)
        scroll_layout = QVBoxLayout(scroll_content)

        # Generate the HTML List of Modules
        module_html = "<ul style='font-size: 14px;'>" 
        for module in course.get('modules', []):
            module_html += f"<li>{module.get('title', '')}</li>"
        module_html += "</ul>"

        module_lbl = QLabel(module_html, scroll_content)
        module_lbl.setWordWrap(True)
        scroll_layout.addWidget(module_lbl)
        scroll_layout.addStretch() # Pushes text to the top

        card_layout.addWidget(body_scroll)

        # Add the finished card to the main GridLayout (Row 1, Column col_idx)
        self.ui.gridLayout.addWidget(card_frame, 1, col_idx, 1, 1)


class HomePageWrap(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        self.CTavgScreenInstance = CTAverageCard(parent=self)
        self.timerScreenInstance = StudyTimerScreen(parent=self)

class CTAverageCard(QWidget):
    def __init__(self, parent):
        super().__init__()
        avgMarks = {"CSE 2201": 16, 
                    "CSE 2203": 15, 
                    "CSE 2205": 19, 
                    "HUM 2213": 13,
                    "Math 2213": 17}
        allMarks = {"CSE 2201": [16, 15, 17], 
                    "CSE 2203": [15, 15, 15, 15], 
                    "CSE 2205": [20, 18], 
                    "HUM 2213": [10, 13, 16],
                    "Math 2213": [16, 18, 17]}
        self.parentInstance = parent
        for cardNo, course in enumerate(avgMarks):
            self.parentInstance.ui.cardFrame = QFrame(self.parentInstance.ui.cardsFrame)
            self.parentInstance.ui.cardFrame.setObjectName(u"cardFrame")
            self.parentInstance.ui.cardFrame.setFrameShape(QFrame.Shape.StyledPanel)
            self.parentInstance.ui.cardFrame.setFrameShadow(QFrame.Shadow.Raised)
            self.parentInstance.ui.verticalLayout_5 = QVBoxLayout(self.parentInstance.ui.cardFrame)
            self.parentInstance.ui.verticalLayout_5.setObjectName(u"verticalLayout_5")
            self.parentInstance.ui.courseCodeLabel = QLabel(self.parentInstance.ui.cardFrame)
            self.parentInstance.ui.courseCodeLabel.setObjectName(u"courseCodeLabel")
            sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
            sizePolicy3.setHorizontalStretch(0)
            sizePolicy3.setVerticalStretch(0)
            sizePolicy3.setHeightForWidth(self.parentInstance.ui.courseCodeLabel.sizePolicy().hasHeightForWidth())
            self.parentInstance.ui.courseCodeLabel.setSizePolicy(sizePolicy3)
            font2 = QFont()
            font2.setFamilies([u"Inter"])
            font2.setPointSize(12)
            font2.setBold(True)
            self.parentInstance.ui.courseCodeLabel.setFont(font2)
            self.parentInstance.ui.courseCodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.parentInstance.ui.verticalLayout_5.addWidget(self.parentInstance.ui.courseCodeLabel)

            self.parentInstance.ui.markLabel = QLabel(self.parentInstance.ui.cardFrame)
            self.parentInstance.ui.markLabel.setObjectName(u"markLabel")
            font3 = QFont()
            font3.setFamilies([u"Inter"])
            font3.setPointSize(48)
            font3.setBold(True)
            self.parentInstance.ui.markLabel.setFont(font3)
            self.parentInstance.ui.markLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.parentInstance.ui.verticalLayout_5.addWidget(self.parentInstance.ui.markLabel)

            for ctNo, marks in enumerate(allMarks.get(course)):
                self.parentInstance.ui.ctLabel = QLabel(self.parentInstance.ui.cardFrame)
                self.parentInstance.ui.ctLabel.setObjectName(u"ctLabel")
                font4 = QFont()
                font4.setFamilies([u"Inter"])
                font4.setPointSize(10)
                font4.setBold(False)
                self.parentInstance.ui.ctLabel.setFont(font4)
                self.parentInstance.ui.ctLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.parentInstance.ui.ctLabel.setText(QCoreApplication.translate("HomePage", f"CT{ctNo + 1}: {marks}", None))
                self.parentInstance.ui.verticalLayout_5.addWidget(self.parentInstance.ui.ctLabel)


            self.parentInstance.ui.horizontalLayout_4.addWidget(self.parentInstance.ui.cardFrame)

            self.parentInstance.ui.courseCodeLabel.setText(QCoreApplication.translate("HomePage", course, None))
            self.parentInstance.ui.markLabel.setText(QCoreApplication.translate("HomePage", str(avgMarks.get(course)), None))


class StudyTimerScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.client = BackendClient()
        self.parentInstance = parent
        self.parentInstance.ui.pauseBtn.setVisible(False)
        self.parentInstance.ui.stopBtn.setVisible(False)
        self.elapsedTime_Seconds = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer_display)
        self.parentInstance.ui.playBtn.clicked.connect(self.handle_playBtn_click)
        self.parentInstance.ui.pauseBtn.clicked.connect(self.handle_pauseBtn_click)
        self.parentInstance.ui.stopBtn.clicked.connect(self.handle_stopBtn_click)
        self.parentInstance.ui.resetBtn.clicked.connect(self.handle_resetBtn_click)
        self.parentInstance.ui.saveSessionBtn.clicked.connect(self.handle_saveSessionBtn_click)

    def handle_playBtn_click(self):
        # if not self.elapsedTime_Seconds:
        #     success, result = self.client.start_study(self.elapsedTime_Seconds)
        #     if success:
        #         print(f"Session started on backend with ID: {result}")
        self.timer.start(1000)
        self.parentInstance.ui.playBtn.setVisible(False)
        self.parentInstance.ui.resetBtn.setVisible(False)
        self.parentInstance.ui.pauseBtn.setVisible(True)
        self.parentInstance.ui.stopBtn.setVisible(True)
        #     else:
        #         print(f"Failed to start on backend: {result}")
        # else:
        #     success, result = self.client.resume_study()
        #     if success:
        #         # Resume your local QTimer
        #         print("Resumed backend")
        #     else:
        #         print("Error resuming timer")

    def handle_resetBtn_click(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Caution")
        msgBox.setInformativeText("Do you want to reset your study session?")
        # reset = msgBox.addButton("Reset", QMessageBox.ButtonRole.AcceptRole)
        # msgBox.addButton(QMessageBox.StandardButton.Cancel)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Reset | QMessageBox.StandardButton.Cancel)
        ret = msgBox.exec()
        if ret == QMessageBox.StandardButton.Reset:
            self.elapsedTime_Seconds = -1
            self.update_timer_display()
            self.parentInstance.ui.stopBtn.setVisible(False)            

    def handle_pauseBtn_click(self):
        # success, result = self.client.pause_study()
        # if success:
        #     print("Paused backend")
        self.timer.stop()
        self.parentInstance.ui.playBtn.setVisible(True)
        self.parentInstance.ui.resetBtn.setVisible(True)
        self.parentInstance.ui.pauseBtn.setVisible(False)

    def handle_stopBtn_click(self):
        self.timer.stop()
        self.parentInstance.ui.playBtn.setVisible(True)
        self.parentInstance.ui.resetBtn.setVisible(True)
        self.parentInstance.ui.pauseBtn.setVisible(False)
        self.parentInstance.ui.stopBtn.setVisible(False)

    def update_timer_display(self):
        self.elapsedTime_Seconds += 1
        hours = self.elapsedTime_Seconds // 3600
        minutes = (self.elapsedTime_Seconds % 3600) // 60
        seconds = self.elapsedTime_Seconds % 60
        timerText = f"<html><head/><body><p>{hours}<span style=\" font-size:24pt;\">hr   </span>{minutes}<span style=\" font-size:24pt;\">min </span>{seconds}<span style=\" font-size:24pt;\">sec</span></p></body></html>" 
        self.parentInstance.ui.timerLabel.setText(timerText)

    def handle_saveSessionBtn_click(self):
        msgbx = QMessageBox()
        msgbx.setWindowTitle("Caution")
        msgbx.setInformativeText("You are about to end the current study session and save the elapsed time. Do you want to save your progress?")
        # reset = msgBox.addButton("Reset", QMessageBox.ButtonRole.AcceptRole)
        # msgBox.addButton(QMessageBox.StandardButton.Cancel)
        msgbx.setStandardButtons(QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel)
        ret = msgbx.exec()
        if ret == QMessageBox.StandardButton.Save:
            # Determine if they finished the timer natively, or hit stop early (interrupted)
            was_interrupted = True # Change this logic based on your timer state
            
            success, result = self.client.stop_study(was_interrupted)
            if success:
                # Reset your local QTimer and UI
                print("Stopped backend")
                
                # Bonus: Automatically fetch the daily summary to update a label!
                self.fetch_summary()
            else:
                print("Error while saving session")

    def fetch_summary(self):
        success, data = self.client.get_today_summary()
        if success:
            print("Today's Summary:", data)
            # Update a label like: self.parent.ui.summaryLabel.setText(...)



class EnterEmailWrap(QWidget):
    sendValidEmailToParent = Signal(str)
    goBack = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_EnterEmail()
        self.client = BackendClient()
        self.recoveryEmail = None
        
        self.ui.setupUi(self)
        self.ui.nextBtn.clicked.connect(self.handle_nextBtn_click)
        self.ui.backBtn.clicked.connect(self.handle_backBtn_click)

    def handle_nextBtn_click(self):
        self.recoveryEmail = self.ui.emailInputLineEdit.text()
        self.ui.nextBtn.setText("Connecting...")
        self.ui.nextBtn.setEnabled(False)
        self.ui.backBtn.setEnabled(False)
        QApplication.processEvents()
        success, response = self.client.sendCode(self.recoveryEmail)
        if success:
            print(response)
            self.sendValidEmailToParent.emit(self.recoveryEmail)
        else:
            QMessageBox.warning(self, "Error", f"An error was encountered: {response}")
        self.ui.nextBtn.setText("Next")
        self.ui.nextBtn.setEnabled(True)
        self.ui.backBtn.setEnabled(True)            
    
    def handle_backBtn_click(self):
        self.goBack.emit()

class EnterCodeNewPassWrap(QWidget):
    codeValid = Signal()
    goBack = Signal()
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_EnterCodeNewPass()
        self.ui.setupUi(self)
        self.recoveryEmail = None
        self.ui.saveBtn.clicked.connect(self.handle_nextBtn_click)
        self.ui.backBtn.clicked.connect(self.handle_backBtn_click)

    def set_recovery_email(self, email):
        self.recoveryEmail = email

    def handle_nextBtn_click(self):
        enteredCode = self.ui.codeInputLineEdit.text()
        newPassword = self.ui.newPassLineEdit.text()
        confirmPassword = self.ui.confirmPassLineEdit.text()
        if newPassword == confirmPassword:
            self.client = BackendClient()
            success, response = self.client.processEnteredCode(self.recoveryEmail, enteredCode, newPassword)
            if success:
                print(response.text)
                self.codeValid.emit()
            else:
                QMessageBox.warning(self, "Error", response.text)
        else:
            QMessageBox.warning(self, "Password Mismatch", "Confirm that the new password correctly.")
        
    def handle_backBtn_click(self):
        self.goBack.emit()

# --- MAIN WINDOW ---

class MySoftware(QMainWindow):
    emitRecoveryEmailSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.current_user_id = None
        self.recovery_email = None

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

        # Recieve signals
        self.page_login.loginSuccess.connect(self.handle_login_success)
        self.page_login.forgotPassword.connect(self.go_to_email)
        self.page_login.signupSuccess.connect(self.go_to_selection)
        self.current_username = None
        self.page_enter_email.sendValidEmailToParent.connect(self.go_to_code)
        self.page_enter_email.goBack.connect(self.go_to_login)
        self.page_enter_code.codeValid.connect(self.go_to_home)
        self.page_enter_code.goBack.connect(self.go_to_email)
        self.page_selection.selectionValid.connect(self.go_to_preview)
        self.page_selection.goBack.connect(self.go_to_login)
        self.page_syllabus.goNext.connect(self.go_to_home)
        self.page_syllabus.goBack.connect(self.go_to_selection)

        self.setCentralWidget(self.onboarding_widget)
        self.resize(1100, 700)

        # Add to stack
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_login)      # Index 0
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_enter_email) # Index 1
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_enter_code) # Index 2
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_selection)  # Index 3
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_syllabus)   # Index 4
        self.go_to_login()

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

    def go_to_preview(self):
        data = self.page_selection.preference_payload() 
        sem_val = 1 if data['semester'] == "Odd" else 2
        
        client = BackendClient()
        client.set_academic_context(
            self.current_user_id,
            data['university'],
            data['department'],
            data['year'],
            sem_val
        )

        syllabus_found = self.page_syllabus.load_data()
        
        if syllabus_found:
            self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(self.PREVIEW_PAGE_IND)
        else:
            QMessageBox.warning(self, "Syllabus not found", "No syllabus was found corresponding to the selected information.")

    def go_to_home(self):
        self.main_app = HomePageWrap()
        self.setCentralWidget(self.main_app)
        welcome = self.current_username or "User"
        self.main_app.ui.welcomeUserLabel.setText(f"Welcome, {welcome}!")
        # Clean up memory by destroying the onboarding views
        self.onboarding_widget.deleteLater()
        self.onboarding_widget = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySoftware()
    window.show()
    sys.exit(app.exec())