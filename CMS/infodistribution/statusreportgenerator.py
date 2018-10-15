from .messageDistro import distributeMessage
from threading import Timer
from datetime import datetime

class StatusReportGenerator():
    def __init__(self, recipient):
        self.distro = distributeMessage
        self.prime_minister_adress = 'lee.hsien.loong@gmail.com'
        # Todo: initialisera statistik

        self.generate_report()


    def notify(self, message):
        # Track statistics about events  Todo: actually track statistics
        self.no_incidents += 1

    def generate_report(self):
        Timer(1800.0, self.generate_report).start()  # Schedule next report

        title = 'Incident status report ' + datetime.now()
        report = 'Very informative report'  # Todo: actually generate a report

        self.distro.sendEmail(title, report, self.prime_minister_adress)

        # Todo: reset statistics