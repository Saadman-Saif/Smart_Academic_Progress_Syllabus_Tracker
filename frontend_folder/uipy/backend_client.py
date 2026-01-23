import requests

class BackendClient:
    def __init__(self):
        # REPLACE THIS WITH THE CHANGING IP
        self.base_url = "http://192.168.0.102:5000/" 

    def login(self, username, password):
        """
        Sends username and password to server laptop.
        Returns: (Success_Boolean, Message_String)
        """
        url = f"{self.base_url}/login"
        
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
    
    def fetchCourseInfo(self, courseCode):
        url = f"{self.base_url}/syllabus/2-2syllabus_mainCopy"
        parameters = {
            "course_code": courseCode
        }
        print(f"DEBUG: Attempting to connect to: {url}") # <--- Check this line in your terminal
        print(f"DEBUG: With params: {parameters}")
        try:
            response = requests.get(url, params=parameters)

            if response.status_code == 200:
                data = response.json()
                return True, data
            elif response.status_code == 404:
                return False, "Course not found"
            else:
                return False, f"Server Error: {response.status_code}"

        except requests.exceptions.ConnectionError:
            return False, "Connection failed. Is the server running?"
        except Exception as e:
            return False, str(e)