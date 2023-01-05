import smtplib

sender='arthurshur@gmail.com'
receiver = 'arthur_ini@yahoo.com'
password = 'tuaktbzurocsjofj'

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(sender, password)
msg = 'Subject: Email from Python script \nLearning about SMTP and the smtplib module in Python.\n \
    Kudos to me.'
smtpserver.sendmail(sender, receiver, msg)

print('Email sent')

smtpserver.close()