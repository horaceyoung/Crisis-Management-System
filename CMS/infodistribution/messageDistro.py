from twilio.rest import Client

account_sid = 'AC911c8d07cb467d8f69f4a933362de87e'
auth_token = '63911216647d96067015c43c4f42eac5'
client = Client(account_sid, auth_token)
print("SMS sent")

message = client.messages \
    .create(
    body="hello this is a text",
    from_='+12674788252',
    to='+6583980512'
)

print(message.sid)

class distributeMessage:

    def sendSMS(self,sms, phoneNumber):
        print("SMS sent")

        message = client.messages \
            .create(
            body=sms,
            from_='+6583980512',
            to='+6583980512'
        )

        print(message.sid)

        #smsAPI send sms(self.message)
    def sendEmail(self, subject, email, recipient):
        print("Email sent")
        #emailAPI send email(self.email)
    def sendTweet(self,tweet, twitterUser):
        print("Tweet sent")
        #twitterAPI send tweet(self.tweet)