import time
import uuid
from db import get_db

class StudyTimerService:
#start of a session
    def start_session(self, user_id):
        """
        Starts a new study session.
        """

        conn = get_db()
        cursor = conn.cursor()

        # Safety: do not allow multiple running sessions
        cursor.execute("""
            SELECT session_id 
            FROM running_session 
            WHERE user_id = ?
        """, (user_id,))
        if cursor.fetchone():
            conn.close()
            raise Exception("A study session is already running")

        now = int(time.time())
        session_id = str(uuid.uuid4())
        today = time.strftime("%Y-%m-%d")

        # Insert into study_session table
        cursor.execute("""
            INSERT INTO study_session (
                session_id,user_id, date, start_ts,status
            ) VALUES (?, ?, ?, ?, ?)
        """, (
            session_id,
            user_id,
            today,
            now,
            "RUNNING"
        ))

        # Insert into running_session table
        cursor.execute("""
            INSERT INTO running_session (
                session_id,user_id, start_ts,
                total_paused, status
            ) VALUES (?, ?, ?, ?, ?)
        """, (
            session_id,
            user_id,
            now,
            0,
            "RUNNING"
        ))

        conn.commit()
        conn.close()

        return session_id
# pausing 
    def pause_session(self, user_id):
        """
        Pauses the currently running study session.
        """
        conn = get_db()
        cursor = conn.cursor()

        # Get running session
        cursor.execute("""
            SELECT status
            FROM running_session
            WHERE user_id = ?
        """, (user_id,))
        row = cursor.fetchone()

        if not row:
            conn.close()
            raise Exception("No running session to pause")

        if row["status"] != "RUNNING":
            conn.close()
            raise Exception("Session is not running")

        now = int(time.time())

        # Update running session to paused
        cursor.execute("""
            UPDATE running_session
            SET last_pause_ts = ?, status = ?
            WHERE user_id = ?
        """, (
            now,
            "PAUSED",
            user_id
        ))

        conn.commit()
        conn.close()
# resuming
    def resume_session(self, user_id):
        """
        Resumes a paused study session.
        """

        conn = get_db()
        cursor = conn.cursor()

        # Get paused session
        cursor.execute("""
            SELECT  last_pause_ts, total_paused, status
            FROM running_session
            WHERE user_id = ?
        """, (user_id,))
        row = cursor.fetchone()

        if not row:
            conn.close()
            raise Exception("No running session found")

        if row["status"] != "PAUSED":
            conn.close()
            raise Exception("Session is not paused")

        now = int(time.time())

        paused_duration = now - row["last_pause_ts"]
        new_total_paused = row["total_paused"] + paused_duration

        # Update running session
        cursor.execute("""
            UPDATE running_session
            SET total_paused = ?, last_pause_ts = NULL, status = ?
            WHERE user_id = ?
        """, (
            new_total_paused,
            "RUNNING",
            user_id
        ))

        conn.commit()
        conn.close()
# stopping
    def stop_session(self, user_id, interrupted=False):
        """
        Stops the current study session.
        interrupted=True means user stopped early.
        """

        conn = get_db()
        cursor = conn.cursor()

        # Get running session
        cursor.execute("""
            SELECT session_id, start_ts, total_paused, status, last_pause_ts
            FROM running_session
            WHERE user_id = ?
        """, (user_id,))
        row = cursor.fetchone()

        if not row:
            conn.close()
            raise Exception("No running session to stop")

        now = int(time.time())

        if row["status"] == "PAUSED":
            paused_duration = now - row["last_pause_ts"]
            total_paused = row["total_paused"] + paused_duration
        else:
            total_paused = row["total_paused"]

        duration = (now - row["start_ts"]) - total_paused
        if duration < 0:
            duration = 0

        final_status = "INTERRUPTED" if interrupted else "COMPLETED"

        # Update study_session
        cursor.execute("""
            UPDATE study_session
            SET end_ts = ?, actual_duration = ?, status = ?
            WHERE session_id = ?
        """, (
            now,
            duration,
            final_status,
            row["session_id"]
        ))

        # Remove running session
        cursor.execute("""
            DELETE FROM running_session
            WHERE user_id = ?
        """, (user_id,))

        conn.commit()
        conn.close()

    def get_today_summary(self,user_id):
        """
        Returns total study time and session count for today.
        """

        conn = get_db()
        cursor = conn.cursor()

        today = time.strftime("%Y-%m-%d")

        cursor.execute("""
            SELECT COUNT(*) as session_count,
                COALESCE(SUM(actual_duration), 0) as total_seconds
            FROM study_session
            WHERE date = ? AND user_id = ?
        """, (today, user_id))

        row = cursor.fetchone()

        conn.close()

        return {
            "date": today,
            "total_seconds": row["total_seconds"],
            "session_count": row["session_count"]
        }