from .informationsender import InformationSender


class SocialMediaAlerter:
    def __init__(self):
        self.messages_received = 0
        self.distro = InformationSender()
        self.phone_numbers = ['+6583980512', '+6583980512']

    def notify(self, message):
        self.messages_received += 1
        self.distro.send_tweet(message)
        for number in self.phone_numbers:
            self.distro.send_sms(message, number)
