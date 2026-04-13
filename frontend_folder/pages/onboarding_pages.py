from PySide6.QtWidgets import (QWidget, QSizePolicy, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea)
from PySide6.QtCore import (QSize, Qt, Signal, QRect)
from PySide6.QtGui import QFont

from uipy.inst_dept_year_semesterWidget import Ui_instDeptYearSemSelection
from uipy.syllabus_previewWidget import Ui_SyllabusPreview
from backend_client import BackendClient

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

    def reset_syllabus_cards(self):
        self.ui.horizontalLayout.removeWidget(self.ui.scrollAreaWidgetContents)
        self.ui.scrollAreaWidgetContents = QWidget()
        self.ui.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1407, 388))
        self.ui.horizontalLayout = QHBoxLayout(self.ui.scrollAreaWidgetContents)
        

    # A sort of setter function for the syllabus data
    def build_and_place_cards(self, data):
        # Backend GET /syllabus returns a JSON array of courses (not {"syllabus": [...]})
        if isinstance(data, list):
            syllabus_list = data
            print("Syllabus loaded:", len(syllabus_list)) 

            for col_idx, course in enumerate(syllabus_list):
                self._create_course_card(course, col_idx)
            self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
            return True
        else:
            print(data)
            return False

    def _create_course_card(self, course, col_idx):
        # Main Card Frame
        card_frame = QFrame(self.ui.scrollAreaWidgetContents)
        card_frame.setMinimumSize(QSize(270, 359))
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

        self.ui.horizontalLayout.addWidget(card_frame)