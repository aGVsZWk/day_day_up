import csv
import smtplib
from email.mime.text import MIMEText


class Mailer(object):
    def send(sender, recipients, subject, message):
        msg = MIMEText()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients


class Logger(object):
    def output(message):
        print("[Logger]".format(message))


class LoggerAdapter(object):
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def send(self, sender, recipients, subject, message):
        log_message = "From: {}\nTo: {}\nSubject: {}\nMessage: {}".format(
            sender, recipients, subject, message)
        self.what_i_have.output(log_message)

    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)


if __name__ == '__main__':
    mailer = Mailer()
    mailer.send("me@example.com", ["a@a.com", "b@b.com"],
                "This is your message", "Have a good day")
