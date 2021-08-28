from scapy.all import EAPOL,sniff,wrpcap
from scapy.layers.dot11 import Dot11,Dot11Elt,Dot11Beacon
import sys

aps=set()
bss=set()
def pktHandler(packet):
    if packet.haslayer(Dot11Beacon):
        if packet[Dot11Elt].info.decode() not in aps:
            aps.add(packet[Dot11Elt].info.decode())
            bss.add(packet[Dot11].addr2)
            print (packet[Dot11Elt].info.decode()," : ",packet[Dot11].addr2)
    if packet.haslayer(EAPOL):
        if packet[Dot11].addr2 in bss:
            print ("EAPOL", packet[Dot11].addr2)
    wrpcap("file.cap",packet,append=True)

sniff(iface=sys.argv[1],prn=pktHandler)
