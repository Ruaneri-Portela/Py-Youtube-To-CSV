import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
class Auth:
    def Main(Mode):
        if Mode == "1":
            api_key = "AIzaSyA-0KfpLK04NpQN1XghxhSlzG-WkC3DHLs"
            youtube = build("youtube","v3",developerKey=api_key)
            return youtube
        if Mode == "2":
            credentials = None
            # token.pickle stores the user's credentials from previously successful logins
            if os.path.exists("token.pickle"):
             print("Loading Credentials From File...")
             with open("token.pickle", "rb") as token:
                credentials = pickle.load(token)
            
            # If there are no valid credentials available, then either refresh the token or log in.
            if not credentials or not credentials.valid:
             if credentials and credentials.expired and credentials.refresh_token:
                print("Refreshing Access Token...")
                credentials.refresh(Request())
             else:
                print("Fetching New Tokens...")
                flow = InstalledAppFlow.from_client_secrets_file("auth.json",scopes=['https://www.googleapis.com/auth/youtube'])
                flow.run_local_server(port=58698, prompt="consent",authorization_prompt_message="")
                credentials = flow.credentials

                # Save the credentials for the next run
                with open("token.pickle", "wb") as f:
                 print('Saving Credentials for Future Use...')
                 pickle.dump(credentials, f)
            youtube = build("youtube","v3",credentials=credentials)
            return youtube