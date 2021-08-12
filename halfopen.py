from scapy.all import sr1,IP,TCP,send
import sys

def scanner(target,port):
    ans=sr1(IP(dst=target)/TCP(dport=port,sport=1024,flags="S",seq=22456),verbose=False)[0]
    if ans[TCP].flags == "SA":
        print ("Port ",port," is open")
    send(IP(dst=target)/TCP(dport=port,sport=1024,flags="R",seq=22458),verbose=False)

target=sys.argv[1]
for port in range(50,85):
    scanner(target,port)
