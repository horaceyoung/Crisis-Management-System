from .informationsender import InformationSender


class SocialMediaAlerter:
    def __init__(self):
        self.messages_received = 0
        self.distro = InformationSender()
        self.twitter_user = 'SingaporeCMS'
        self.phone_numbers = [12341234, 12341235]

    def notify(self, message):
        self.messages_received += 1
        # organise message to be fit for twitter
        self.distro.send_tweet(message, self.twitter_user)
        # organize message to be for sms
        for number in self.phone_numbers:
            self.distro.send_sms(message, number)
