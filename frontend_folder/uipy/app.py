import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
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
        self.ui.myButton.clicked.connect(self.handle_login_click)
        self.ui.label_9.linkActivated.connect(self.handle_link_click)
    
    def handle_login_click(self):
        # Get the text from the boxes
        user_text = self.ui.lineEdit.text()
        pass_text = self.ui.lineEdit_2.text()

        # Visual Feedback
        self.ui.myButton.setText("Connecting...")
        self.ui.myButton.setEnabled(False)
        QApplication.processEvents() # Force update UI

        # Send the data to the backend
        success, message = self.client.login(user_text, pass_text)

        # Handle the result
        self.ui.myButton.setText("Login")
        self.ui.myButton.setEnabled(True)

        if success:
            print("Login worked!")
            self.main_window.go_to_selection()
        else:
            # Show an error popup
            QMessageBox.warning(self, "Login Failed", message)

    def handle_link_click(self, link_url):        
        if link_url == "register_page":
            print("Switching to Register Page...")
            self.uiOnboardingStackPage.stackedWidget.setCurrentIndex()
            
        elif link_url == "forgot_password":
            print("Opening Forgot Password dialog...")

class InstDeptYearSemPageWrap(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_instDeptYearSemSelection()
        self.ui.setupUi(self)
        # self.ui.nextBtn.clicked.connect(self.form_submission)
        

class SyllabusPreviewPageWrap(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SyllabusPreview()
        self.ui.setupUi(self)

class HomePageWrap(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)

# --- MAIN WINDOW ---

class MySoftware(QMainWindow):
    def __init__(self):
        super().__init__()
        
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
        self.page_selection.ui.backBtn.clicked.connect(self.go_to_login)

    def go_to_login(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(0)
        # self.uiOnboardingStackPage.stackedWidget.slideInIdx(0)
    def go_to_selection(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(1)
        # self.uiOnboardingStackPage.stackedWidget.slideInIdx(1)
    def go_to_preview(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(2)
        # self.uiOnboardingStackPage.stackedWidget.slideInIdx(2)
    def go_to_home(self):
        self.uiOnboardingStackPage.stackedWidget.setCurrentIndex(3)
        # self.uiOnboardingStackPage.stackedWidget.slideInIdx(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySoftware()
    window.show()
    sys.exit(app.exec())