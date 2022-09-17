import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Auth:
    def Main(Mode):
        # To use non-google auth accont
        if Mode == "1":
            with open("api_key.dat") as f:
                api_key = f.read()
                f.close()
            youtube = build("youtube", "v3", developerKey=api_key)
            return youtube
        # To use on google auth on accont
        if Mode == "2":
            credentials = None
            # Check If Token Pickle (Googe Login) Exist
            if os.path.exists("token.pickle"):
                print("Loading Credentials From File...")
                with open("token.pickle", "rb") as token:
                    credentials = pickle.load(token)

            # Case Not, Re-get Google Credential
            if not credentials or not credentials.valid:
                if credentials and credentials.expired and credentials.refresh_token:
                    print("Refreshing Access Token...")
                    credentials.refresh(Request())
                else:
                    print("Fetching New Tokens...")
                    flow = InstalledAppFlow.from_client_secrets_file(
                        "auth.json", scopes=['https://www.googleapis.com/auth/youtube'])
                    flow.run_local_server(
                        port=58698, prompt="consent", authorization_prompt_message="")
                    credentials = flow.credentials

                    # Save Credential For Next Run
                    with open("token.pickle", "wb") as f:
                        print('Saving Credentials for Future Use...')
                        pickle.dump(credentials, f)
            youtube = build("youtube", "v3", credentials=credentials)
            return youtube