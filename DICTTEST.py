import os
import re
from datetime import datetime
import pandas as pd
# 文件夹重命名函数
def changename(strings):
    for name in os.listdir():
        strings = strings.replace(',', '，')
        strings = strings.replace('  ', '，')
        strings = strings.replace('\t', '，')
        strings = strings.replace('、', '，')
        strings = strings.replace(' ', '，')
        os.rename(name, strings)


# 文件名称导出到excel函数
def exportxlsx():
    ls = []
    print(os.listdir())
    for name in os.listdir():
        item = {}
        name = re.split("，|：", name)
        a, b, c, *rest = name
        item['类型1'] = a
        item['投保人姓名'] = b
        item['类型2'] = c
        item['被保人姓名'] = ','.join(i for i in rest)
        item['被保险人人数'] = len(rest)
        ls.append(item)
        df = pd.DataFrame(ls)
    df.to_excel("E:/可删/材料收集{}.xlsx".format(datetime.now().date().strftime('%m%d')), index=False)


path = 'E:/1智慧医疗/项目/南京宁惠保3期/投保/客服/退保/6月5日之后收集的退保材料'
os.chdir(path)
exportxlsx()
