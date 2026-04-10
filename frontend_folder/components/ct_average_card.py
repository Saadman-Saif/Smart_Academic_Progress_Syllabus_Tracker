from PySide6.QtWidgets import (QSizePolicy, QFrame, QVBoxLayout, QLabel)
from PySide6.QtCore import (Qt, Signal)
from PySide6.QtGui import QFont

class CTAverageCard(QFrame):
    cardClicked = Signal(str)
    
    def __init__(self, course_name, avg_mark, ct_marks, parent=None):
        super().__init__(parent)
        self.courseName = course_name
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)
        self.setObjectName(u"cardFrame") # Keeps stylesheet targeting
        
        layout = QVBoxLayout(self)

        self.courseCodeLabel = QLabel(course_name)
        self.courseCodeLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.courseCodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        self.courseCodeLabel.setSizePolicy(sizePolicy3)
        
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.courseCodeLabel.setFont(font2)
        
        layout.addWidget(self.courseCodeLabel)

        self.markLabel = QLabel(str(avg_mark))
        self.markLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.markLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(48)
        font3.setBold(True)
        self.markLabel.setFont(font3)
        
        layout.addWidget(self.markLabel)

        for ctNo, marks in enumerate(ct_marks):
            ctLabel = QLabel(f"CT{ctNo + 1}: {marks}")
            ctLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
            ctLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            font4 = QFont()
            font4.setFamilies([u"Inter"])
            font4.setPointSize(10)
            ctLabel.setFont(font4)
            
            layout.addWidget(ctLabel)
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.cardClicked.emit(self.courseName) 
        super().mouseReleaseEvent(event)