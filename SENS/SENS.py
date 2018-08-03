import requests
import datetime
import ctypes

# now = '27/07/2018'
now = datetime.datetime.now().strftime("%d/%m/%Y")

from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        counter = 0
        for link in s.findAll('span', {'class':'normal'}):
            if now in link.get_text():
                counter+=1
        if counter>0:
            ctypes.windll.user32.MessageBoxA(0, str(counter) + " new announcement(s) has been added to SENS feeds today.", "New announcement", 1)

web(1,'http://www.sharenet.co.za/free/sens/list_sens.phtml?scode=STP&scheme=default')