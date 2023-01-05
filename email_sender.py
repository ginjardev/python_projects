import smtplib, ssl

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

print('Email sent, Gmail')

smtpserver.close()

#testing with yahoo

yusername = 'arthur_ini@yahoo.com'
yreceiver = 'arthurshur@gmail.com'
ypassword = 'vbglfpdjpuvhhaus'

context = ssl.create_default_context()

yahoo_smtpserver = smtplib.SMTP('smtp.mail.yahoo.com', 587)
yahoo_smtpserver.ehlo()
yahoo_smtpserver.starttls()
yahoo_smtpserver.ehlo()
print('server created')
yahoo_smtpserver.login(yusername, ypassword)
print('logged in')

ymsg = 'Subject: Yahoo SMTP \nJust saying hi. Bye bye!'
yahoo_smtpserver.sendmail(yusername, yreceiver, ymsg)

print("Email sent from Yahoo")
yahoo_smtpserver.close()