

const inquirer = require('inquirer')
const fs = require('fs');
const readline = require('readline');
const {google} = require('googleapis');

// If modifying these scopes, delete token.json.
const SCOPES = [
  'https://www.googleapis.com/auth/gmail.send',
];
// The file token.json stores the user's access and refresh tokens, and is
// created automatically when the authorization flow completes for the first
// time.

const TOKEN_PATH = "../credentials/node_user_token.json";
const JSON_OAUTH_PATH = "../credentials/oauth2_client.json"


/**
 * Create an OAuth2 client with the given credentials, and then execute the
 * given callback function.
 */
async function send_mail() {

  // Load client secrets from a local file.
  var creds_content = JSON.parse(fs.readFileSync(JSON_OAUTH_PATH))
  const {client_secret, client_id, redirect_uris} = creds_content.installed;
  const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);


  // Check if we have previously stored a token.
  try {
    var token = JSON.parse(fs.readFileSync(TOKEN_PATH))
    console.log("Saved token: ", token)

  // Autenticate and save one if there is not one allready saved:
  } catch (error) {
    console.log(">> Error reading token, creating new one")

    //get the token using a url generator and the code authentication:
    const authUrl = oAuth2Client.generateAuthUrl({
      access_type: 'offline',
      scope: SCOPES,
    });
    console.log('Authorize this app by visiting this url:', authUrl);
    var questions = [{
      type: 'input',
      name: 'code',
      message: 'Enter the code from that page here: ',
    }]

    //get the code from command line
    var answers = await inquirer.prompt(questions)
    console.log(`the code received is: ${answers['code']}!`)

    //get the token using the code:
    var token = await oAuth2Client.getToken(answers['code'])
    
    // Store the token to disk for later program executions
    fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
      if (err) return console.error(err);
      console.log('Token stored to', TOKEN_PATH);
    });
  }

  // pass the credentials to the oauth object manager:
  oAuth2Client.setCredentials(token.tokens);

  
  
  // You can use UTF-8 encoding for the subject using the method below.
  // You can also just use a plain string if you don't need anything fancy.
  const subject = '🤘 Hello 🤘';
  const utf8Subject = `=?utf-8?B?${Buffer.from(subject).toString('base64')}?=`;
  const messageParts = [
    'From: <juandara2222@gmail.com>',
    'To: <juandara2222@gmail.com>',
    'Content-Type: text/html; charset=utf-8',
    'MIME-Version: 1.0',
    `Subject: ${utf8Subject}`,
    '',
    'This is a message just to say hello.',
    'So... <b>Hello!</b>  🤘❤️😎',
  ];
  const message = messageParts.join('\n');

  // The body needs to be base64url encoded.
  const encodedMessage = Buffer.from(message)
    .toString('base64')
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=+$/, '');

  const gmail = google.gmail({version: 'v1', auth: oAuth2Client});

  const res = await gmail.users.messages.send({
    userId: 'me',
    requestBody: {
      raw: encodedMessage,
    },
  });
  console.log(">> res data: ", res.data);


}



//if the module is main execute the example
if (module === require.main) {
  send_mail()
}

module.exports = send_mail;


