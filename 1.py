import requests
url="https://aiqicha.baidu.com/s"
hd={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection':'keep-alive',
'sec-ch-ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Referer': 'https://aiqicha.baidu.com/'}
kv={'q':'南通永凡文化传媒有限公司','t':'0'}
r=requests.get(url,headers=hd,params=kv)

#r=requests.get(url,params=kv)
r.encoding='utf-8'
#print(r.request.url)
print(r.text)
