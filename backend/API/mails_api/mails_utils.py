import smtplib
from email.mime.text import MIMEText

def send_me_email(subject, body):
    password = "&Anapurna01"
    recipients = ["contact.admin@codovore.fr"]
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['To'] = recipients[0]
    try:
        smtp_server = smtplib.SMTP_SSL('mail.infomaniak.com', 465)
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
        smtp_server.quit()
        return True
    except Exception as e:
        print(f"error to send mail: {e}")
        return False