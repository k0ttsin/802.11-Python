from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11ProbeResp
from scapy.layers.dot11 import Dot11Beacon
from scapy.layers.dot11 import Dot11Elt

hidden_ap=set()

def pktHandler(pkts):
    if pkts.haslayer(Dot11Beacon):
        if not pkts.info:
            if pkts.addr3 not in hidden_ap:
                hidden_ap.add(pkts.addr3)
                print ("Hidden SSID Found : {}".format(pkts.addr3))
    elif pkts.haslayer(Dot11ProbeResp) and pkts.addr3 in hidden_ap:
        print ("Undercovered SSID Found :", pkts.info.decode()," : ",pkts.addr3)


sniff(iface="wlan0",count=10000,prn=pktHandler)
