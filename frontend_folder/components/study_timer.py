from PySide6.QtWidgets import (QWidget, QMessageBox, QLabel)
from PySide6.QtCore import (QTimer, Qt)
# Backend
from backend_client import BackendClient

class StudyTimerScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.client = BackendClient()
        self.parentInstance = parent
        self.parentInstance.ui.pauseBtn.setVisible(False)
        self.parentInstance.ui.stopBtn.setVisible(False)
        self.defaultPlannedDuration_Seconds = 3600
        self.total_time = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer_display)
        self.parentInstance.ui.playBtn.clicked.connect(self.handle_playBtn_click)
        self.parentInstance.ui.pauseBtn.clicked.connect(self.handle_pauseBtn_click)
        self.parentInstance.ui.stopBtn.clicked.connect(self.handle_stopBtn_click)
        self.parentInstance.ui.resetBtn.clicked.connect(self.handle_resetBtn_click)
        self.parentInstance.ui.saveSessionBtn.clicked.connect(self.handle_saveSessionBtn_click)

        self.parentInstance.ui.label_3.setVisible(False)
        # 1. Create the label
        self.summary_label = QLabel("Ready to study! Your daily summary will appear here.")
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.summary_label.setWordWrap(True)
        self.summary_label.setStyleSheet("color: #AAAAAA; font-size: 14px; margin-top: 20px;")

        # 2. Inject it into the UI
        self.parentInstance.ui.verticalLayout_7.addWidget(self.summary_label)

    def handle_playBtn_click(self):
        if not self.total_time:
            success, result = self.client.start_study(self.total_time, self.defaultPlannedDuration_Seconds)
            if success:
                print(f"Session started on backend with ID: {result}")
                self.timer.start(1000)
                self.parentInstance.ui.playBtn.setVisible(False)
                self.parentInstance.ui.resetBtn.setVisible(False)
                self.parentInstance.ui.pauseBtn.setVisible(True)
                self.parentInstance.ui.stopBtn.setVisible(True)
            else:
                print(f"Failed to start on backend: {result}")
        else:
            success, result = self.client.resume_study()
            if success:
                # Resume your local QTimer
                self.timer.start(1000)
                self.parentInstance.ui.playBtn.setVisible(False)
                self.parentInstance.ui.resetBtn.setVisible(False)
                self.parentInstance.ui.pauseBtn.setVisible(True)
                self.parentInstance.ui.stopBtn.setVisible(True)
                print("Resumed backend")
            else:
                print(result)

    def handle_resetBtn_click(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Caution")
        msgBox.setInformativeText("Do you want to reset your study session?")
        # reset = msgBox.addButton("Reset", QMessageBox.ButtonRole.AcceptRole)
        # msgBox.addButton(QMessageBox.StandardButton.Cancel)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Reset | QMessageBox.StandardButton.Cancel)
        ret = msgBox.exec()
        if ret == QMessageBox.StandardButton.Reset:
            self.total_time = -1
            self.update_timer_display()
            self.parentInstance.ui.stopBtn.setVisible(False)            

    def handle_pauseBtn_click(self):
        success, result = self.client.pause_study()
        if success:
            print("Paused backend")
            self.timer.stop()
            self.parentInstance.ui.playBtn.setVisible(True)
            self.parentInstance.ui.resetBtn.setVisible(True)
            self.parentInstance.ui.pauseBtn.setVisible(False)
        else:
            print(f"Error: {result}")

    def handle_stopBtn_click(self):
        success, result = self.client.pause_study()
        if success:
            print("Stopped Timer")
            self.timer.stop()
            self.parentInstance.ui.playBtn.setVisible(True)
            self.parentInstance.ui.resetBtn.setVisible(True)
            self.parentInstance.ui.pauseBtn.setVisible(False)
            self.parentInstance.ui.stopBtn.setVisible(False)
        else:
            print(result)

    def update_timer_display(self):
        self.total_time += 1
        hours = self.total_time // 3600
        minutes = (self.total_time % 3600) // 60
        seconds = self.total_time % 60
        timerText = f"<html><head/><body><p>{hours}<span style=\" font-size:24pt;\">hr   </span>{minutes}<span style=\" font-size:24pt;\">min </span>{seconds}<span style=\" font-size:24pt;\">sec</span></p></body></html>" 
        self.parentInstance.ui.timerLabel.setText(timerText)

    def handle_saveSessionBtn_click(self):
        msgbx = QMessageBox()
        msgbx.setWindowTitle("Caution")
        msgbx.setInformativeText("You are about to end the current study session and save the elapsed time. Do you want to save your progress?")
        # reset = msgBox.addButton("Reset", QMessageBox.ButtonRole.AcceptRole)
        # msgBox.addButton(QMessageBox.StandardButton.Cancel)
        msgbx.setStandardButtons(QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel)
        ret = msgbx.exec()
        if ret == QMessageBox.StandardButton.Save:
            # Determine if they finished the timer natively, or hit stop early (interrupted)
            was_interrupted = True # Change this logic based on your timer state
            
            success, result = self.client.stop_study(was_interrupted)
            if success:
                # Reset your local QTimer and UI
                print("Stopped backend")
                self.total_time = -1
                self.update_timer_display()
                
                # Bonus: Automatically fetch the daily summary to update a label!
                self.fetch_summary()
            else:
                print(result)

    def fetch_summary(self):
        success, data = self.client.get_today_summary()
        
        if success:
            print("DEBUG: Raw summary data:", data)
            
            # Extract the data (Change these keys to match your teammate's JSON response!)
            total_time = data.get('total_seconds', 'N/A')
            hours = total_time // 3600
            minutes = (total_time % 3600) // 60
            seconds = total_time % 60
            message = data.get('message', 'Great job today!')

            # Format and display it
            summary_text = f"✅ Session Saved!\n\nToday's Total: {hours} hr {minutes} min {seconds} sec \n{message}"
            self.summary_label.setText(summary_text)
            
            # Make it pop with your yellow theme
            self.summary_label.setStyleSheet("color: #D4D925; font-weight: bold; font-size: 16px; margin-top: 20px;")
        else:
            self.summary_label.setText("Session saved, but could not load daily summary.")
            print(f"Failed to fetch summary: {data}")