
//const fs = require('fs');
//const readline = require('readline');
//const {google} = require('googleapis');
//
//// If modifying these scopes, delete token.json.
//const SCOPES = ['https://www.googleapis.com/auth/gmail.readonly'];
//// The file token.json stores the user's access and refresh tokens, and is
//// created automatically when the authorization flow completes for the first
//// time.
//
//
//const JSON_OAUTH_PATH = "../credentials/oauth2_client.json"
//const JSON_USER_CREDENTIALS_PATH = "../credentials/node_user_token.json"
////PICKLE_USER_CREDENTIALS_PATH = "../credentials/user_token.pickle"
//
//
//// Load client secrets from a local file.
//fs.readFile(JSON_OAUTH_PATH, (err, content) => {
//  if (err) return console.log('Error loading client secret file:', err);
//  // Authorize a client with credentials, then call the Gmail API.
//  authorize(JSON.parse(content), listLabels);
//});
//
///**
// * Create an OAuth2 client with the given credentials, and then execute the
// * given callback function.
// * @param {Object} credentials The authorization client credentials.
// * @param {function} callback The callback to call with the authorized client.
// */
//function authorize(credentials, callback) {
//  const {client_secret, client_id, redirect_uris} = credentials.installed;
//  const oAuth2Client = new google.auth.OAuth2(
//      client_id, client_secret, redirect_uris[0]);
//
//  // Check if we have previously stored a token.
//  let token_raw;
//  try {
//    token_raw = fs.readFileSync(JSON_USER_CREDENTIALS_PATH);  
//  } catch (error) {
//    console.log("Error loading the saved token!")
//    token_raw = getNewToken(oAuth2Client, callback);
//  }
//
//  console.log("setting credentials...")
//  oAuth2Client.setCredentials(JSON.parse(token_raw));
//  callback(oAuth2Client);
//  
//}
//
///**
// * Get and store new token after prompting for user authorization, and then
// * execute the given callback with the authorized OAuth2 client.
// * @param {google.auth.OAuth2} oAuth2Client The OAuth2 client to get token for.
// * @param {getEventsCallback} callback The callback for the authorized client.
// */
//function getNewToken(oAuth2Client, callback) {
//
//  const authUrl = oAuth2Client.generateAuthUrl({
//    access_type: 'offline',
//    scope: SCOPES,
//  });
//  
//  console.log('Authorize this app by visiting this url:', authUrl);
//  const rl = readline.createInterface({
//    input: process.stdin,
//    output: process.stdout,
//  });
//  
//  rl.question('Enter the code from that page here: ', (code) => {
//    rl.close();
//    oAuth2Client.getToken(code, (err, token) => {
//      if (err) return console.error('Error retrieving access token', err);
//      oAuth2Client.setCredentials(token);
//      // Store the token to disk for later program executions
//      fs.writeFile(JSON_USER_CREDENTIALS_PATH, JSON.stringify(token), (err) => {
//        if (err) return console.error(err);
//        console.log('Token stored to', JSON_USER_CREDENTIALS_PATH);
//      });
//      callback(oAuth2Client);
//    });
//  });
//}
//
///**
// * Lists the labels in the user's account.
// *
// * @param {google.auth.OAuth2} auth An authorized OAuth2 client.
// */
//function listLabels(auth) {
//  const gmail = google.gmail({version: 'v1', auth});
//  gmail.users.labels.list({
//    userId: 'me',
//  }, (err, res) => {
//    if (err) return console.log('The API returned an error: ' + err);
//    const labels = res.data.labels;
//    if (labels.length) {
//      console.log('Labels:');
//      labels.forEach((label) => {
//        console.log(`- ${label.name}`);
//      });
//    } else {
//      console.log('No labels found.');
//    }
//  });
//}
  
//module.exports = Mail_manager_insecure







const inquirer = require('inquirer')
const fs = require('fs');
const readline = require('readline');
const {google} = require('googleapis');

// If modifying these scopes, delete token.json.
const SCOPES = [
  'https://www.googleapis.com/auth/gmail.readonly',
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
async function read_labels() {

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

  //use the saved autentiaction client to run the gmail api:
  const gmail = google.gmail({version: 'v1', auth: oAuth2Client});
  gmail.users.labels.list({
    userId: 'me',
  }, (err, res) => {
    if (err) return console.log('The API returned an error: ' + err);
    const labels = res.data.labels;
    if (labels.length) {
      console.log('Labels:');
      labels.forEach((label) => {
        console.log(`- ${label.name}`);
      });
    } else {
      console.log('No labels found.');
    }
  });



}

/**
 * Get and store new token after prompting for user authorization, and then
 * execute the given callback with the authorized OAuth2 client.
 * @param {google.auth.OAuth2} oAuth2Client The OAuth2 client to get token for.
 * @param {getEventsCallback} callback The callback for the authorized client.
 */
async function getNewToken(oAuth2Client) {

  
}


//if the module is main execute the example
if (module === require.main) {
  read_labels()
}

module.exports = read_labels;


