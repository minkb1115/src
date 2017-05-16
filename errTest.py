#!/usr/bin/python
# -*- coding: utf-8 -*-

import pexpect
import optparse
import os

ID = 'User1'
cmdrun = 'A LINUX COMMAND'
sshChild = pexpect.spawn('ssh root@192.168.0.4')
sshOut = file('sshLog.txt','w')
sshChild.logfile = sshOut
sshChild.expect('Last login:*')
sshChild.expect('Please enter your login Id')
sshChild.sendline(ID + '\r')
sshChild.sendline('ssh 192.168.21.1\r')
sshChild.expect('Last login:*')
sshChild.expect('Please enter your login Id')
sshChild.sendline(ID + '\r')
sshChild.sendline(cmdrun + '\r')