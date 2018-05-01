from pprint import pprint
from collections import OrderedDict

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