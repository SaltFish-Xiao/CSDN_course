from openpyxl import load_workbook #加载已存在的excel
from openpyxl import Workbook #创建新的excel
from docx import Document #导入docx基础包
from docx.shared import Cm,Inches,Pt #导入单位换算函数
from docx.oxml.ns import qn #中文字体模块
#from docx.enum.text import WD_ALIGN_PARAGRAPH
from docxtpl import DocxTemplate #导入docx的模板操作
from datetime import datetime
import time
monDay = time.strftime('%m%d',time.localtime())
#计算天数差
endTime = datetime.now().date()
startTime = datetime.strptime('2023-02-10',"%Y-%m-%d").date()
diffdays = (endTime-startTime).days+1
#获取月份
current_m = datetime.now().month
#获取日期
current_d = datetime.now().day
import os
os.chdir('D:/1智慧医疗/项目/南京宁惠保3期/理赔/理赔周报/')
loadPath='周报需要的数据.xlsx'
doc = DocxTemplate("南京宁惠保三期情况汇报模板.docx")
wordSavePath='南京宁惠保三期情况汇报{}'.format(monDay)
#excel表格初始化
lista = []
book = load_workbook(loadPath)
#sheet = book['Sheet2']
# try:
#     sheet = book['Sheet1']
# except:
#     print('sheet选取有误,当前名称为{},请检查'.format(sheet))

opening_days_3=diffdays
d20wan="{:,}".format(round((sheet['d'][20].value)/10000))
a20="{:,}".format(sheet['a'][20].value)
b20="{:,}".format(sheet['b'][20].value)
c20="{:,}".format(sheet['c'][20].value)
d20="{:,}".format(sheet['d'][20].value)
e20=round(sheet['e'][20].value*100,2)
e15=round(sheet['e'][15].value*100,2)
g20="{:,}".format(sheet['g'][20].value)
d23="{:,}".format(sheet['d'][23].value)
h20=round(sheet['h'][20].value*100,2)
e23=round(sheet['e'][23].value*100,2)
i20="{:,}".format(sheet['i'][20].value)
j20="{:,}".format(sheet['j'][20].value)
k20="{:,}".format(sheet['k'][20].value)
# 医疗责任
d17wan="{:,}".format(round((sheet['d'][17].value)/10000))
e17=round(sheet['e'][17].value*100,2)
a17="{:,}".format(sheet['a'][17].value)
b17="{:,}".format(sheet['b'][17].value)
c17="{:,}".format(sheet['c'][17].value)
d17="{:,}".format(sheet['d'][17].value)
c5="{:,}".format(sheet['c'][5].value)
c6="{:,}".format(sheet['c'][6].value)
c12="{:,}".format(sheet['c'][12].value)
c7="{:,}".format(sheet['c'][7].value)
c8="{:,}".format(sheet['c'][8].value)
c13="{:,}".format(sheet['c'][13].value)
c9="{:,}".format(sheet['c'][9].value)
c10="{:,}".format(sheet['c'][10].value)
g17="{:,}".format(sheet['g'][17].value)
i15="{:,}".format(sheet['i'][15].value)
c4="{:,}".format(sheet['c'][4].value)
d4=round(sheet['d'][4].value*100,2)
d5=round(sheet['d'][5].value*100,2)
d6=round(sheet['d'][6].value*100,2)
d7=round(sheet['d'][7].value*100,2)
d8=round(sheet['d'][8].value*100,2)
d9=round(sheet['d'][9].value*100,2)
d10=round(sheet['d'][10].value*100,2)
e4="{:,}".format(sheet['e'][4].value)
e5="{:,}".format(sheet['e'][5].value)
e6="{:,}".format(sheet['e'][6].value)
e7="{:,}".format(sheet['e'][7].value)
e8="{:,}".format(sheet['e'][8].value)
e9="{:,}".format(sheet['e'][9].value)
e10="{:,}".format(sheet['e'][10].value)
f4=round(sheet['f'][4].value*100,2)
f5=round(sheet['f'][5].value*100,2)
f6=round(sheet['f'][6].value*100,2)
f7=round(sheet['f'][7].value*100,2)
f8=round(sheet['f'][8].value*100,2)
f9=round(sheet['f'][9].value*100,2)
f10=round(sheet['f'][10].value*100,2)
h17=round(sheet['h'][17].value*100,2)
i17="{:,}".format(sheet['i'][17].value)
j17="{:,}".format(sheet['j'][17].value)
k17="{:,}".format(sheet['k'][17].value)
d18wan="{:,}".format(round((sheet['d'][18].value)/10000))
e18=round(sheet['e'][18].value*100,2)
a18="{:,}".format(sheet['a'][18].value)
b18="{:,}".format(sheet['b'][18].value)
c18="{:,}".format(sheet['c'][18].value)
d18="{:,}".format(sheet['d'][18].value)
b23="{:,}".format(sheet['b'][23].value)
b24="{:,}".format(sheet['b'][24].value)
g18="{:,}".format(sheet['g'][18].value)
c23="{:,}".format(sheet['c'][23].value)
h18=round(sheet['h'][18].value*100,2)
i18="{:,}".format(sheet['i'][18].value)
j18="{:,}".format(sheet['j'][18].value)
k18="{:,}".format(sheet['k'][18].value)
#print(os.path.getmtime(loadPath))

context = {'opening_days_3':opening_days_3,
'd20wan':d20wan,
'current_m':current_m,
'current_d':current_d,
'a20':a20,
'b20':b20,
'c20':c20,
'd20':d20,
'e20':e20,
'e15':e15,
'g20':g20,
'd23':d23,
'i20':i20,
'j20':j20,
'k20':k20,
'h20':h20,
'd17wan':d17wan,
'e17':e17,
'a17':a17,
'b17':b17,
'c17':c17,
'd17':d17,
'c5':c5,
'c6':c6,
'c12':c12,
'c7':c7,
'c8':c8,
'c13':c13,
'c9':c9,
'c10':c10,
'g17':g17,
'i15':i15,
'c4':c4,
'd4':d4,
'd5':d5,
'd6':d6,
'd7':d7,
'd8':d8,
'd9':d9,
'd10':d10,
'e4':e4,
'e5':e5,
'e6':e6,
'e7':e7,
'e8':e8,
'e9':e9,
'e10':e10,
'f4':f4,
'f5':f5,
'f6':f6,
'f7':f7,
'f8':f8,
'f9':f9,
'f10':f10,
'h17':h17,
'i17':i17,
'j17':j17,
'k17':k17,
'd18wan':d18wan,
'e18':e18,
'a18':a18,
'b18':b18,
'c18':c18,
'd18':d18,
'b23':b23,
'b24':b24,
'g18':g18,
'c23':c23,
'h18':h18,
'i18':i18,
'j18':j18,
'k18':k18,
'e23':e23}
doc.render(context)
doc.save("南京宁惠保三期情况汇报{:02d}{:02d}.docx".format(current_m, current_d))