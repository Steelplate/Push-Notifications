# notification_service/service.py

import yaml
import urllib
import requests
import http.client

class Service:
    def __init__(self, config_file: str):
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
            self.user_id = config.get("user_id")
            self.api_key = config.get("api_key")

        if self.user_id is None:
            raise ValueError("User ID not found in configuration file.")
        
        if self.api_key is None:
            raise ValueError("API key not found in configuration file.")

    def notification(self, message: str, image_filepath: str = None):
        """Send a notification to the Pushover service."""

        if image_filepath:
            with open(image_filepath, "rb") as img:
                response = requests.post(
                    "https://api.pushover.net/1/messages.json", 
                    data={
                        "token": self.api_key,
                        "user": self.user_id,
                        "message": message
                    },
                    files={
                        "attachment": ("image.jpg", img, "image/jpeg")
                    }
                )

            return response.status_code == 200
        else:
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json", 
                         urllib.parse.urlencode({
                             "token": self.api_key,
                             "user": self.user_id,
                             "message": message
                         }), 
                         { "Content-type": "application/x-www-form-urlencoded" })

            return conn.getresponse().status == 200
