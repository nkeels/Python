import os


bashCommand = "sudo arp-scan --interface=enp0s25 --localnet | grep 192.168.2.* > output.txt"
os.system(bashCommand)

f = open('output.txt', 'r')
print f.read()

print f

