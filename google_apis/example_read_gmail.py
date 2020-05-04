


import pickle
import json 
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pathlib import Path


JSON_OAUTH_PATH = Path("../credentials/oauth2_client.json")
JSON_USER_CREDENTIALS_PATH = Path("../credentials/python_user_token.json")
PICKLE_USER_CREDENTIALS_PATH = Path("../credentials/python_user_token.pickle")


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(PICKLE_USER_CREDENTIALS_PATH):
        with open(PICKLE_USER_CREDENTIALS_PATH, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                JSON_OAUTH_PATH, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(PICKLE_USER_CREDENTIALS_PATH, 'wb') as token:
            pickle.dump(creds, token)

        # more about the cred object: 
        # https://google-auth.readthedocs.io/en/latest/reference/google.oauth2.credentials.html

        creds_dict = dict()
        creds_dict["token"] = creds.token
        creds_dict["refresh_token"] = creds.refresh_token 
        creds_dict["id_token"] = creds.id_token 
        creds_dict["token_uri"] = creds.token_uri 
        creds_dict["client_id"] = creds.client_id 
        creds_dict["client_secret"] = creds.client_secret


        # Save the credentials for the next run
        with open(JSON_USER_CREDENTIALS_PATH, 'w') as token:
            json.dump(creds_dict, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

if __name__ == '__main__':
    main()