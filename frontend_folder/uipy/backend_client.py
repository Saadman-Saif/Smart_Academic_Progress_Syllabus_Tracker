import requests

class BackendClient:
    shared_session = requests.Session()
    def __init__(self):
        # REPLACE THIS WITH THE CHANGING IP
        self.base_url = "http://192.168.0.102:5000/"
        self.req_session = BackendClient.shared_session

    def signup(self, username, email, password):
        url = f"{self.base_url}signup"

        payload = {
            "username": username,
            "email": email,
            "password": password
        }

        response = self.req_session.post(url, json=payload, timeout=5)

        if response.status_code == 201:
            data = response.json()
            user_id = data.get("user_id")
            return True, "Account Created Successfully", user_id
        elif response.status_code == 409:
            return False, "Email already exists", None
        else:
            return False, f"Failed somewhere, error code: {response.status_code}", None


    def login(self, username, password):
        url = f"{self.base_url}login"
        
        payload = {
            "email": username,
            "password": password
        }

        try:
            # Send the request (wait max 5 seconds)
            response = self.req_session.post(url, json=payload, timeout=5)
            
            # Check if the backend said "OK" (Status Code 200)
            if response.status_code == 200:
                data = response.json()
                user_id = data.get("user_id")
                return True, "Login Successful", user_id
            elif response.status_code == 401:
                return False, "Invalid Username or Password", None
            else:
                return False, f"Server Error: {response.status_code}", None

        except self.req_session.exceptions.ConnectionError:
            return False, "Could not connect to server."
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
        
    def sendCode(self, recoveryEmail):
        """Function used to send recovery code to provided email"""
        url = f"{self.base_url}forgot-password"
        payload = {
            "email": recoveryEmail
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
            "new_password": newPass
        }

        response = self.req_session.post(url, json=payload, timeout=10)
        try:
            if response.status_code == 400 or response.status_code == 401 or response.status_code == 404:
                return False, response
            elif response.status_code == 200:
                return True, response
        except Exception as e:
            return False, f"Connection Error: {str(e)}"
    
    def get_syllabus(self, user_id):
        """
        Backend expects only email. It looks up the Uni/Year/Sem 
        from the database automatically.
        """
        url = f"{self.base_url}courses"
        # payload = {"user_id": user_id} 
        
        try:
            response = self.req_session.get(url, timeout=5)
            print(response)
            if response.status_code == 200:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)
        
    def set_academic_context(self, user_id, uni, dept, year, sem):
        url = f"{self.base_url}/set-academic-context"
        payload = {
            "user_id": user_id,
            "university": uni,
            "department": dept,
            "year": int(year),
            "semester": int(sem) # Logic to convert "Odd"/"Even" to 1/2 handled in UI
        }
        try:
            self.req_session.post(url, json=payload)
            return True
        except:
            return False

    def start_study(self, elapsedTime_Seconds):
        url = f"{self.base_url}/study/start"
        payload = {"duration": elapsedTime_Seconds}
        try:
            # Notice we use self.req_session here!
            response = self.req_session.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                return True, response.json().get("session_id")
            return False, response.json().get("error")
        except Exception as e:
            return False, str(e)

    def pause_study(self):
        url = f"{self.base_url}/study/pause"
        try:
            response = self.req_session.post(url, timeout=5)
            return response.status_code == 200, response.json()
        except Exception as e:
            return False, str(e)

    def resume_study(self):
        url = f"{self.base_url}/study/resume"
        try:
            response = self.req_session.post(url, timeout=5)
            return response.status_code == 200, response.json()
        except Exception as e:
            return False, str(e)

    def stop_study(self, interrupted=False):
        url = f"{self.base_url}/study/stop"
        payload = {"interrupted": interrupted}
        try:
            response = self.req_session.post(url, json=payload, timeout=5)
            return response.status_code == 200, response.json()
        except Exception as e:
            return False, str(e)

    def get_today_summary(self):
        url = f"{self.base_url}/study/today-summary"
        try:
            # Notice this one is a GET request!
            response = self.req_session.get(url, timeout=5)
            if response.status_code == 200:
                return True, response.json()
            return False, response.json().get("error")
        except Exception as e:
            return False, str(e)