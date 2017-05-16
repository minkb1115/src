'''
Created on 2013. 3. 2.

@author: minkb
'''
#-*- coding= cp949 -*-
#-*- coding= utf-8 -*-
import socket
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s= socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return
    
def checkVulns(banner): 
    f= open("c:\\test.txt","r")
    for line in f.readlines():
        if line.strip('\n') in banner:
           # print line
            print "week :"+ banner.strip('\n')
       
def main():
        portList=[22]
        for x in range(1,5):
            ip = '69.197.27.194'
            for port in portList:
                banner = retBanner(ip,port)
                if banner:
                    print ip + " : "+banner
                    checkVulns(banner)
if __name__ == '__main__':
    main()