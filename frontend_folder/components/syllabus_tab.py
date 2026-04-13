from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from PySide6.QtCore import Qt, Signal

from components.module_cards import ModuleCard 

class SyllabusTabWrap(QWidget):
    progressUpdated = Signal(int, bool) 
    isEditingRelay = Signal(bool)
    def __init__(self):
        super().__init__()
        self.is_editing = False
        self.cards = [] 

        main_layout = QVBoxLayout(self)
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
            
            card.progressUpdated.connect(self.progressUpdated.emit)
            
            self.cards_layout.addWidget(card)
            self.cards.append(card) 

    def toggle_all_cards(self):
        self.is_editing = not self.is_editing
        self.isEditingRelay.emit(self.is_editing)

        for card in self.cards:
            card.set_edit_mode(self.is_editing)