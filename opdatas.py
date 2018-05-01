import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from collections import OrderedDict
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.10 Safari/537.36"
    }
    
def get_html(url):
    html = requests.get(url, headers=headers)
    return html.text
    
def get_datas(html):
    soup = BeautifulSoup(html, "lxml")
    soup_data = soup.select("div#chartsData")
    # soup_data = soup.select("div#linechartsData")
    datas = soup_data[0].get_text() if soup_data else None
    return datas
    
def get_items(code):
    url = "http://stockpage.10jqka.com.cn/{}/operate/".format(code)
    print("\nget url>>> {}\n".format(url))
    html = get_html(url)
    datas = get_datas(html)
    items = json.loads(datas) if datas else None
    return items
    
def get_codes():
    with open("codes.txt", "r") as txtf:
        codes = [code.strip().split('\t') for code in txtf.readlines()]
    return codes
 
def main():
    codes = get_codes()
    #print(*codes[:20], sep="\n")
    for code ,name in codes[:20]:
        items = get_items(code)
        print(items) if items else print("error code: {}".format(code))
        print("need sleep 3 seconds.")
        time.sleep(3)
        print("\n")
        
if __name__ == "__main__":
    main()