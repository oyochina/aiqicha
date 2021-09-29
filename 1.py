import requests
import json

def parse_index(content, flag=True):
    tag_2 = '/* eslint-enable */</script><script data-app'
    tag_1 = 'window.pageData ='
    idx_1 = content.find(tag_1)
    idx_2 = content.find(tag_2)
    # 判断关键词区间中的JSON数据来进行匹配
    if idx_2 > idx_1:
        # 关键词提取判断，去除多余字符
        mystr = content[idx_1 + len(tag_1): idx_2].strip()
        mystr = mystr.replace("\n", "")
        mystr = mystr.replace("window.isSpider = null;", "")
        mystr = mystr.replace("window.updateTime = null;", "")
        mystr = mystr.replace(" ", "")
        mystr = mystr.replace("if(window.pageData.result.isDidiwei){window.location.href=`/login?u=${encodeURIComponent(window.location.href)}`}", "")
        mystr = mystr.replace(" ", "")
        len_str = len(mystr)
        if mystr[len_str - 1] == ';':
             mystr = mystr[0:len_str - 1]
        # 数据JSON转化
        j = json.loads(mystr)
        # 判断数据
        if flag:
            return j["result"]

        if len(j["result"]["resultList"]) > 0:
            item = j["result"]["resultList"][0]
            return item
        else:
            # 返回可能没查到企业信息
            return None

    else:
        #logger.error("【关键词数据提取失败】 {}".format(idx_1))
        return None



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
content=r.text
item=parse_index(content)
#r=requests.get(url,params=kv)
r.encoding='utf-8'
#print(r.request.url)
print(item)
