from scapy.all import Dot11,Dot11Beacon,Dot11Elt,Dot11ProbeReq,Dot11ProbeResp,sniff
import sys
from threading import Thread
import os
import pandas
import time


networks = pandas.DataFrame(columns=["BSSID", "ESSID", "Signal", "Channel", "ENC/AUTH"])
networks.set_index("ESSID", inplace=True)

clients = pandas.DataFrame(columns=["SSID","STA"])
clients.set_index("STA", inplace=True)


def PacketHandler(packet):
    if packet.haslayer(Dot11Beacon):
        global essid
        essid = packet[Dot11Elt].info.decode()
        bssid = packet[Dot11].addr2
        
        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"
        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        channel = str(channel)
        encry = stats.get("crypto")
        encry =str(encry)
        networks.loc[essid]=(bssid,dbm_signal,channel,encry)
    
    if packet.type==0 and packet.subtype==4:
        if not packet.info:
            packet.info="<<Not Associated>>"
        clients.loc[packet.addr2]=(packet.info.decode())
                      

def printNetworks():
    while True:
        os.system("clear")
        print (networks.drop_duplicates())
        print (clients.drop_duplicates())
        time.sleep(1)


def changeChnl():
    for i in range(16):
        iface=sys.argv[1]
        chnge="iwconfig"+iface+"channel"+i
        os.system(chnge)

    
try:
    if __name__ == "__main__":
        prnter=Thread(target=printNetworks)
        prnter.daemon=True
        prnter.start()
        chnggg=Thread(target=changeChnl)
        chnggg.start()
        sniff(iface=sys.argv[1],prn=PacketHandler)
except Exception as e:
    print (e)
 
