import json
import os
import requests


class BackendClient:
    shared_session = requests.Session()

    def __init__(self):
        # REPLACE THIS WITH THE CHANGING IP
        self.base_url = "http://192.168.0.103:5000/"
        self.req_session = BackendClient.shared_session
        self.COOKIE_FILE = "session_data.json"
        self.load_cookies()

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
            self.save_cookies()
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
                self.save_cookies()
                return True, "Login Successful", user_id, username
            elif response.status_code == 401:
                return False, "Invalid Username or Password", None, None
            else:
                return False, f"Server Error: {response.status_code}", None, None

        except requests.exceptions.ConnectionError:
            return False, "Could not connect to server.", None, None
        except Exception as e:
            return False, f"An error occurred: {str(e)}", None, None
        
    def save_cookies(self):
        """Saves the current session cookies to a local file."""
        try:
            with open(self.COOKIE_FILE, 'w') as f:
                # Convert the session cookies into a simple dictionary and save as JSON
                json.dump(self.req_session.cookies.get_dict(), f)
            print("DEBUG: Session cookies saved to disk.")
        except Exception as e:
            print(f"DEBUG: Failed to save cookies: {e}")

    def load_cookies(self):
        """Loads cookies from the local file into the session."""
        try:
            if os.path.exists(self.COOKIE_FILE):
                with open(self.COOKIE_FILE, 'r') as f:
                    cookies = json.load(f)
                    # Inject the loaded cookies back into the shared session
                    self.req_session.cookies.update(cookies)
                print("DEBUG: Session cookies loaded from disk.")
        except Exception as e:
            print(f"DEBUG: Failed to load cookies: {e}")

    def is_logged_in(self):
        url = f"{self.base_url}check-session"
        try:
            response = self.req_session.get(url, timeout=5)
            print(f"DEBUG: Server returned status code {response.status_code}")
            print(f"DEBUG: Raw server response: {response.text}")
            isLoggedIn = response.json().get("logged_in")
            if response.status_code == 200:
                print(isLoggedIn)
                print("200")
                return True, isLoggedIn, response.json()
            if response.status_code == 401:
                print(isLoggedIn)
                print("401")
                return True, isLoggedIn, response.json()
            try:
                err = response.text
            except ValueError:
                err = response.text
            return False, False, err
        except Exception as e:
            return False, False, str(e)
        
    def logout(self):
        # 1. Ping the backend to destroy the server-side session (optional but best practice)
        url = f"{self.base_url}logout" 
        try:
            self.req_session.post(url)
        except Exception:
            pass # We don't care if this fails, we force the local logout anyway!

        # 2. Clear the cookies from Python's RAM
        self.req_session.cookies.clear()
        
        # 3. Delete the saved cookie file from the hard drive!
        try:
            import os
            if os.path.exists(self.COOKIE_FILE):
                os.remove(self.COOKIE_FILE)
                print("DEBUG: Local session cookie deleted.")
        except Exception as e:
            print(f"DEBUG: Could not delete cookie file: {e}")
            
        return True

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
        
    def update_topic_completion(self, topic_id, is_completed):
        url = f"{self.base_url}/update-completion"
        payload = {
            "topic_id": topic_id,
            "completed": is_completed # Python boolean becomes JSON true/false
        }
        
        try:
            response = self.req_session.post(url, json=payload)
            if response.status_code == 200:
                return True, response.json()
            else:
                return False, response.json().get("error", "Failed to update completion")
        except Exception as e:
            return False, str(e)
        
    def upload_routine(self, user_id, file_path):
        url = f"{self.base_url}routine/upload"
        try:
            # Open file in binary read mode
            with open(file_path, 'rb') as f:
                files = {'file': f}
                data = {'user_id': user_id}
                # requests handles the multipart/form-data headers automatically!
                response = self.req_session.post(url, files=files, data=data)
                
            return response.status_code == 200, response.json()
        except Exception as e:
            return False, str(e)

    def get_routine_info(self, user_id):
        url = f"{self.base_url}routine/{user_id}"
        try:
            response = self.req_session.get(url)
            return response.status_code == 200, response.json()
        except Exception as e:
            return False, str(e)

    # def add_topic(self, module_id, topic_name):
    #     url = f"{self.base_url}/add-topic"
    #     payload = {"module_id": module_id, "name": topic_name}
        
    #     try:
    #         response = self.session.post(url, json=payload)
    #         if response.status_code == 200:
    #             return True, response.json()
    #         return False, response.json().get("error", "Failed to add topic")
    #     except Exception as e:
    #         return False, str(e)

    # def delete_topic(self, topic_id):
    #     url = f"{self.base_url}/delete-topic"
    #     payload = {"topic_id": topic_id}
        
    #     try:
    #         # Using POST here is often easier for simple Flask JSON APIs than DELETE
    #         response = self.session.post(url, json=payload) 
    #         if response.status_code == 200:
    #             return True, response.json()
    #         return False, response.json().get("error", "Failed to delete topic")
    #     except Exception as e:
    #         return False, str(e)

    # def send_topic_completion(self, topicId):
    #     url = f"{self}update-completion"
    #     payload = {
    #         "topic_id": topicId,
    #         "completed": 1
    #     }
    #     try:
    #         response = self.req_session.post(url, json=payload, timeout=5)
    #         if response.status_code == 200:
    #             return True, response.json()
    #         try:
    #             err = response.json()
    #         except ValueError:
    #             err = response.text
    #         return False, err
    #     except Exception as e:
    #         return False, str(e)


    # def fetch_course_completion(self, courseId):
    #     url = f"{self.base_url}course/{courseId}"
    #     try:
    #         response = self.req_session.get(url, timeout=5)
    #         if response.status_code == 200:
    #             return True, response.json() # "total_topics, completed, percentage, topics"
    #         try:
    #             err = response.json()
    #         except ValueError:
    #             err = response.text
    #         return False, err
    #     except Exception as e:
    #         return False, str(e)

    def start_study(self, elapsedTime_Seconds, defaultPlannedDuration_Seconds):
        url = f"{self.base_url}study/start"
        payload = {
            "duration": elapsedTime_Seconds,
            "planned_duration": defaultPlannedDuration_Seconds 
        }
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

    def stop_study(self, interrupted=False):
        url = f"{self.base_url}study/stop"
        payload = {"interrupted": interrupted}
        try:
            response = self.req_session.post(url, timeout=5)
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
