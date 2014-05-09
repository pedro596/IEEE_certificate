#!/usr/bin/env python
# -*- coding: utf8 -*-

# ------------------------------------------------------ #
#  Email Certificate Sender Version:1.0 Date: 4/May/14   #
# ---------- Specially designed to ISEPinIEEE ---------- # 
#  Authors:Pedro Sousa (main author)                     #
#          Victor Fernandes (attachment)                 #
#                                   Language: Python 2.7 #
# ------------------------------------------------------ #

import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMENonMultipart import MIMENonMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage


#Global Variables 
username = ""
password = ""


def mailCredentials(user, passwd):
    username = user
    password = passwd

def sendCertificate(
    workshop_name,
    student_name,
    student_mail
    ):
    #prepare message
    msg = MIMEMultipart()
    msg['Subject'] = '[ISEPinIEEE] Certificate \"'+workshop_name+'\"'
    msg.attach(MIMEText("Hi "+student_name+""",\n
Attached goes the certificate that proves your participation in the activity \""""+workshop_name+"""\".\n
Kind Regards,
ISEPinIEEE - IEEE Student Branch\n\n 
This email and the certificates were generated automatically by the software ISEPinIEEE Certificates.
If you have any problem, please report the error to pedro.sousa.pt@ieee.org or victor.fernandes.1991@ieee.org
"""  , "plain", _charset="utf-8"))
    fp = open(workshop_name+'/certificate.pdf', 'rb')
    attach = MIMENonMultipart('application', 'pdf')
    payload = (fp.read()).encode('base64')
    attach.set_payload(payload)
    attach['Content-Transfer-Encoding'] = 'base64'
    fp.close()
    attach.add_header('Content-Disposition', 'attachment', filename = 'Certificate.pdf')
    msg.attach(attach)
    #start server
    s = smtplib.SMTP("smtp.gmail.com:587")
    s.starttls()
    s.login(username, password)
    #send mail
    s.sendmail(username, student_mail, msg.as_string())
    s.quit()      

if __name__ == '__main__':
    mailCredentials()
    sendCertificate("Python Workshop", "João cabeça de melão", username)
