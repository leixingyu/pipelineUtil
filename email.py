import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(server, sender, recipients, subject='', html=''):
    """
    Send out email formatted in HTML

    :param server: str. smtp email server address
                   e.g. smtp.gmail.com
    :param sender: str. email address of the sender
    :param recipients: [str]. list of email recipients addresses
    :param subject: str. email subject line
    :param html: str. email body in html formatted string
    """
    server = smtplib.SMTP(server)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    msg.attach(MIMEText(html, 'html'))

    to_addresses = recipients.split(',')
    server.sendmail(sender, to_addresses, msg.as_string())
    server.quit()
