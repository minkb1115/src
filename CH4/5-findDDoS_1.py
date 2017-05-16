#!/usr/bin/python
# -*- coding: utf-8 -*-
import dpkt
import optparse
import socket
THRESH = 1000


def findDownload(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    print '[!] ' + src + ' Downloaded LOIC.'
        except:
            pass
f = open('E:\\pysource\\dump.pcap','rb')
pcap = dpkt.pcap.Reader(f)
findDownload(pcap)