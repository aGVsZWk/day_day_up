import smtplib
from email.mime.text import MIMEText


def send_mail(sender, recipients, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(recipients)

    mail_sender = smtplib.SMTP('localhost')
    mail_sender.send_message(msg)
    mail_sender.quit()


if __name__ == '__main__':
    response = send_mail("qqbushi905713813@gmail.com",
                         ["qq905713813@163.com", "peter@example.com"],
                         "This is your message", "Have a good day")
