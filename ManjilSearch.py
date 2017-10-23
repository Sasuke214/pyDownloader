
import urllib
from bs4 import BeautifulSoup

def search(textToSearch):
        #
        query = urllib.request.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        try:
                #
                response = urllib.request.urlopen(url)
                #
                html = response.read()
                #
                soup = BeautifulSoup(html,'lxml')
                i=0
                #
                allurls=[]
                #
                for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                    if i==0:
                            i+=1
                            continue
                #
                    allurls.append('https://www.youtube.com' + vid['href'])
                return allurls
        except:
                print('Please Check Your Internet Connection...')
                return []
        
