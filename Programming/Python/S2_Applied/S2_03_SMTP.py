#!/usr/bin/python3
#   SMTP

#T# SMTP stands for Simple Mail Transfer Protocol

#T# import the SMTP module
import smtplib

#T# string with the sender user
sender1 = 'thisisrtsthree999@gmail.com'

#T# string with the receiver user
receiver1 = ['julings12@gmail.com']

#T# string with the subject of the email
subject1 = 'Test email subject'

#T# string with the filepath of the attachment
attachment1 = '/home/jul/PolirecylBases/README.md'

#T# open and read the attachment to attach it in the email
fh1 = open(attachment1,"rb")
attContent1 = fh1.read()

#T# boundary to separate text from attachment
boundary1 = "separateParts"

#T# actual email
message1 = """From: %s
To: %s
Subject: %s
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
Content-Type: text/plain

Newly attempt to send a message over SMTP from Python.
It has an attachment. Thanks and good day.
--%s
Content-Type: multipart/mixed; name=\"%s\"
Content-Disposition: attachment; filename="testFile"

%s
--%s--
""" % (sender1,", ".join(receiver1),subject1,boundary1,boundary1,boundary1
    ,attachment1,attContent1,boundary1)

#T# send email within try except block
try:

#T# creat an SMTP object with SMTP(host,port)
    smtpObj1 = smtplib.SMTP('smtp.gmail.com',587)

#T# extended SMTP hello function with ehlo()
    smtpObj1.ehlo()

#T# secure communication with starttls()
    smtpObj1.starttls()

#T# login with login()
    smtpObj1.login(sender1,'s9l1pknOt')

#T# send the email with sendmail()
    smtpObj1.sendmail(sender1,receiver1,message1)

#T# close communication with close()
    smtpObj1.close()
    print("Email was sent")
except:
    print("Error, Can't send email")