#!/usr/bin/env python
# -*- coding: utf8 -*-

# ------------------------------------------------------ #
#  Email Certificate Sender Version:1.0 Date: 4/May/14   #
# ---------- Specially designed to ISEPinIEEE ---------- # 
#  Authors:Pedro Sousa (main author)                     #
#          Victor Fernandes (attachment)                 #
#                                   Language: Python 2.7 #
# ------------------------------------------------------ #
import send_mail
import certificate

from easygui import passwordbox
from easygui import enterbox

#Global Variables 
username = ""
password = ""


username = enterbox(msg='Please enter your Gmail Accout', title='ISEPinIEEE Certificates', default='', strip=True)
password = passwordbox(msg='What is your password?', title='ISEPinIEEE Certificates')
send_mail.mailCredentials(username,password)

i  = 0
while (i<2):
    certificate.createCertificate("Python Workshop",3,"May",2014,"Victor Fernandes"+str(i),"Pedro Sousa","Pedro Sousa")
    send_mail.sendCertificate("Python Workshop","Pedro Sousa"," maildequemvaireceber@....")
    i+=1
