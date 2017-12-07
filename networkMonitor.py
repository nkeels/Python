#*****************************************************************#
# This script is going to run a daily test on all ip addresses to #
# see if they are still open                                      #
#                                           -nkeels               #
#*****************************************************************#

import smtplib
import socket

def email(content):
    content
    mail = smtplib.SMTP('smtp.gmail.com',587) # Parameterize these as well
    mail.ehlo()
    mail.starttls()
    mail.login('<email>','<password>') 
    mail.sendmail('<from email>', '<to email>', content)
    mail.close 
    
#adjusted from pythonsms.py alexle

def text(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('<email>','<password>') 
    server.sendmail('<from email>', '<to email>', message)
    
# In a future version these will be parametarized for better command line functionality
# they will also be able to be read from a file.
ip = [<list of ip's>]

for address in ip:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((address, 9999)) # This port will also be parameterized
    if result != 0: 
        Email('There is an issue with the {} address'.format(address))





