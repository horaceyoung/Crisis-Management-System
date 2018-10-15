from . import messageDistro as md


class dispatcherAlert:
    def __init__(self):
        self.distro = md.distributeMessage

    def notify(self, message):
        # organise message to be fit for sms
        self.distro.sendSMS(message)