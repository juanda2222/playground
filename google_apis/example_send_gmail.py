


import pickle
import json 
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pathlib import Path

# Import the email modules we'll need
from email.mime.text import MIMEText
import base64

JSON_OAUTH_PATH = Path("../credentials/oauth2_client.json")
JSON_USER_CREDENTIALS_PATH = Path("../credentials/python_user_token.json")
PICKLE_USER_CREDENTIALS_PATH = Path("../credentials/python_user_token.pickle")


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']



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

    def create_message_format():
        """Create a message for an email.

        Args:
            sender: Email address of the sender.
            to: Email address of the receiver.
            subject: The subject of the email message.
            message_text: The text of the email message.

        Returns:
            An object containing a base64url encoded email object.
        """
        message = MIMEText("this is the content of the e mail (might have some html)")
        message['to'] = "juandara2222@gmail.com"
        message['from'] = "juandara2222@gmail.com"
        message['subject'] = "test subject"

        print(">> Message: ",message)
        print(">> Message as string: ", message.as_string())

        message_without_urls = base64.urlsafe_b64encode(message.as_string().encode('utf-8'))
        print(">> Message encoded: ", message_without_urls)
        decoded_again = message_without_urls.decode('utf-8')
        print("Message decoded again: ", decoded_again)
        return {'raw': decoded_again}

    # Call the Gmail API
    message_formated = create_message_format()
    # For attachments see:
    # https://developers.google.com/gmail/api/guides/sending#python_1

    try:
        message = service.users().messages().send(userId="me", body=message_formated).execute()
        print('Message Id: %s' % message['id'])
        print("Returned messaage: ", message)
    except Exception as e:
        print ('An error occurred: %s' % error)
    


if __name__ == '__main__':
    main()