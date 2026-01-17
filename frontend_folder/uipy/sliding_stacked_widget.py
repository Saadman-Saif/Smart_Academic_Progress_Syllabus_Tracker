from PySide6.QtWidgets import QStackedWidget
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QParallelAnimationGroup, QPoint, Qt

class SlidingStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_direction = Qt.Horizontal
        self.m_speed = 500  # Animation duration in ms
        self.m_animation_type = QEasingCurve.OutCubic # Smooth easing
        self.m_now = 0
        self.m_next = 0
        self.m_wrap = False
        self.m_pnm = False
        self.m_active = False

    def setSpeed(self, speed):
        self.m_speed = speed

    def setAnimation(self, animationtype):
        self.m_animation_type = animationtype

    def slideInIdx(self, index):
        if index > self.count() - 1:
            index = index % self.count()
        elif index < 0:
            index = (index + self.count()) % self.count()
        
        self.slideInWgt(self.widget(index))

    def slideInWgt(self, newwidget):
        if self.m_active:
            return

        self.m_active = True
        _now = self.currentIndex()
        _next = self.indexOf(newwidget)

        if _now == _next:
            self.m_active = False
            return

        offset_x, offset_y = self.frameRect().width(), self.frameRect().height()
        self.widget(_next).setGeometry(self.frameRect())

        # Determine direction based on index (Next vs Back)
        if not self.m_direction == Qt.Horizontal:
            if _now < _next:
                offset_x, offset_y = 0, -offset_y
            else:
                offset_x = 0
        else:
            if _now < _next:
                offset_x, offset_y = -offset_x, 0
            else:
                offset_x, offset_y = offset_x, 0

        pnext = self.widget(_next).pos()
        pnow = self.widget(_now).pos()
        self.m_pnm = pnext

        # Create the New Widget Position (Start from off-screen)
        self.widget(_next).move(pnext.x() - offset_x, pnext.y() - offset_y)
        self.widget(_next).show()
        self.widget(_next).raise_()

        # Create Animation Group
        self.anim_group = QParallelAnimationGroup(self)
        self.anim_group.finished.connect(self.animationDoneSlot)

        # Animate Old Widget leaving
        anim_now = QPropertyAnimation(self.widget(_now), b"pos")
        anim_now.setDuration(self.m_speed)
        anim_now.setEasingCurve(self.m_animation_type)
        anim_now.setStartValue(QPoint(pnow.x(), pnow.y()))
        anim_now.setEndValue(QPoint(pnow.x() + offset_x, pnow.y() + offset_y))
        self.anim_group.addAnimation(anim_now)

        # Animate New Widget entering
        anim_next = QPropertyAnimation(self.widget(_next), b"pos")
        anim_next.setDuration(self.m_speed)
        anim_next.setEasingCurve(self.m_animation_type)
        anim_next.setStartValue(QPoint(pnext.x() - offset_x, pnext.y() - offset_y))
        anim_next.setEndValue(QPoint(pnext.x(), pnext.y()))
        self.anim_group.addAnimation(anim_next)

        self.m_next = _next
        self.m_now = _now
        self.anim_group.start()

    def animationDoneSlot(self):
        self.setCurrentIndex(self.m_next)
        self.widget(self.m_now).hide()
        self.widget(self.m_now).move(self.m_pnm)
        self.m_active = False