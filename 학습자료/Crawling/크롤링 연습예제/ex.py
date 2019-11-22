from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("file:///C:/Users/admin/Documents/GitHub/web1/1.html")
bsBody = BeautifulSoup(html.read(), "html.parser")
print(bsBody)
