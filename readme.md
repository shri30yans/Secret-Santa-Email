# Secret Santa Email Bot
This is a script designed to automate the process of organizing Secret Santa events. By taking a .csv file containing the names and emails of participants, the bot randomly assigns each person a Secret Santa and notifies them via email.

## Features
- **Automated Pairing:** Randomly pairs participants ensuring that no one gets their own name.
- **Email Notifications:** Sends out personalized email notifications to each participant with the name of their Secret Santa recipient.
- **Easy to Use:** Simply provide a .csv file with names and emails, and the bot handles the rest.
- **Efficient:** Organize Secret Santa events quickly, in just a few minutes.\

## How to Use
1. **Prepare Your .csv File:** Create a .csv file with two columns: the first for names and the second for email addresses of all participants. Example here. Place this file in the same directory as the script.

2. **Setup the SMTP config:** Configure the SMTP server address, port, and authentication details. (https://support.google.com/accounts/answer/185833)

3. **Run the Bot:** Execute the Secret Santa Bot script. 
`python main.py`.

4. **Check Emails:** Once the bot has run, each participant will receive an email with the name of their Secret Santa recipient.


