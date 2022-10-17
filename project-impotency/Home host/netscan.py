
# probably not right

from mimetypes import init
from time import sleep



print ("welcome to netscan :3")

print ("to get started we need an IP address")
print ("If you are looking to scan a subnet mask please put a /24")
print ("If you are looking to map a subnet, please put a /24 after your IP")
print ("EX: 192.168.0.0/24")
##double check when you arent high retard
print ("EX 10.10.10.1/13")

sleep (1)

IP = input ("who is todays target intended target \n")

sleep (2)

portScanOption = input("Would you like to scan for specific ports? [Y]es/[N]o")



if portScanOption == "Y" or "y" or "Yes" or "yes":
    def Yesports():
        global Yesports

        print("alright, so you are looking to scan specific ports...")

        sleep(1.5)

        print("please specify which ports you would like to scan" )
        print("the format should look like this")
        print("")
        print("For a range of ports, such as 1,2,3,4 would look like Ex: 1-4")
        print("For specific individual ports, please enter the port numbers with commas and no spaces Ex: 1,2,3,4 ")
        ChosenPorts = input("Please put the desired ports here!\n")
        
        print ("ok, what kind of scan are we looking for")
        print

        sleep (1)

        print ("1 = Stealthy")
        print ("2 = OS detector")
        print ("3 = Port scan")
        print ("4 = VulnHub")


        sleep (5)

        print ("Enter the number of the scan you want to run")

        scantype = input("Enter the number of the scan you want to run")


        if scantype == 1:
            print ("sudo nmap -sX -v + " + IP)
        elif scantype == 2: 
            print("sudo nmap -sL -O " + IP)
        elif scantype == 3:
            print("sudo nmap ") ## do scan research when power comes back on
        elif scantype == 4:
            print("sudo nmap ") # add a scan
        elif scantype == 5:
            print("sudo nmap") #same shit




        ##Host ports
        print ("sudo nmap -sX -v + " +IP)
elif portScanOption == "N" or "n" or "no" or "No":
    
    def Noports():
        global Noports
        print ("ok, what kind of scan are we looking for")


        sleep (1)

        print ("1 = Stealthy")
        print ("2 = OS detector")
        print ("3 = Port scan")
        print ("4 = VulnHub")


        sleep (5)

        print ("Enter the number of the scan you want to run")

        scantype = input("Enter the number of the scan you want to run")


        if scantype == 1:
            print ("sudo nmap -sX -v + " +IP)
        elif scantype == 2: 
            print("sudo nmap -sL -O " + IP)
        elif scantype == 3:
            print("sudo nmap ") ## do scan research when power comes back on
        elif scantype == 4:
            print("sudo nmap ") # add a scan
        elif scantype == 5:
            print("sudo nmap") #same shit




        ##Host ports
        print ("sudo nmap -sX -v + " +IP)


