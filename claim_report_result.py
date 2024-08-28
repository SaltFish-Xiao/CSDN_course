from  claimreport import ClaimReport
from docxtpl import DocxTemplate
import datetime as dt
import sqlgather as sg
import time
doc = DocxTemplate("南京宁惠保情况汇报_模板.docx")
if __name__=='__main__':
    days = (dt.date.today() - dt.datetime.strptime('2022-02-10', "%Y-%m-%d").date()).days
    month = dt.date.today().month
    day = dt.date.today().day
    a=ClaimReport()
    #二期数据
    noa=f'{int(a.implement(sg.noa)[0][0]):,d}'#申请数
    nocc=f'{int(a.implement(sg.nocc)[0][0]):,d}' #结案数
    nocs=f'{int(a.implement(sg.nocs)[0][0]):,d}' #理赔数
    tcp=f'{a.implement(sg.tcp_ir_pcc)[0][0]:,.2f}' #赔付金额
    ir_2=format(a.implement(sg.tcp_ir_pcc)[0][1]*100,'.2f') #赔付率
    pcc=f'{a.implement(sg.tcp_ir_pcc)[0][2]:,.2f}' #人均赔付
    aiwlr=format(a.implement(sg.aiwlr)[0][0]*100,'.2f') #减负率
    tme=f'{a.implement(sg.tme_ssp_ib)[0][0]:,.2f}'#总费用
    ssp=f'{a.implement(sg.tme_ssp_ib)[0][1]:,.2f}' #统筹
    ib=f'{a.implement(sg.tme_ssp_ib)[0][2]:,.2f}' #个人负担
    payment_amount=f'{float(a.implement(sg.tcp_ir_pcc)[0][0])/10000:,.0f}'
    ir_1=format(a.implement(sg.ir_1)[0][0]*100,'.2f') #一期赔付率
    #三期数据

    context = {'opening_days':days,'payment_amount':payment_amount,'current_m':month,'current_d':day,'noa':noa,'nocc':nocc,'nocs':nocs,'tcp':tcp,'ir_2':ir_2,'pcc':pcc,'aiwlr':aiwlr,'tme':tme,'ssp':ssp,'ib':ib,'ir_1':ir_1}
    doc.render(context)
    doc.save("南京宁惠保情况汇报{:02d}{:02d}.docx".format(month,day))



