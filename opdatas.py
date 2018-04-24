import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from collections import OrderedDict

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
    
def shift_dict(listuple):   # 可以直接用dict(listuple)转换，此处主要是把值转化为float
    data = {item[0]: float(item[1]) for item in listuple}
    return data
      
def flat_data(items, category=2):
    category = str(category)
    if category not in ['1', '2', '3']:
        print("\ncategory should be 1 or 2 or 3, now auto set be 2.\n")
        category = '2'
    result = {}
    datas = OrderedDict()
    lrbl = shift_dict(items["LRBL"][category])
    yycb = shift_dict(items["YYCB"][category])
    yysr = shift_dict(items["YYSR"][category])
    for key in lrbl.keys():
        result[key] = (yysr[key], yysr[key] / sum(yysr.values()), yycb[key], yycb[key] / sum(yycb.values()), lrbl[key] / 100, 
                        (yysr[key] - yycb[key]) / yysr[key])
                        
    result = sorted(result.items(), key=lambda x: x[1][1], reverse=True)
    for item in result:
        datas[item[0]] = item[1]
    return datas
    
def main():
    url = "http://stockpage.10jqka.com.cn/000816/operate/"
    html = get_html(url)
    datas = get_datas(html)
    items = get_items(datas)["2017-06-30"]
    result = flat_data(items, 4)
    # print("\n", items, sep="")
    print("\n")
    # pprint(items)
    pprint(result)
    # print(result["柴油机"])
    
    
if __name__ == "__main__":
    main()