import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QLineEdit, QHBoxLayout, QPushButton, QMessageBox, QSizePolicy, QFrame, QVBoxLayout, QLabel, QScrollArea)
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

#------ Wrappers ------
#------ Authentication Page ------
class LoginPageWrap(QWidget):
    loginSuccess = Signal(int, str)
    forgotPassword = Signal()
    signupSuccess = Signal(int, str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.client = BackendClient()
        self.ui.signupFrame.setVisible(False)

        # Connect the buttons
        self.ui.login_btn.clicked.connect(self.handle_login_click)
        self.ui.forgot_password_label.linkActivated.connect(self.handle_link_click)
        self.ui.signup_btn.clicked.connect(self.handle_signup_click)
        self.ui.signupLinkLabel.linkActivated.connect(self.handle_signupLinkLabel_click)
        self.ui.backToLoginBtn.clicked.connect(self.handle_backToLoginBtn_click)
    
    def handle_signupLinkLabel_click(self):
        self.ui.loginFrame.setVisible(False)
        self.ui.signupFrame.setVisible(True)

    def handle_backToLoginBtn_click(self):
        self.ui.loginFrame.setVisible(True)
        self.ui.signupFrame.setVisible(False)

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

#------ Selection Page ------
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

#------ Syllabus Preview Page ------
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

    # A sort of setter function for the syllabus data
    def build_and_place_cards(self, data):
        # Backend GET /syllabus returns a JSON array of courses (not {"syllabus": [...]})
        if isinstance(data, list):
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

        module_html = "<ul style='font-size: 14px;'>" 
        for module in course.get('modules', []):
            module_html += f"<li>{module.get('title', '')}</li>"
        module_html += "</ul>"

        module_lbl = QLabel(module_html, scroll_content)
        module_lbl.setWordWrap(True)
        scroll_layout.addWidget(module_lbl)
        scroll_layout.addStretch() # Pushes text to the top

        card_layout.addWidget(body_scroll)

        self.ui.gridLayout.addWidget(card_frame, 1, col_idx, 1, 1)

#------ Landing Page ------
class HomePageWrap(QWidget):
    sendUpdatedMarks = Signal(str, list)
    loadCTMarks = Signal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        # self.build_dynamic_cards()
        self.avgMark = 0
        self.allMarks = []
        self.timerScreenInstance = StudyTimerScreen(parent=self)

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
   
#------ Home Tab ------
class EditMarksDialog(QDialog):
    def __init__(self, course_name, parent=None):
        super().__init__(parent)
        self.courseCode = course_name
        self.setWindowTitle(f"Edit Marks for {course_name}")
        self.setFixedSize(300, 200)
        
        layout = QVBoxLayout(self)
        
        self.instruction = QLabel("Enter new CT marks:")
        self.marks_input_ct1 = QLineEdit()
        self.marks_input_ct2 = QLineEdit()
        self.marks_input_ct3 = QLineEdit()
        self.marks_input_ct4 = QLineEdit()
        
        btn_layout = QHBoxLayout()
        self.save_btn = QPushButton("Save")
        self.cancel_btn = QPushButton("Cancel")
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.cancel_btn)
        
        layout.addWidget(self.instruction)
        layout.addWidget(self.marks_input_ct1)
        layout.addWidget(self.marks_input_ct2)
        layout.addWidget(self.marks_input_ct3)
        layout.addWidget(self.marks_input_ct4)
        layout.addLayout(btn_layout)
        
        self.save_btn.clicked.connect(self.accept) 
        self.cancel_btn.clicked.connect(self.reject) 

    # Getter function for the backend
    def get_new_marks(self):
        return self.marks_input_ct1.text(), self.marks_input_ct2.text(), self.marks_input_ct3.text(), self.marks_input_ct4.text()

class CTAverageCard(QFrame):
    cardClicked = Signal(str)
    
    def __init__(self, course_name, avg_mark, ct_marks, parent=None):
        super().__init__(parent)
        self.courseName = course_name
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)
        self.setObjectName(u"cardFrame") # Keeps stylesheet targeting
        
        layout = QVBoxLayout(self)

        self.courseCodeLabel = QLabel(course_name)
        self.courseCodeLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.courseCodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        self.courseCodeLabel.setSizePolicy(sizePolicy3)
        
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.courseCodeLabel.setFont(font2)
        
        layout.addWidget(self.courseCodeLabel)

        self.markLabel = QLabel(str(avg_mark))
        self.markLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.markLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(48)
        font3.setBold(True)
        self.markLabel.setFont(font3)
        
        layout.addWidget(self.markLabel)

        for ctNo, marks in enumerate(ct_marks):
            ctLabel = QLabel(f"CT{ctNo + 1}: {marks}")
            ctLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
            ctLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            font4 = QFont()
            font4.setFamilies([u"Inter"])
            font4.setPointSize(10)
            ctLabel.setFont(font4)
            
            layout.addWidget(ctLabel)
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.cardClicked.emit(self.courseName) 
        super().mouseReleaseEvent(event)

