from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QScrollArea
from PySide6.QtCore import Qt, Signal
from module_cards import ModuleCard 

class SyllabusTabWrap(QWidget):
    # ONLY the progress relay remains!
    progressUpdated = Signal(int, bool) 

    def __init__(self):
        super().__init__()
        self.is_editing = False
        self.cards = [] 

        main_layout = QVBoxLayout(self)

        self.edit_btn = QPushButton("✎ Update Progress")
        self.edit_btn.setFixedSize(150, 35)
        self.edit_btn.setStyleSheet("background-color: #444444; color: white; border-radius: 5px;")
        self.edit_btn.clicked.connect(self.toggle_all_cards)
        
        main_layout.addWidget(self.edit_btn, alignment=Qt.AlignmentFlag.AlignRight)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        
        self.scroll_content = QWidget()
        self.cards_layout = QVBoxLayout(self.scroll_content)
        self.cards_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area)

    def set_syllabus_data(self, course_data):
        for card in self.cards:
            card.deleteLater()
        self.cards.clear()

        for module in course_data.get('modules', []):
            card = ModuleCard(module.get('id'), module.get('title'), module.get('topics', []))
            
            # Connect ONLY the progress signal
            card.progressUpdated.connect(self.progressUpdated.emit)
            
            self.cards_layout.addWidget(card)
            self.cards.append(card) 

    def toggle_all_cards(self):
        self.is_editing = not self.is_editing
        
        if self.is_editing:
            self.edit_btn.setText("Close Progress Editor")
            self.edit_btn.setStyleSheet("background-color: #005f73; color: white; border-radius: 5px;") # Nice teal color
        else:
            self.edit_btn.setText("✎ Update Progress")
            self.edit_btn.setStyleSheet("background-color: #444444; color: white; border-radius: 5px;")

        for card in self.cards:
            card.set_edit_mode(self.is_editing)