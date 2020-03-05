import urllib.request
import os
import pycurl
from bs4 import BeautifulSoup
import re
import json
import requests
import subprocess


mapage="http://challenge01.root-me.org/programmation/ch8/"
r = requests.get(mapage)
cooks = r.cookies
print (cooks)
page = urllib.request.urlopen(mapage)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
name_box = soup.find('img')
test = str(name_box)
#print(name_box)


#Pour retirer l'image:
regex = r"data.*\="
img_list = re.findall(regex,test)

for item in img_list:
    
    #print(item)
    urllib.request.urlretrieve(item, "captcha.jpg")
    os.system('tesseract captcha.jpg out')
    cap = os.system('')
    getcap = subprocess.Popen("cat out.txt", shell=True,stdout=subprocess.PIPE).stdout
    cap = getcap.read()
    captcha = cap.decode()
    print (captcha)
    payload = {'cametu' : captcha}

    r = requests.post(mapage, data=payload, cookies=cooks)
    print(r.text)






#os.system('curl -d "cametu=",cap" -X POST http://challenge01.root-me.org/programmation/ch8/')
