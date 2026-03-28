import requests


class BackendClient:
    shared_session = requests.Session()

    def __init__(self):
        # REPLACE THIS WITH THE CHANGING IP
        self.base_url = "http://192.168.0.104:5000/"
        self.req_session = BackendClient.shared_session

    def signup(self, username, email, password):
        url = f"{self.base_url}signup"

        payload = {
            "username": username,
            "email": email,
            "password": password,
        }

        response = self.req_session.post(url, json=payload, timeout=5)

        if response.status_code == 201:
            data = response.json()
            user_id = data.get("user_id")
            uname = data.get("username")
            return True, "Account Created Successfully", user_id, uname
        elif response.status_code == 409:
            return False, "Email already exists", None, None
        else:
            return False, f"Failed somewhere, error code: {response.status_code}", None, None

    def login(self, email, password):
        url = f"{self.base_url}login"

        payload = {
            "email": email,
            "password": password,
        }

        try:
            response = self.req_session.post(url, json=payload, timeout=5)

            if response.status_code == 200:
                data = response.json()
                user_id = data.get("user_id")
                username = data.get("username")
                return True, "Login Successful", user_id, username
            elif response.status_code == 401:
                return False, "Invalid Username or Password", None, None
            else:
                return False, f"Server Error: {response.status_code}", None, None

        except requests.exceptions.ConnectionError:
            return False, "Could not connect to server.", None, None
        except Exception as e:
            return False, f"An error occurred: {str(e)}", None, None

    def get_me(self):
        """Fetch current user from study.db via session cookie (same as login/signup session)."""
        url = f"{self.base_url}me"
        try:
            response = self.req_session.get(url, timeout=5)
            if response.status_code == 200:
                return True, response.json()
            try:
                err = response.json()
            except ValueError:
                err = response.text
            return False, err
        except Exception as e:
            return False, str(e)

    def sendCode(self, recoveryEmail):
        """Function used to send recovery code to provided email"""
        url = f"{self.base_url}forgot-password"
        payload = {
            "email": recoveryEmail,
        }
        try:
            response = self.req_session.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                return True, "Code sent successfully"
            else:
                return False, f"Error code: {response.status_code}"
        except Exception as e:
            return False, f"Connection Error: {str(e)}"

    def processEnteredCode(self, email, enteredCode, newPass):
        """Checks the validity of the code entered by the user"""
        url = f"{self.base_url}reset-password"
        payload = {
            "email": email,
            "code": enteredCode,
            "new_password": newPass,
        }

        response = self.req_session.post(url, json=payload, timeout=10)
        try:
            if response.status_code == 400 or response.status_code == 401 or response.status_code == 404:
                return False, response
            elif response.status_code == 200:
                return True, response
        except Exception as e:
            return False, f"Connection Error: {str(e)}"

    def get_syllabus(self):
        """
        Syllabus is scoped by the logged-in session (server reads users.university, etc.).
        """
        url = f"{self.base_url}syllabus"

        try:
            response = self.req_session.get(url, timeout=5)
            if response.status_code == 200:
                return True, response.json()
            try:
                err = response.json()
            except ValueError:
                err = response.text
            return False, err
        except Exception as e:
            return False, str(e)

    def set_academic_context(self, user_id, uni, dept, year, sem):
        url = f"{self.base_url}set-academic-context"
        payload = {
            "user_id": user_id,
            "university": uni,
            "department": dept,
            "year": int(year),
            "semester": int(sem),
        }
        try:
            self.req_session.post(url, json=payload)
            return True
        except Exception:
            return False
        
    def get_ct_marks(self, courseCode):
        url = f"{self.base_url}ct/{courseCode}"

        try:
            response = self.req_session.get(url, timeout=5)
            if response.status_code == 200:
                return True, response.json()
            try:
                err = response.json()
            except ValueError:
                err = response.text
            return False, err
        except Exception as e:
            return False, str(e)

    def set_ct_marks(self, courseCode, ctNo, mark):
        url = f"{self.base_url}ct/update"
        payload = {
            "course_code": courseCode,
            "ct_number": ctNo,
            "mark": mark
        }
        try:
            response = self.req_session.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                return True, response.json()
            try:
                err = response.json()
            except ValueError:
                err = response.text
            return False, err
        except Exception as e:
            return False, str(e)

    def send_topic_completion(self, topicId):
        url = f"{self}update-completion"
        payload = {
            "topic_id": topicId,
            "completed": 1
        }
        try:
            response = self.req_session.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                return True, response.json()
            try:
                err = response.json()
            except ValueError:
                err = response.text
            return False, err
        except Exception as e:
            return False, str(e)


    def fetch_course_completion(self, courseId):
        url = f"{self.base_url}course/{courseId}"
        try:
            response = self.req_session.get(url, timeout=5)
            if response.status_code == 200:
                return True, response.json() # "total_topics, completed, percentage, topics"
            try:
                err = response.json()
            except ValueError:
                err = response.text
            return False, err
        except Exception as e:
            return False, str(e)

    def start_study(self, elapsedTime_Seconds):
        url = f"{self.base_url}study/start"
        payload = {"duration": elapsedTime_Seconds}
        try:
            response = self.req_session.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                return True, response.json().get("session_id")
            return False, response.json().get("error")
        except Exception as e:
            return False, str(e)

    def pause_study(self):
        url = f"{self.base_url}study/pause"
        try:
            response = self.req_session.post(url, timeout=5)
            return response.status_code == 200, response.json()
        except Exception as e:
            return False, str(e)

    def resume_study(self):
        url = f"{self.base_url}study/resume"
        try:
            response = self.req_session.post(url, timeout=5)
            return response.status_code == 200, response.json()
        except Exception as e:
            return False, str(e)

    def stop_study(self, interrupted=True):
        url = f"{self.base_url}study/stop"
        payload = {"interrupted": interrupted}
        try:
            response = self.req_session.post(url, json=payload, timeout=5)
            return response.status_code == 200, response.json()
        except Exception as e:
            return False, str(e)

    def get_today_summary(self):
        url = f"{self.base_url}study/today-summary"
        try:
            response = self.req_session.get(url, timeout=5)
            if response.status_code == 200:
                return True, response.json()
            return False, response.json().get("error")
        except Exception as e:
            return False, str(e)
