#!/usr/bin/env python
from scapy.all import *
import time

# VARIABLES
src = sys.argv[1]
dst = sys.argv[2]
sport = random.randint(1024,65535)
dport = int(sys.argv[3])

# SYN
ip=IP(src=src,dst=dst)
SYN=TCP(sport=sport,dport=dport,flags='S',seq=1000)
SYNACK=sr1(ip/SYN)

# ACK
ACK=TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
send(ip/ACK)

time.sleep(15)

ip = IP(src=src, dst=dst)
tcp = ip / TCP(sport=sport, dport=dport, flags="PA", seq=123, ack=1) / "scapy packet 123"
tcp.show2()

send(tcp)