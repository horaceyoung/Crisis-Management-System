from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tweepy

CONSUMER_KEY ="ojjWC47FsOrdkKiQxfITL9FwC"
CONSUMER_SECRET = "2pQqgJvVjcczubPHjiBxEKkYZFjWQ4gOoqiTV0u1phE2UyY9Da"
ACCESS_KEY = "1053928436874395648-UM3wmevzmLOJZsQYIt2WvHj64Y5qEY"
ACCESS_SECRET = "8veJe3ZLy382zYthP1gt6k0rh6aMnTt3HZ4OoD0FcMBC0"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitterApi = tweepy.API(auth)

senderEmail = '8paxemailservice@gmail.com'
password = '-?.8JG,/zrazT)x*'


account_sid = "AC911c8d07cb467d8f69f4a933362de87e"
auth_token  = "63911216647d96067015c43c4f42eac5"

client = Client(account_sid, auth_token)


class InformationSender:
    def send_sms(self, sms, phoneNumber):
        message = client.messages.create(
            to=phoneNumber,
            from_="+12674788252",
            body=sms)

        print(message.sid)
        print("SMS to " + phoneNumber + " sent.")
        del message

    def send_email(self, subject, email, recipient):
        msg = MIMEMultipart()
        msg['From'] = senderEmail
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(email, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senderEmail, password)
        text = msg.as_string()
        server.sendmail(senderEmail, recipient, text)
        server.quit()
        print("Email to " + recipient + " sent.")
        del msg
        del text

    def send_tweet(self, tweet):
        twitterApi.update_status(tweet)
        print(tweet + " sent.")

