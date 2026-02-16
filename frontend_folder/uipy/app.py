import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QSizePolicy, QFrame, QVBoxLayout, QLabel, QScrollArea
from PySide6.QtCore import QSize, QCoreApplication, Qt, QRect
from PySide6.QtGui import QFont
# Imports
from onboarding import Ui_AppName
from authpageWidget import Ui_LoginScreen
from inst_dept_year_semesterWidget import Ui_instDeptYearSemSelection
from syllabus_previewWidget import Ui_SyllabusPreview
from homepageWidget import Ui_HomePage
from backend_client import BackendClient

# --- WRAPPERS ---

class LoginPageWrap(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        # Store a reference to the main window so we can change pages
        self.main_window = main_window
        
        # Initialize the connection to the backend
        self.client = BackendClient()

        # Connect the button
        self.ui.login_btn.clicked.connect(self.handle_login_click)
        self.ui.forgot_password_label.linkActivated.connect(self.handle_link_click)
        self.ui.signup_btn.clicked.connect(self.handle_singup_click)
    
    def handle_login_click(self):
        # Get the text from the boxes
        user_text = self.ui.login_email_lineedit.text()
        pass_text = self.ui.login_password_lineedit.text()

        # Visual Feedback
        self.ui.login_btn.setText("Connecting...")
        self.ui.login_btn.setEnabled(False)
        QApplication.processEvents() # Force update UI

        # Send the data to the backend
        success, message = self.client.login(user_text, pass_text)

        # Handle the result
        self.ui.login_btn.setText("Login")
        self.ui.login_btn.setEnabled(True)

        if success:
            print("Login worked!")
            MySoftware.handle_login_success(self.main_window, email=user_text)
        else:
            # Show an error popup
            QMessageBox.warning(self, "Login Failed", message)

    def handle_link_click(self, link_url):        
        if link_url == "register_page":
            print("Switching to Register Page...")
            self.main_window.uiOnboardingStackPage.stackedWidget.setCurrentIndex(0)
            
        elif link_url == "forgot_password":
            print("Opening Forgot Password dialog...")

    def handle_singup_click(self):
        username = self.ui.signup_username_lineedit.text()
        email = self.ui.signup_email_lineedit.text()
        password = self.ui.signup_password_lineedit.text()

        success, response = self.client.signup(username, email, password)

        if success:
            print("Signup worked!")
            self.main_window.handle_login_success(email=email)
        else:
            # Show an error popup
            QMessageBox.warning(self, "Login Failed", response)
            

class InstDeptYearSemPageWrap(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_instDeptYearSemSelection()
        self.ui.setupUi(self)

    def preference_payload(self):        
        uni = self.ui.universityComboBox.currentText()
        dept = self.ui.departmentComboBox.currentText()
        year = self.ui.yearComboBox.currentText()
        semester = self.ui.semesterComboBox.currentText()
        
        return {
            "university": uni,
            "department": dept,
            "year": year,
            "semester": semester
        }

class SyllabusPreviewPageWrap(QWidget,):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SyllabusPreview()
        self.ui.setupUi(self)
        self.client = BackendClient()
        # DELETED: The API call that was crashing the app

    def load_data(self, user_email):
        """
        Called by Main Window when the user arrives at this page.
        """
        print(f"Fetching syllabus for {user_email}...")
        success, data = self.client.get_syllabus(user_email)
        
        if success:
            if len(data['syllabus']) != 0:
                print("Syllabus loaded:", len(data['syllabus'])) 
                cardNo = 0
                for i in data['syllabus']:
                    self.ui.cardFrame = QFrame(self.ui.gridFrame)
                    self.ui.cardFrame.setObjectName(u"cardFrame")
                    sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
                    sizePolicy3.setHorizontalStretch(1)
                    sizePolicy3.setVerticalStretch(1)
                    sizePolicy3.setHeightForWidth(self.ui.cardFrame.sizePolicy().hasHeightForWidth())
                    self.ui.cardFrame.setSizePolicy(sizePolicy3)
                    self.ui.cardFrame.setMinimumSize(QSize(188, 359))
                    self.ui.cardFrame.setStyleSheet(u"background-color: rgb(50, 50, 50);")
                    self.ui.cardFrame.setFrameShape(QFrame.Shape.StyledPanel)
                    self.ui.cardFrame.setFrameShadow(QFrame.Shadow.Raised)
                    self.ui.verticalLayout = QVBoxLayout(self.ui.cardFrame)
                    self.ui.verticalLayout.setObjectName(u"verticalLayout")
                    self.ui.header = QFrame(self.ui.cardFrame)
                    self.ui.header.setObjectName(u"header")
                    self.ui.header.setStyleSheet(u"background-color: rgb(75, 75, 75)")
                    self.ui.header.setFrameShape(QFrame.Shape.StyledPanel)
                    self.ui.header.setFrameShadow(QFrame.Shadow.Raised)
                    self.ui.header.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

                    # Text within the header of the card
                    self.ui.courseCode = QLabel(self.ui.header)
                    self.ui.courseCode.setObjectName(u"courseCode")
                    self.ui.courseCode.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
                    font1 = QFont()
                    font1.setFamilies([u"Inter"])
                    font1.setPointSize(12)
                    font1.setBold(True)
                    self.ui.courseCode.setFont(font1)
                    self.ui.verticalLayout_8 = QVBoxLayout(self.ui.header)
                    self.ui.verticalLayout_8.setObjectName(u"verticalLayout_8")
                    self.ui.verticalLayout_8.addWidget(self.ui.courseCode)

                    self.ui.courseTitle = QLabel(self.ui.header)
                    self.ui.courseTitle.setObjectName(u"courseTitle")
                    font2 = QFont()
                    font2.setFamilies([u"Inter"])
                    self.ui.courseTitle.setFont(font2)
                    self.ui.courseTitle.setWordWrap(True)
                    self.ui.courseTitle.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

                    self.ui.verticalLayout_8.addWidget(self.ui.courseTitle)

                    self.ui.verticalLayout.addWidget(self.ui.header)

                    self.ui.body = QScrollArea(self.ui.cardFrame)
                    self.ui.body.setObjectName(u"body")
                    self.ui.body.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                    self.ui.body.setEnabled(True)
                    self.ui.body.setWidgetResizable(True)
                    self.ui.bodyScrollAreaWidgetContent = QWidget()
                    self.ui.bodyScrollAreaWidgetContent.setObjectName(u"bodyScrollAreaWidgetContent")
                    sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
                    sizePolicy4.setHorizontalStretch(0)
                    sizePolicy4.setVerticalStretch(1)
                    sizePolicy4.setHeightForWidth(self.ui.body.sizePolicy().hasHeightForWidth())
                    self.ui.body.setSizePolicy(sizePolicy4)
                    self.ui.body.setStyleSheet(u"background-color: rgb(60, 60, 60)")
                    self.ui.body.setFrameShape(QFrame.Shape.StyledPanel)
                    self.ui.body.setFrameShadow(QFrame.Shadow.Raised)

                    # Text within the body of the card (actual syllabus)
                    self.ui.moduleTitle = QLabel(self.ui.body)
                    self.ui.moduleTitle.setObjectName(u"moduleTitle")
                    self.ui.moduleTitle.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
                    self.ui.moduleTitle.setWordWrap(True)
                    moduleTitleText = "<ul style='font-size: 14px;'>" 
                    moduleNo = 0
                    for module in data['syllabus'][cardNo]['modules']:
                        moduleTitleText += f"<li>{data['syllabus'][cardNo]['modules'][moduleNo]['title']}</li>"
                        moduleNo += 1
                    moduleTitleText += "</ul>"
                    self.ui.moduleTitle.setText(QCoreApplication.translate("SyllabusPreview", moduleTitleText, None))
                    self.ui.moduleTitle.setScaledContents(True)
                    # self.ui.scrollArea = QScrollArea(self.ui.frame_2)
                    # self.ui.scrollArea.setObjectName(u"scrollArea")
                    # self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                    # self.ui.scrollArea.setWidgetResizable(True)
                    # self.ui.scrollAreaWidgetContents_2 = QWidget()
                    # self.ui.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
                    # self.ui.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1112, 224))
                    # self.ui.verticalLayout_5 = QVBoxLayout(self.ui.scrollAreaWidgetContents_2)
                    # self.ui.verticalLayout_5.setObjectName(u"verticalLayout_5")
                    # self.ui.label_3 = QLabel(self.ui.scrollAreaWidgetContents_2)
                    # self.ui.label_3.setObjectName(u"label_3")
                    # self.ui.label_3.setMinimumSize(QSize(0, 100))

                    # self.ui.verticalLayout_5.addWidget(self.ui.label_3)

                    # self.ui.label_4 = QLabel(self.ui.scrollAreaWidgetContents_2)
                    # self.ui.label_4.setObjectName(u"label_4")
                    # self.ui.label_4.setMinimumSize(QSize(0, 100))

                    # self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents_2)

                    # self.ui.verticalLayout_4.addWidget(self.ui.scrollArea)

                    self.ui.verticalLayout.addWidget(self.ui.body)

                    self.ui.gridLayout.addWidget(self.ui.cardFrame, 1, cardNo, 1, 1)

                    self.ui.courseCode.setText(QCoreApplication.translate("SyllabusPreview", data['syllabus'][cardNo]['course_code'], None))
                    self.ui.courseTitle.setText(QCoreApplication.translate("SyllabusPreview", data['syllabus'][cardNo]['course_name'], None))
                    cardNo += 1
                return True
            else:
                return False

        else:
            print("Error loading syllabus:", data)
        


class HomePageWrap(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)

# --- MAIN WINDOW ---

class MySoftware(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_user_email = None
        # 1. Setup Main Container (The Stack)
        self.uiOnboardingStackPage = Ui_AppName()
        self.uiOnboardingStackPage.setupUi(self)

        # 2. Setup Pages
        self.page_login = LoginPageWrap(self)
        self.page_selection = InstDeptYearSemPageWrap()
        self.page_syllabus = SyllabusPreviewPageWrap()
        self.page_home = HomePageWrap()

        # 3. Add pages to Stack
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_login)      # Index 0
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_selection)  # Index 1
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_syllabus)   # Index 2
        self.uiOnboardingStackPage.stackedWidget.addWidget(self.page_home)       # Index 3
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(0)

        # 4. Connect Buttons
        # Note the extra ".ui" in the path to get to the button
        # self.page_login.ui.myButton.clicked.connect(self.go_to_selection)
        self.page_selection.ui.nextBtn.clicked.connect(self.go_to_preview)
        self.page_selection.ui.backBtn.clicked.connect(self.go_to_login)
        self.page_syllabus.ui.nextBtn.clicked.connect(self.go_to_home)
        self.page_syllabus.ui.backBtn.clicked.connect(self.go_to_selection)

    def handle_login_success(self, email):
        # You need to update LoginPageWrap to pass the email back to here
        self.current_user_email = email
        print(self.current_user_email)
        self.go_to_selection()

    def go_to_login(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(0)
        # self.uiOnboardingStackPage.stackedWidget.slideInIdx(0)
    def go_to_selection(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(1)
        # self.uiOnboardingStackPage.stackedWidget.slideInIdx(1)
    def go_to_preview(self):
        # 1. Get data from Selection Page Wrapper
        data = self.page_selection.preference_payload() # This returns the dict
        
        # 2. Convert Sem to Int (Odd=1, Even=2)
        sem_val = 1 if data['semester'] == "Odd" else 2

        # 3. Send to Backend to SAVE context
        client = BackendClient()
        client.set_academic_context(
            self.current_user_email,
            data['university'],
            data['department'],
            data['year'],
            sem_val
        )

        # 4. Now tell the preview page to LOAD
        syllabusFound = self.page_syllabus.load_data(self.current_user_email)
        
        if syllabusFound:
            self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(2)
        else:
            QMessageBox.warning(self, "Syllabus not found", "No syllabus was found corresponding to the selected information.")
        # self.uiOnboardingStackPage.stackedWidget.slideInIdx(2)
    def go_to_home(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(3)
        # self.uiOnboardingStackPage.stackedWidget.slideInIdx(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySoftware()
    window.show()
    sys.exit(app.exec())