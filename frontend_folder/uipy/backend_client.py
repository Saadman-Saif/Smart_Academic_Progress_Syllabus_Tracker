import requests

class BackendClient:
    def __init__(self):
        # REPLACE THIS WITH THE CHANGING IP
        self.base_url = "http://192.168.0.105:5000/" 

    def signup(self, username, email, password):
        url = f"{self.base_url}signup"

        payload = {
            "username": username,
            "email": email,
            "password": password
        }

        response = requests.post(url, json=payload, timeout=5)

        if response.status_code == 201:
            return True, "Account Created Successfully"
        else:
            return False, f"Failed somewhere, error code: {response.status_code}"


    def login(self, username, password):
        """
        Sends username and password to server laptop.
        Returns: (Success_Boolean, Message_String)
        """
        url = f"{self.base_url}login"
        
        payload = {
            "email": username,
            "password": password
        }

        try:
            # Send the request (wait max 5 seconds)
            response = requests.post(url, json=payload, timeout=5)
            
            # Check if the backend said "OK" (Status Code 200)
            if response.status_code == 200:
                return True, "Login Successful"
            elif response.status_code == 401:
                return False, "Invalid Username or Password"
            else:
                return False, f"Server Error: {response.status_code}"

        except requests.exceptions.ConnectionError:
            return False, "Could not connect to server."
        except Exception as e:
            return False, f"An error occurred: {str(e)}"
    
    def get_syllabus(self, email):
        """
        Backend expects only email. It looks up the Uni/Year/Sem 
        from the database automatically.
        """
        url = f"{self.base_url}/get-syllabus"
        payload = {"email": email} 
        
        try:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                return True, response.json()
            else:
                return False, response.text
        except Exception as e:
            return False, str(e)
        
    def set_academic_context(self, email, uni, dept, year, sem):
        url = f"{self.base_url}/set-academic-context"
        payload = {
            "email": email,
            "university": uni,
            "department": dept,
            "year": int(year),
            "semester": int(sem) # Logic to convert "Odd"/"Even" to 1/2 handled in UI
        }
        try:
            requests.post(url, json=payload)
            return True
        except:
            return False