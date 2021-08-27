#!/usr/bin/python3

import sys
from scapy.all import *
from scapy.layers.dot11 import Dot11
from scapy.layers.dot11 import Dot11ProbeReq

clientprobes=set()

def PacketHandler(packet):

    if packet.haslayer(Dot11ProbeReq):
        if packet.type==0 and packet.subtype==4:
            if (packet.addr2 not in clientprobes):
                clientprobes.add(packet.addr2)
                if not packet.info:
                    packet.info="<<Not Associated>>"
                print ("Client :",packet.addr2," SSID :",packet.info.decode())

sniff(iface=sys.argv[1], prn=PacketHandler)
