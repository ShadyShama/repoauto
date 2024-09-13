import getpass
import telnetlib

host = "localhost"
user= input("Enter your remote account:")
password = getpass.getpass()

f=open('switches') 
#here mention the file conatins ips of all switches you want to configure#

for IP in f:
    IP=IP.strip() #to strip any space in ip address
    print("Configuring Switch" +(IP))
    host=IP
    tn = telnetlib.Telnet(host)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii')+b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii')+b"\n")
    tn.write(b"conf t\n")
    #tn.write(b"terminal length 0\n")#
    # in order to no need to press space to see the whole pages of running conf#
    for n in range(10,90,10):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
    tn.write(b"vlan 21\n")
    tn.write(b"name Switches\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 61\n")
    tn.write(b"name ITWorkshop\n")
    tn.write(b"exit\n")

    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    #backup config in file#
    readoutput= tn.read_all()
    saveoutput= open("switch" + host,"w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close
    print(tn.read_all().decode('ascii'))






#import telnetlib
#import getpass
#HOST = "localhost"
#user = input("USERNAME: ")
#password = getpass.getpass()
#tn = telnetlib.Telnet()
#tn.open(HOST)
#tn.read_until(b"login: ")
#tn.write(user.encode("ascii")+b"\n")
#tn.read_until(b"Password: ")
#tn.write(password.encode("ascii")+b"\n")
#tn.write(b"exit\n")
#print(tn.read_all())
#tn.close()