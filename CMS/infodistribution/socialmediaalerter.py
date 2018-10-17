from .messageDistro import distributeMessage


class SocialMediaAlerter:
    def __init__(self):
        self.messages_received = 0
        self.distro = distributeMessage

    def notify(self, message):
        self.messages_received += 1
        # organise message to be fit for twitter
        self.distro.sendTweet(message)
        # organize message to be for sms
        self.distro.sendSMS(message)