#*****************************************************************#
# This script is going to run a daily test on all ip addresses to #
# see if they are still open                                      #
#                                           -nkeels               #
#*****************************************************************#

import smtplib
import socket

def Email(content):
    content
    mail = smtplib.SMTP('smtp.gmail.com',587) # Parameterize these as well
    mail.ehlo()
    mail.starttls()
    mail.login('byuidahoradioingest@gmail.com','W1deOrb!t') # Hardcoded pass....wut
    mail.sendmail('byuidahoradioingest@gmail.com', 'nikeels92@gmail.com', content)
    mail.sendmail('byuidahoradioingest@gmail.com', 'eldermcgurk@gmail.com', content)
    mail.close 
# In a future version these will be parametarized for better command line functionality
# they will also be able to be read from a file.
ip = ['10.25.128.225', '10.25.128.223', '10.25.128.224', '10.25.128.241']

for address in ip:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((address, 9999)) # This port will also be parameterized
    if result != 0: 
        Email('There is an issue with the {} address'.format(address))





