#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
from scapy.all import *


def findGoogle(pkt):
    if pkt.haslayer(Raw):
        payload = pkt.getlayer(Raw).load
        if 'GET' in payload:
            if 'naver' in payload:
                r = re.findall(r'(?i)\&q=(.*?)\&', payload)
                if r:
                    search = r[0].split('&')[0]
                    search = search.replace('q=', '').\
                      replace('+', ' ').replace('%20', ' ')
                    print '[+] Searched For: ' + search


def main():

    conf.iface = 'wlan0mon'

    try:
        print '[*] Starting Google Sniffer.'
        sniff(filter='tcp port 80', prn=findGoogle)
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main()

