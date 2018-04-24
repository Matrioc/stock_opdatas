import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

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
    
def get_items(datas):
    items = json.loads(datas)
    return items
    
def shift_dict(listuple):
    data = {item[0]: float(item[1]) for item in listuple}
    return data
      
def flat_data(items):
    result = {}
    lrbl2 = shift_dict(items["LRBL"]['2'])
    yycb2 = shift_dict(items["YYCB"]['2'])
    yysr2 = shift_dict(items["YYSR"]['2'])
    for key in lrbl2.keys():
        result[key] = (lrbl2[key], yycb2[key], yysr2[key], yycb2[key] / sum(yycb2.values()), yysr2[key] / sum(yysr2.values()), 
                        (yysr2[key] - yycb2[key]) / yysr2[key])
    return result
    
def main():
    url = "http://stockpage.10jqka.com.cn/000816/operate/"
    html = get_html(url)
    datas = get_datas(html)
    items = get_items(datas)["2017-06-30"]
    result = flat_data(items)
    # print("\n", items, sep="")
    print("\n")
    pprint(result)
    
    
if __name__ == "__main__":
    main()