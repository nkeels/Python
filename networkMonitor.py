#***************************************************************#
#This script is going to run a daily test on all ip addresses to#
#see if they are still open                                     #
#                                                               #
#                                                               #
#                                                               #
#                                           -Nicholas Keels 2017#
#***************************************************************#

port socket
import contact_lib


ip = ['10.25.128.225', '10.25.128.223', '10.25.128.224', '10.25.128.241']
err = []


for address in ip:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((address, 9999))
    if result != 0:
        err.append(address)

if len(err) == 0:
    quit()
else:
    contact_lib.email('There is an error with the {} ip address(es)! Please check on the issue as soon as possible!!!!!'.format(err))



