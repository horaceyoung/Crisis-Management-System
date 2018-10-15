from .messageDistro import distributeMessage


class dispatcherAlert:
    def __init__(self):
        self.distro = distributeMessage

    def notify(self, message):
        # organise message to be fit for sms
        self.distro.sendSMS(message)