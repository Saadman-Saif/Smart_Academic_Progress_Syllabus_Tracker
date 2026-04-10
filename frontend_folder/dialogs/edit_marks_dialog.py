from PySide6.QtWidgets import (QDialog, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout, QLabel)

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