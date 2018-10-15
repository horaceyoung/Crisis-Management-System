class distributeMessage:

    def sendSMS(self,sms):
        print("SMS sent")
        #smsAPI send sms(self.message)
    def sendEmail(self,email):
        print("Email sent")
        #emailAPI send email(self.email)
    def sendTweet(self,tweet):
        print("Tweet sent")
        #twitterAPI send tweet(self.tweet)

class dispatcherAlert:
    def __init__(self,message):
        distro = distributeMessage
        #organise message to be fit for sms
        distro.sendSMS(message)
        del distro

class socialmediaAlert:
    def __init__(self,message):
        distro = distributeMessage
        #organise message to be fit for twitter
        distro.sendTweet(message)
        del distro
