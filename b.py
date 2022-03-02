import datetime
from distutils.command.build_scripts import first_line_re
import imp 
import time
import requests
from bs4 import BeautifulSoup 
b=datetime.datetime.fromtimestamp(time.time())
print("時刻")
print(b)
r=requests.get("http://www.cis1.c.dendai.ac.jp/")
print(r.headers)
print(r.encoding)
a=BeautifulSoup(r.content,"html.parser")
print(a.find())