from PySide6.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

class ShadowFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Auto-apply shadow on creation
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setYOffset(14)
        self.setGraphicsEffect(shadow)