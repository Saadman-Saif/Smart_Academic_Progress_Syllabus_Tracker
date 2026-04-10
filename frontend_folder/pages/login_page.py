from PySide6.QtWidgets import (QApplication, QWidget, QMessageBox)
from PySide6.QtCore import Signal

from uipy.authpageWidget import Ui_LoginScreen
from uipy.forgotPasswordEnterEmail import Ui_EnterEmail
from uipy.forgotPasswordEnterCodeNewPass_ui import Ui_EnterCodeNewPass
from backend_client import BackendClient

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