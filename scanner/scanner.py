import scanner.useragent as useragent
import requests
from lxml import html
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bsoup
import re

class dscr:
    def __init__(self):
        self.results = []
        pass
    def search_google(self,query,start=0):
        user_agent = {'User-agent': useragent.get_useragent()}
        page = requests.get(f"http://www.google.com.tr/search?q={query}&num=100&start={start}",headers=user_agent)
        webpage = html.fromstring(page.content)
        a = webpage.xpath('//a/@href')
        for i in range(len(a)):
            a[i] = a[i].replace("/url?q=","")
            
            if(urlparse(a[i]).netloc != ""):
                a[i] = a[i].split("&sa=")[0]
            else:
                a[i] = ""
            if( a[i].find("google") > 0):
                a[i] = ""
        a = list(filter(None, a))
        self.results = self.results+a
        return a
    def search_duckduckgo(self,query):
        user_agent = {'User-agent': useragent.get_useragent()}
        response = requests.get(f"https://html.duckduckgo.com/html/?q={query}",headers=user_agent)
        urls = re.findall(r'<a class="result__url" href="(.+?)">', response.text)
        return urls
    def search_ask(self,query):
        user_agent = {'User-agent': useragent.get_useragent()}
        response = requests.get(f"https://www.ask.com/web?q={query}",headers=user_agent)
        urls = re.findall(r"target=\"_blank\" href='(.*?)' data-unified=", response.text)
        return urls
    def search_results(self,dork):
        try:
            google_list = self.search_google(dork)
        except:
            google_list = []
        try:
            duckduckgo_list = self.search_duckduckgo(dork)
        except:
            duckduckgo_list = []
        try:
            ask_list = self.search_ask(dork)
        except:
            ask_list = []
        result_list = google_list+duckduckgo_list+ask_list
        return result_list
