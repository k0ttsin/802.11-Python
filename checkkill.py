#
import sys
import subprocess

try:
    firstarg=sys.argv[1]
except:
    firstarg=""
try:
    seconarg=sys.argv[2]
except:
    seconarg=""


##############################################################################################
try:
    NetworkManagerID=subprocess.check_output(['pgrep','-f','NetworkManager'])
    NetworkManagerID=NetworkManagerID.decode().strip('\n')
except:
    NetworkManagerID="None"
                                                                                    ####Porcesses
try:
    WPASupplicantID=subprocess.check_output(['pgrep','-f','wpa_supplicant'])
    WPASupplicantID=WPASupplicantID.decode().strip('\n')
except:
    WPASupplicantID="None"
##############################################################################################

if (firstarg=="check" and seconarg=="") or (firstarg=="Check" and seconarg==""):
    print ('NetworkManager',NetworkManagerID)
    print ('wpa_supplicant',WPASupplicantID)
elif (firstarg=="check" or firstarg=="Check" ) and (seconarg=="kill" or seconarg=="Kill"):
    if NetworkManagerID!="None":
        try:
            subprocess.call(['kill','-9',NetworkManagerID])
        except:
            print ("Can't Kill The Process",NetworkManagerID)
    else:
        print ("Not Found NetworkManager Process")
    
    if WPASupplicantID!="None":
        try:
            subprocess.call(['kill','-9',WPASupplicantID])
        except:
            print ("Can't Kill The Process",WPASupplicantID)
    else:
        print ("Not Found wpa_supplicant Process")
elif firstarg=="" and seconarg=="":
    print ("Usage: python3 checkkill.py check to Check The Processes")
    print ("Usage: python3 checkkill.py check kill to Kill The Processes")
else:
    print ("Usage: python3 checkkill.py check to Check The Processes")
    print ("Usage: python3 checkkill.py check kill to Kill The Processes")
