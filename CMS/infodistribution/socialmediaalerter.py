from .messageDistro import distributeMessage


class SocialMediaAlerter:
    def __init__(self):
        self.messages_received = 0
        self.distro = distributeMessage()
        self.twitter_user = 'SingaporeCMS'
        self.phone_numbers = [12341234, 12341235]

    def notify(self, message):
        self.messages_received += 1
        # organise message to be fit for twitter
        self.distro.sendTweet(message, self.twitter_user)
        # organize message to be for sms
        for number in self.phone_numbers:
            self.distro.sendSMS(message, number)
