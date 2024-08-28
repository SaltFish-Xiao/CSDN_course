import os
def walk(file):
    j = 0
    i = 0
    for root,dirs,files, in os.walk(file):
        #root 表示当前访问的文件夹路径
        #dirs 表示该文件夹下的子目录名list
        #files 表示该文件夹下的文件list
        #遍历文件
        #for f in files:
           # print(os.path.join(root,f))
        #遍历所有文件夹
        for d in dirs:
            print(d)
            j+=1
        for f in files:
            i+=1
    print(i)
    print(j)
def main():
    walk("E:/微信聊天/WeChat Files/wxid_il2j8czws7d821/FileStorage/File/2023-08/陈楚欣2022年度发票汇总")

if __name__=='__main__':
    main()