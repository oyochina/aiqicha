
import caiji
from openpyxl import Workbook,load_workbook
import time,re
book= load_workbook('1.xlsx')

# 获取sheet页
ws = book['Sheet1']


pattern = re.compile(r'<[^>]+>', re.S)


for i in range(309,310):
    name,address = caiji.collection(ws.cell(row=i, column=3).value)
    
    result = pattern.sub('', address)
    ws.cell(i,10).value=result



    print(str(i)+name+':'+result)
    
    time.sleep(2)
    
    #print(ws.cell(row=i, column=3).value)






#r=requests.get(url,params=kv)
#r.encoding='utf-8'
#print(r.request.url)


#path='test.xlsx'
#wb=Workbook()
#ws=wb.active
#ws.title='hello'
#ws.cell(row=1,column=2,value=item['entName'])

#entName=item['entName']
#pattern = re.compile(r'<[^>]+>', re.S)
#result = pattern.sub('', entName)
#ws.cell(2,6).value=result
book.save('1.xlsx')
book.close