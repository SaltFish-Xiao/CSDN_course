import os
import re
def walk(file):

    for root,dirs,files, in os.walk(file):
        #root 表示当前访问的文件夹路径
        #dirs 表示该文件夹下的子目录名list
        #files 表示该文件夹下的文件list
        #遍历文件
        #for f in files:
           # print(os.path.join(root,f))
        #遍历所有文件夹
        items = []
        for d in dirs:
            #print(d)
            a = re.split("：|，",d)
            #c = a.split("，")
            #if len(a)<4:
               # print(a)
            print(a[3])
def main():
    walk('D:/1智慧医疗/项目/南京宁惠保4期/退保/退保材料收集')

if __name__=='__main__':
    main()