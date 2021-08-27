from scapy.all import *
from scapy.layers.dot11 import Dot11
from scapy.layers.dot11 import Dot11Beacon
from scapy.layers.dot11 import Dot11Elt

hidden_aps=set()

def pktHandler(pkts):
    if pkts.haslayer(Dot11Beacon):

sniff(iface="wlan0",count=20,prn=pktHandler)

