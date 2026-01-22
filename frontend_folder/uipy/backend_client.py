import requests

class BackendClient:
    def __init__(self):
        # REPLACE THIS WITH THE CHANGING IP
        self.base_url = "http://10.149.30.219:5000/" 

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