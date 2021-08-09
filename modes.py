#For Script Learning
#
#
#By KC <penguin>
#
#
#Example Usage:
#
#For Managed Mode
#sudo python3 kcmon-pen.py wlan1 Managed
#
#For Monitoring Mode
#sudo python3 kcmon-pen.py wlan1 Monitor
#
#
#

import subprocess
import sys

try:
    try:
        interface=sys.argv[1]
    except:
        interface=""
    try:
        mode=sys.argv[2]
    except:
        mode=""

    if mode=='Monitor' or mode=='monitor':   #for Monitoring Mode
        subprocess.call(['ifconfig',interface,'down'])
        print ("Changing Monitoring Mode For : ",interface)
        subprocess.call(['iwconfig',interface,'mode','Monitor'])
        subprocess.call(['ifconfig',interface,'up'])
        print ("Changed Successfully!!!")
    elif mode=='Managed' or mode=='managed': #for Normal Mode
        subprocess.call(['ifconfig',interface,'down'])
        print ("Changing Managed Mode For : ",interface)
        subprocess.call(['iwconfig',interface,'mode','Managed'])
        subprocess.call(['ifconfig',interface,'up'])
        print ("Changed Successfully!!!")
    elif interface=="" and mode=="":
        print ('''
        Example Usage : python3 kcmon-pen.py <interface> <mode>
        Available Modes : Monitor and Managed
        ''')
    else:
        print ('''
        Example Usage : python3 kcmon-pen.py <interface> <mode>
        Available Modes : Monitor and Managed
        ''')
except Exception as e:
    print (e)
