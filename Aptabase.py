import requests
import uuid
from datetime import datetime
import platform

class init:
    def __init__(self, token, version, debug, host="https://eu.aptabase.com"):
        self.api_token = token
        self.host = host
        self.session_id = str(uuid.uuid4())

        self.system_props = {
            "isDebug": bool(debug),
            "osName": str(platform.system()),
            "osVersion": str(platform.version()),
            "appVersion": str(version),
            "appBuildNumber": '1',
            "sdkVersion": 'aptabase_python@0.1.0'
        }

    def track(self, event_name, event_props={}):
        event_data = {
            "eventName": event_name,
            "props": event_props,
            "sessionId": self.session_id,
            "systemProps": self.system_props,
            "timestamp": datetime.now().isoformat()
        }

        url = f"{self.host}/api/v0/event"
        headers = {
            'Content-Type': 'application/json',
            'App-Key': self.api_token,
        }

        try:
            response = requests.post(url, headers=headers, json=event_data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Some wild error occured:", e)