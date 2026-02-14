class StudySession:
    def __init__(
        self,
        session_id,
        date,
        start_ts,
        end_ts,
        planned_duration,
        actual_duration,
        status
    ):
        self.session_id = session_id
        self.date = date
        self.start_ts = start_ts
        self.end_ts = end_ts
        self.planned_duration = planned_duration
        self.actual_duration = actual_duration
        self.status = status


class RunningSession:
    def __init__(
        self,
        session_id,
        start_ts,
        planned_duration,
        total_paused,
        last_pause_ts,
        status
    ):
        self.session_id = session_id
        self.start_ts = start_ts
        self.planned_duration = planned_duration
        self.total_paused = total_paused
        self.last_pause_ts = last_pause_ts
        self.status = status