#------ Syllabus Tab ------
# class ModuleTopicCard(QWidget):

# class 

#------ Study Timer Tab ------
class StudyTimerScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.client = BackendClient()
        self.parentInstance = parent
        self.parentInstance.ui.pauseBtn.setVisible(False)
        self.parentInstance.ui.stopBtn.setVisible(False)
        self.defaultPlannedDuration_Seconds = 3600
        self.elapsedTime_Seconds = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer_display)
        self.parentInstance.ui.playBtn.clicked.connect(self.handle_playBtn_click)
        self.parentInstance.ui.pauseBtn.clicked.connect(self.handle_pauseBtn_click)
        self.parentInstance.ui.stopBtn.clicked.connect(self.handle_stopBtn_click)
        self.parentInstance.ui.resetBtn.clicked.connect(self.handle_resetBtn_click)
        self.parentInstance.ui.saveSessionBtn.clicked.connect(self.handle_saveSessionBtn_click)

    def handle_playBtn_click(self):
        if not self.elapsedTime_Seconds:
            success, result = self.client.start_study(self.elapsedTime_Seconds, self.defaultPlannedDuration_Seconds)
            if success:
                print(f"Session started on backend with ID: {result}")
                self.timer.start(1000)
                self.parentInstance.ui.playBtn.setVisible(False)
                self.parentInstance.ui.resetBtn.setVisible(False)
                self.parentInstance.ui.pauseBtn.setVisible(True)
                self.parentInstance.ui.stopBtn.setVisible(True)
            else:
                print(f"Failed to start on backend: {result}")
        else:
            success, result = self.client.resume_study()
            if success:
                # Resume your local QTimer
                self.timer.start(1000)
                self.parentInstance.ui.playBtn.setVisible(False)
                self.parentInstance.ui.resetBtn.setVisible(False)
                self.parentInstance.ui.pauseBtn.setVisible(True)
                self.parentInstance.ui.stopBtn.setVisible(True)
                print("Resumed backend")
            else:
                print("Error resuming timer")

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
        success, result = self.client.pause_study()
        if success:
            print("Paused backend")
            self.timer.stop()
            self.parentInstance.ui.playBtn.setVisible(True)
            self.parentInstance.ui.resetBtn.setVisible(True)
            self.parentInstance.ui.pauseBtn.setVisible(False)
        else:
            print(f"Error: {result}")

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
                print(result)

    def fetch_summary(self):
        success, data = self.client.get_today_summary()
        if success:
            print("Today's Summary:", data)
            # Update a label like: self.parent.ui.summaryLabel.setText(...)


#------ Forgot Password ------
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

#------ MAIN WINDOW ------
class MySoftware(QMainWindow):
    emitRecoveryEmailSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.current_user_id = None
        self.recovery_email = None
        self.current_user_syllabus = None

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
        self.main_app.sendUpdatedMarks.connect(self.update_ct_marks_and_cardsFrame)
        self.main_app.loadCTMarks.connect(self.load_ct_marks)
        self.setCentralWidget(self.main_app)
        welcome = self.current_username or "User"
        self.main_app.ui.welcomeUserLabel.setText(f"Welcome, {welcome}!")

        # Request course code value from backend to then request ct marks from the backend against those courses
        success = self.load_syllabus()
        # print(self.current_user_syllabus)
        if success:
            self.main_app.fill_in_cardsFrame(self.current_user_syllabus)
            # for course in self.current_user_syllabus:
            #     success, allMarks, avgMark, ctCount = self.load_ct_marks(course.get('course_code'))
            #     self.main_app.build_dynamic_cards(course.get('course_code'), avgMark, allMarks)
        
        # Clean up memory by destroying the onboarding views
        self.onboarding_widget.deleteLater()
        self.onboarding_widget = None

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySoftware()
    window.show()
    sys.exit(app.exec())