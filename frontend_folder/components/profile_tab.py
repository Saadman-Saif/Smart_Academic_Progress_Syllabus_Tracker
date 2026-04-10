from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton
from PySide6.QtCore import Qt, Signal

class ProfileTabWrap(QWidget):
    logoutRelay = Signal()
    def __init__(self, api_client, user_id):
        super().__init__()
        self.client = api_client
        self.user_id = user_id
        
        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        # Styles
        label_style = "font-size: 16px; color: #AAAAAA; font-weight: bold;"
        value_style = "font-size: 16px; color: white;"
        
        # Create empty labels
        self.name_lbl = QLabel("Loading...")
        self.email_lbl = QLabel("Loading...")
        self.uni_lbl = QLabel("Loading...")
        self.dept_lbl = QLabel("Loading...")
        self.year_lbl = QLabel("Loading...")
        self.sem_lbl = QLabel("Loading...")
        
        # Apply style to all values
        for lbl in [self.name_lbl, self.email_lbl, self.uni_lbl, self.dept_lbl, self.year_lbl, self.sem_lbl]:
            lbl.setStyleSheet(value_style)
        
        # Add them to the form (Row Title -> Row Value)
        form_layout.addRow(QLabel(f"<span style='{label_style}'>Name:</span>"), self.name_lbl)
        form_layout.addRow(QLabel(f"<span style='{label_style}'>Email:</span>"), self.email_lbl)
        form_layout.addRow(QLabel(f"<span style='{label_style}'>University:</span>"), self.uni_lbl)
        form_layout.addRow(QLabel(f"<span style='{label_style}'>Department:</span>"), self.dept_lbl)
        form_layout.addRow(QLabel(f"<span style='{label_style}'>Year:</span>"), self.year_lbl)
        form_layout.addRow(QLabel(f"<span style='{label_style}'>Semester:</span>"), self.sem_lbl)
        
        main_layout.addLayout(form_layout)

        # 1. Create the Logout Button
        self.logout_btn = QPushButton("🚪 Logout")
        self.logout_btn.setFixedSize(200, 40)
        self.logout_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #A31621; 
                color: white; 
                font-weight: bold; 
                border-radius: 4px; 
                margin-top: 30px;
            }
            QPushButton:hover { background-color: #D32F2F; }
        """)
        
        # 2. Add it to the layout and connect it
        main_layout.addWidget(self.logout_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.logout_btn.clicked.connect(self.handle_logout)

        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop) # Pushes everything to the top
        
        # Fetch the data immediately on startup
        self.load_profile_data()

    def load_profile_data(self):
        success, data = self.client.get_me()
        if success:
            # Change these strings ('username', 'email', etc.) to match 
            # the exact keys your teammate's JSON dictionary sends back!
            self.name_lbl.setText(data.get('username', 'N/A'))
            self.email_lbl.setText(data.get('email', 'N/A'))
            self.uni_lbl.setText(data.get('university', 'N/A'))
            self.dept_lbl.setText(data.get('department', 'N/A'))
            # self.year_lbl.setText(data.get('year', 'N/A'))
            # self.sem_lbl.setText(data.get('semester', 'N/A'))
        else:
            self.name_lbl.setText("Error loading profile.")
            print(f"DEBUG: Failed to load profile: {data}")
        
    def handle_logout(self):
        self.logout_btn.setText("Logging out...")
        self.client.logout()       # Destroy the cookies
        self.logoutRelay.emit()    # Tell the Home Page to close! 