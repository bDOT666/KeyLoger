import smtplib

gmail_user = 'keyloger.mail.prosze@gmail.com'
gmail_password = '12345678a!'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:
    print('Something went wrong...')