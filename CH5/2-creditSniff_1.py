#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import optparse
from scapy.all import *


def findCreditCard(raw):
    americaRE = re.findall('3[47][0-9]{13}', raw)
    if americaRE:
        print '[+] Found American Express Card: ' + americaRE[0]


def main():
    conf.iface = 'wlan0mon'
    tests =[]
    tests.append('I would like to buy 133 copies of that dvd')
    tests.append('Bill my card : 378282246310005 for \$2600')
    for test in tests:
        findCreditCard(test)

if __name__ == '__main__':
    main()
