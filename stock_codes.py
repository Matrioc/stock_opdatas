import requests
import re


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) \Chrome/49.0.2623.112 Safari/537.36"
}

mac_pattern = re.compile(r"http://quote.eastmoney.com/s['hz']([0-9]{6}).html")


def get_codes():
    url = "http://quote.eastmoney.com/stocklist.html"
    html = requests.get(url, headers=headers).text
    matchs = re.findall(mac_pattern, html)
    codes = [code+'\n' for code in matchs if code.startswith(('6', '0', '3'))]
    return codes
    
def write_txt(datas, filename="codes.txt"):
    with open(filename, "w") as txtf:
        txtf.writelines(datas)
    print("write success.")
    
def main():
    codes = get_codes()
    print(*codes[:100])
    write_txt(codes)
    

if __name__ == "__main__":
    main()
    
    
