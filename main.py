
import caiji
from openpyxl import Workbook,load_workbook
import time
book= load_workbook('参保.xlsx')

# 获取sheet页
ws = book['Sheet1']





for i in range(3,8):
    name,address = caiji.collection(ws.cell(row=i, column=3).value)
    ws.cell(i,10).value=address



    #print(name)
    #print(address)
    time.sleep(5)
    
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