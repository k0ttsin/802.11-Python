#!/usr/bin/python3
from scapy.all import sniff,Dot11,Dot11Elt,Dot11Beacon,wrpcap,rdpcap,EAPOL
import sys

def read_packet(pcap):
    packets=rdpcap(pcap)
    for packet in packets:
        if packet.haslayer(EAPOL):
            print (packet.summary)


read_packet(sys.argv[1])
