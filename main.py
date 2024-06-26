import smtplib
import sys
from time import sleep
import random
import csv
import csv

user = "your_username"
email = "your_email@mail.com"
password = "your_app_psswd"  # Your app password (https://support.google.com/accounts/answer/185833)


smtp_server = "smtp.gmail.com"
port = 587

name_email_pairs = {}

with open("info.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        email = row[1]
        name_email_pairs[name] = email


def find_pairs():
    final_dict = {}  # to:from
    temp_dict = name_email_pairs.copy()
    for reciever in name_email_pairs:
        valid_values = [x for x in temp_dict.keys() if x != reciever]
        # print(reciever, valid_values)
        buyer = random.choice(valid_values)
        temp_dict.pop(buyer)
        final_dict[buyer] = reciever
    return final_dict


print(find_pairs())


def send_emails(final_dict):

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()
        server.login(email, password)
        subject = "PES Secret Santa!"
        for reciever in final_dict:
            giver = final_dict[reciever]
            body = f"Ho ho ho! Chrismas greetings! You have been choosen to be the secret santa for {name_email_pairs[reciever]}.\nEmail: {reciever}"
            msg = "From: " + user + "\nSubject: " + subject + "\n" + body
            server.sendmail(email, giver, msg)
            print(".", end="")
            sleep(1)
        server.quit()
        print("All emails sent!")

    except KeyboardInterrupt:
        print("[-] Canceled")
        sys.exit()
    except smtplib.SMTPAuthenticationError:
        print(
            "\n[!] The username, password or custom STMP server/port you entered is incorrect."
        )
        sys.exit()


final_dict = find_pairs()

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Giver", "Giver Email", "Receiver", "Receiver Email"])
    for receiver in final_dict:
        giver = final_dict[receiver]
        writer.writerow(
            [giver, name_email_pairs[giver], receiver, name_email_pairs[receiver]]
        )

# Uncomment this line if you want to send the emails
# send_emails(final_dict)
