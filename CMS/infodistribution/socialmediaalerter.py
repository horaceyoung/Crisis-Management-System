from . import messageDistro as md


class socialmediaAlert:
    def __init__(self):
        self.distro = md.distributeMessage

    def notify(self, message):
        # organise message to be fit for twitter
        self.distro.sendTweet(message)
        # organize message to be for sms
        self.distro.sendSMS(message)