from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QPushButton, QLineEdit, QFrame)
from PySide6.QtCore import Qt, Signal
# from module_card import ModuleCard  # Import your new card class!

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QPushButton, QLineEdit, QFrame)
from PySide6.QtCore import Qt, Signal

class ModuleCard(QFrame):
    # --- SIGNALS FOR THE ROOT ---
    # Notice we changed the string to an INT so we can send the exact Topic ID!
    topicDeleted = Signal(int)      # Sends: (Topic ID)
    topicAdded = Signal(int, str)   # Sends: (Module ID, New Topic Name)
    progressUpdated = Signal(int, bool) # Sends: (Topic ID, Is Completed)

    def __init__(self, module_id, module_title, topics_list):
        super().__init__()
        self.module_id = module_id
        self.module_title = module_title
        self.topics = topics_list # This is now a list of dictionaries
        
        self.setStyleSheet("""
            ModuleCard {
                background-color: #333333;
                border-radius: 8px;
                margin-bottom: 10px;
            }
            QLabel { color: #E0E0E0; }
        """)
        
        self.main_layout = QVBoxLayout(self)

        self.header_label = QLabel(self.module_title)
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_label.setStyleSheet("font-weight: bold; background-color: #444444; padding: 5px; border-radius: 4px;")
        self.main_layout.addWidget(self.header_label)

        # 1. Extract just the names for the comma-separated View Mode
        topic_names = [t.get('name', '') for t in self.topics]
        self.view_label = QLabel(", ".join(topic_names))
        self.view_label.setWordWrap(True)
        self.view_label.setStyleSheet("padding: 10px;")
        self.main_layout.addWidget(self.view_label)

        self.edit_container = QWidget()
        self.edit_layout = QVBoxLayout(self.edit_container)
        self.edit_layout.setContentsMargins(0, 10, 0, 0)
        
        self._build_edit_rows() 
        
        self.main_layout.addWidget(self.edit_container)
        self.edit_container.setVisible(False)

    def _build_edit_rows(self):
        # 2. Iterate through the dictionaries
        for topic_dict in self.topics:
            topic_id = topic_dict.get('id')
            topic_name = topic_dict.get('name', 'Unknown')
            # is_completed = topic_dict.get('completed', False) # We will use this when we add checkboxes!
            
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            row_layout.setContentsMargins(10, 0, 10, 0)
            
            topic_label = QLabel(topic_name)
            del_btn = QPushButton("❌")
            del_btn.setFixedSize(24, 24)
            del_btn.setStyleSheet("background-color: transparent; border: none;")
            
            # 3. Emit the precise ID instead of the name!
            del_btn.clicked.connect(lambda checked=False, t_id=topic_id: self.topicDeleted.emit(t_id))
            
            row_layout.addWidget(topic_label)
            row_layout.addStretch()
            row_layout.addWidget(del_btn)
            
            self.edit_layout.addWidget(row_widget)

        self.add_input = QLineEdit()
        self.add_input.setPlaceholderText("Add new topic...")
        self.add_input.setStyleSheet("background-color: #222222; color: white; padding: 5px; border-radius: 4px; margin: 10px;")
        self.add_input.returnPressed.connect(self.handle_add_pressed)
        self.edit_layout.addWidget(self.add_input)

    def handle_add_pressed(self):
        new_text = self.add_input.text().strip()
        if new_text:
            # Emit the Module ID so the backend knows where to put the new topic
            self.topicAdded.emit(self.module_id, new_text)
            self.add_input.clear() 

    def set_edit_mode(self, is_editing: bool):
        self.view_label.setVisible(not is_editing)
        self.edit_container.setVisible(is_editing)

class SyllabusTabWrap(QWidget):
    # --- The Relay Signals ---
    topicDeleted = Signal(str, str) # (Module Title, Topic Name)
    topicAdded = Signal(str, str)   # (Module Title, New Topic Name)

    def __init__(self):
        super().__init__()
        self.is_editing = False
        self.cards = [] # We need to keep a list of the cards to toggle them later

        main_layout = QVBoxLayout(self)

        # 1. The Global Edit Button
        self.edit_btn = QPushButton("✎ Edit Full Syllabus")
        self.edit_btn.setFixedSize(150, 35)
        self.edit_btn.setStyleSheet("background-color: #444444; color: white; border-radius: 5px;")
        self.edit_btn.clicked.connect(self.toggle_all_cards)
        
        # Align button to the right like in your Figma design
        main_layout.addWidget(self.edit_btn, alignment=Qt.AlignmentFlag.AlignRight)

        # 2. Scroll Area (Crucial because expanding cards take up vertical space!)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        
        self.scroll_content = QWidget()
        self.cards_layout = QVBoxLayout(self.scroll_content)
        self.cards_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area)

    # --- TOP-DOWN DATA RECEIVER ---
    def set_syllabus_data(self, course_data):
        # 1. Clear old cards if they exist
        for card in self.cards:
            card.deleteLater()
        self.cards.clear()

        # 2. Build new cards based on the JSON data
        # (Assuming course_data is a dictionary with a 'modules' list)
        for module in course_data.get('modules', []):
            card = ModuleCard(module.get('id'), module.get('title'), module.get('topics', []))
            
            # --- THE SIGNAL RELAY ---
            # When the card shouts, the wrapper immediately shouts the exact same thing to the Root
            card.topicDeleted.connect(self.topicDeleted.emit)
            card.topicAdded.connect(self.topicAdded.emit)
            
            self.cards_layout.addWidget(card)
            self.cards.append(card) # Save it to our list!

    # --- GLOBAL TOGGLE LOGIC ---
    def toggle_all_cards(self):
        self.is_editing = not self.is_editing
        
        # Change button appearance
        if self.is_editing:
            self.edit_btn.setText("Cancel Editing")
            self.edit_btn.setStyleSheet("background-color: #8b0000; color: white; border-radius: 5px;")
        else:
            self.edit_btn.setText("✎ Edit Full Syllabus")
            self.edit_btn.setStyleSheet("background-color: #444444; color: white; border-radius: 5px;")

        # Loop through every card and flip its state!
        for card in self.cards:
            card.set_edit_mode(self.is_editing)