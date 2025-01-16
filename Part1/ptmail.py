import smtplib
from email.mime.text import MIMEText
import os

# Kräver ett "app password" för Gmail
email = 'ptestmail404@gmail.com' # E-postadress att skicka från
password = os.getenv('PTM_PASS') # Lösenord

def send_email(subject, body, to):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to

    send_email_via_smtp(to, msg)
    

def send_email_via_smtp(to, msg):
    with smtplib.SMTP("smtp-gmail.com", 25) as server:
        server.connect ("smtp.gmail.com", 587)
        server. ehlo()
        server.starttls()
        server. login (email, password)
        text = msg.as_string()
        server. sendmail (email, to, text)
        server.quit()

subject = "Automail from mitt Python"
message = "Jag testar min Python"
recipient = "magnus.kurtz@gmail.com"

if __name__ == "__main__":
    send_email(subject, message, recipient)