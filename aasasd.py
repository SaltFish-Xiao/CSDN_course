
import os,re
path = 'D:/1智慧医疗/项目/南京宁惠保4期/退保/退保材料收集'
os.chdir(path)
for name in os.listdir():
   #  item = {}
   #  name = re.split("，|：", name)
   # # print(name)
   #  a, b, c, *rest = name
   #  print(a)
   #  print(b)
   #  print(c)
   #  print(*rest)
    #将字符串中空格替换成逗号
    old_name = name
    new_name = old_name.replace(";", "：")
    #重命名文件名
    os.rename(old_name, new_name)

