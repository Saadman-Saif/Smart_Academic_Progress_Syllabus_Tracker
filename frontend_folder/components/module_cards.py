from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QFrame, QCheckBox)
from PySide6.QtCore import Qt, Signal

class ModuleCard(QFrame):
    # ONLY the progress signal remains!
    progressUpdated = Signal(int, bool) 

    def __init__(self, module_id, module_title, topics_list):
        super().__init__()
        self.module_id = module_id
        self.module_title = module_title
        self.topics = topics_list
        
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

        # The Comma-Separated View Label
        topic_names = [t.get('name', '') for t in self.topics]
        self.view_label = QLabel(", ".join(topic_names))
        self.view_label.setWordWrap(True)
        self.view_label.setStyleSheet("padding: 10px;")
        self.main_layout.addWidget(self.view_label)

        self.edit_container = QWidget()
        self.edit_layout = QVBoxLayout(self.edit_container)
        self.edit_layout.setContentsMargins(10, 10, 10, 10)
        
        self._build_edit_rows() 
        
        self.main_layout.addWidget(self.edit_container)
        self.edit_container.setVisible(False)

    def _build_edit_rows(self):
        # Build the clean list of Checkboxes
        for topic_dict in self.topics:
            topic_id = topic_dict.get('id')
            topic_name = topic_dict.get('name', 'Unknown')
            is_completed = topic_dict.get('completed', False) 
            
            checkbox = QCheckBox(topic_name)
            checkbox.setChecked(is_completed)
            checkbox.setStyleSheet("color: white; padding: 2px;")
            
            # Emit the ID and state!
            checkbox.toggled.connect(lambda checked, t_id=topic_id: self.progressUpdated.emit(t_id, checked))
            
            self.edit_layout.addWidget(checkbox)

    def set_edit_mode(self, is_editing: bool):
        self.view_label.setVisible(not is_editing)
        self.edit_container.setVisible(is_editing)
        
        # Force the UI to stretch
        self.updateGeometry()
        if self.parentWidget():
            self.parentWidget().adjustSize()