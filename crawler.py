'''
Created on 2013. 10. 1.

@author: minkb
'''
import urllib
import urllib2
import cookielib

"""Adding cookie support"""
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

"""Next we will log in to the site. The actual url will be different and also the data.
You should check the log in form to see what parameters it takes and what values.

"""
data = {'p_userid' : 'minkb',
        'p_passwd' : '3302'
       }
data = urllib.urlencode(data)
urllib2.urlopen('http://www.soramoon.info/member/login.php', data) #this should log us in

"""Now you can parse the site"""
html = urllib2.urlopen('http://photo.soramoon.info/album/theme/pic_view.php?p_num=2063877&p_anum=999&p_option=&p_ix=1').read()
print html