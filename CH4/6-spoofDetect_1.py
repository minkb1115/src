#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import optparse
from scapy.all import *
from IPy import IP as IPTEST

def testTTL(pkt):
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            print '[+] pkt Recieved From '+ipsrc+ ' with TTL '   + ttl
    except:
        pass

def main():
    sniff(prn=testTTL, store=0)

if __name__=='__main__':
    main()