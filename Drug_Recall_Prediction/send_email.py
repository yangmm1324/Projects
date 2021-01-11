
import smtplib
from email.mime.text import MIMEText


def send_email(email,height,avg_height, count):
    from_email='yangmm1324@gmail.com'
    from_password='ym19831005!'
    to_email=email

    subject='Height data'
    message='Hey there, your height is <strong> %s</strong>. Average height of all is <strong> %s </strong> and that is\
    calculated out of <strong> %s </strong> people.' % (height, avg_height, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
