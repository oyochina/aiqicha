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
'Referer': 'https://aiqicha.baidu.com/',
'Cookie': '__yjs_duid=1_fe207f6ebd145963e38088af0dd7f3cb1632553348651; log_guid=f572f5841ace0c8dbd2633b26910a798; _j47_ka8_=57; BAIDUID=7DD04014400D9D22136D5CDC50B11E80:FG=1; BAIDUID_BFESS=7DD04014400D9D22136D5CDC50B11E80:FG=1; ZX_UNIQ_UID=c409472ebc7548bba08f362c9eeadaa1; BIDUPSID=7DD04014400D9D22136D5CDC50B11E80; PSTM=1632563603; delPer=0; PSINO=3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; kleck=91c132c8445c13ee83213772aadaa90b; H_PS_PSSID=34649_34068_34554_34741_34584_34505_34578_26350_34706_34691_34678; _fb537_=xlTM-TogKuTwC615Znve4ARiOLIBbAIieH6dTomiDFg-ABpsxVaGdnsmd; ZX_HISTORY=%5B%7B%22visittime%22%3A%222021-09-25+21%3A56%3A26%22%2C%22pid%22%3A%22xlTM-TogKuTwV-8MPnfHULi59b1VNzNGIwmd%22%7D%2C%7B%22visittime%22%3A%222021-09-25+20%3A56%3A20%22%2C%22pid%22%3A%22xlTM-TogKuTwVrSdDmlKm5R1Et%2ArDJ-CGgmd%22%7D%2C%7B%22visittime%22%3A%222021-09-25+20%3A55%3A12%22%2C%22pid%22%3A%22xlTM-TogKuTw-z725Tq8m5jSWW6jwEdWJAmd%22%7D%2C%7B%22visittime%22%3A%222021-09-25+20%3A55%3A01%22%2C%22pid%22%3A%22xlTM-TogKuTwaq4S7fBn36ZKyDirj4Rbagmd%22%7D%2C%7B%22visittime%22%3A%222021-09-25+20%3A54%3A33%22%2C%22pid%22%3A%22xlTM-TogKuTwCERCoohJSXXV2TqI5hmqeQmd%22%7D%2C%7B%22visittime%22%3A%222021-09-25+20%3A53%3A49%22%2C%22pid%22%3A%22xlTM-TogKuTw7zgKg2ppe3BpJQDJ%2AWPb1Qmd%22%7D%5D; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1632574375,1632574584,1632582420,1632582427; __yjs_st=2_NjY2NjA4MmQ1YmFkNjM5YjlkM2NhZGQzODY1M2I0NTk2OGU3NGU0MjUxZjEzNGJkNjVlYjkzZDYxYTgyM2RiODQ3YTY2NTBhY2U1ZTFhNjk3YTNmYjc4OTJhMWIyMWNjNmY1MWI3Mzg5ZWIzMDFmYjhkZjNhNzVmNzZmYzFlZjQ1Yzg4M2QzMjk2YzQ0OTgwMjhkZTkzODM4MDlhNDEwMjY2NmM4ZTIyZWJmNzAxMTcwZmUwYmQ2ZGNkOTU3ODdiMTYyMDE4YTUxNzNlZmIwZmU2NGI3NjgxMzM1M2ZkOWFmMTlmMDIyMDcyZTZjZWQ3ZjJjYzhjODllYzUxZDhiMF83XzczNzM5MTIw; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1632582611; ab_sr=1.0.1_ZmQ2MTEzM2VlNDAwMTA0NDdlZTFhMTMzMmY1NTM2YWExMWI5Nzc0MDY5MjFkNjgyM2RkMTg0YTUwYzQzZTE3N2YzMGNhOGQ4Y2ZiZjU0MTgxMzRiODJkMzJhM2U1NWY2YmQ4ZjdjNjc3ZWQwMTIzMGU0MWVkZDg4ZWQ1Nzk4ZTQ3YTE0ZTI3NjQ3ODU0ZmNmZTdkMDBkNWMzMjJhNTY0NA==; _s53_d91_=e27d644896d1800d6f2981fcb981e321adea0c9c207d962fd7fd1650b06e7c64d352812de00d5ecddceb68e28b0a0437dba53c76cee047fa70e439f81d3bad144e0aa995c8b2467472d6ed141ef4fe650ae89f0754bdcad9bce6ab495b66d1cd967cd0da7a22c60ec62d08ccc86359a72957d8f9cf5718eada9d90796ecbfad31bdf95e122cc74c37b377f65857e3e10a927734513a18e8e66cb93064dbedda37c815694c4bccd89a73bb08826fa2f5b2d0e9ac4a2bf1208df3d5c6d508067f98ae6ba1b00425b5604a3464425f400f4e7a0132febb0def280ca2eb88d34a4a1; _y18_s21_=fda90423; RT="z=1&dm=baidu.com&si=1vfyf3m1bw6&ss=ktzxf45z&sl=6&tt=c82&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=45zh&ul=i5jm"'}
kv={'q':'启东一胜网络','t':'0'}
r=requests.get(url,headers=hd,params=kv,)

#r=requests.get(url,params=kv)
r.encoding=r.apparent_encoding
print(r.request.url)
print(r.text)
