import requests
import json
import random

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

def build_headers(referer=None):
        if not referer:
            referer = 'https://aiqicha.baidu.com/'
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/68.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) '
            'Gecko/20100101 Firefox/68.0',
            'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/68.0'
        ]
        ua = random.choice(user_agents)
        headers = {
            'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
            'Connection': 'Keep-Alive',
            'Cookie': 'BIDUPSID=74E1BB0581123443B047EFE2912719C3; PSTM=1607598182; BAIDUID=74E1BB05811234434C178C92D65E4707:FG=1; H_WISE_SIDS=164371_161578_163320_160248_160662_156286_163806_159614_162898_163702_159547_163302_151532_162372_159382_164577_159937_164289_162904_160879_161125_164298_164696_127969_164164_161560_163979_161443_163338_164605_163292_131423_156071_158983_162615_163522_161567_107320_164001_163411_160573_161965_163271_144966_159797_154212_161237_158640_155689_163748_155932_163118_164284_162267_164074_161774_164448_162643_159092_162975_162156_110085_162025_163321_163568_163566_164962; BDUSS=pFV2l6UWQtZGk4ZHB5UjVwRndaam9BSXRLUEVJekxrMlRufmVSeHlLd2N6UWRnSVFBQUFBJCQAAAAAAAAAAAEAAAD4FWEib3lvY2hpbmExMTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABxA4F8cQOBfeU; BDUSS_BFESS=pFV2l6UWQtZGk4ZHB5UjVwRndaam9BSXRLUEVJekxrMlRufmVSeHlLd2N6UWRnSVFBQUFBJCQAAAAAAAAAAAEAAAD4FWEib3lvY2hpbmExMTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABxA4F8cQOBfeU; BDPPN=a78d05322f2caa8f221ecd79f988f8b7; _j54_6ae_=xlTM-TogKuTwMCEomaRR-402V6yz6-YRRQmd; Hm_lvt_baca6fe3dceaf818f5f835b0ae97e4cc=1614571809; log_guid=d78e2d4959261674c0e16be210adb9c4; _j47_ka8_=57; __yjs_duid=1_30d14ba72477e0a76bbe71538ed4f4d51619960624321; BAIDUID_BFESS=74E1BB05811234434C178C92D65E4707:FG=1; MCITY=-:; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=34651_34531_34068_34748_34654_34742_34525_34584_34518_26350_34729_34415_34697_34677; BA_HECTOR=8h8084ak242k2kah2a1glank70q; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1632618436,1632639488,1632704481,1632986427; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1632986439; ab_sr=1.0.1_N2M3MWI2YzYzYjdmMWY1OGUyMmY1ODk4ZWM1ODhjYmNiNmM2NDliZTdhMTIwZWQwNzBjMGNjYTllYTBkMDc3MzYxMDU4MDIwOTA3YWNlYzBhOTM3NDk1ZWZhNmJkNmUzZDBiMWMzYjQwM2ZlYWRjNGY0Y2RiMmU5OGRlNTA0YzlmYWYyOGZmMTU2MTE0OWZkZmEyY2U5YzAzN2ExYTEzOA==; _s53_d91_=e27d644896d1800d6f2981fcb981e321adea0c9c207d962fd7fd1650b06e7c64d352812de00d5ecddceb68e28b0a0437a4294aede271a18d392d6450c6825c053aab31022c1d3cdd996587d82da73779b641544ab9df5a0d4c3a70cd79ea1bd702c4378c500771db1789148f1ead30fc9f7b1ad612d8a8f17d27dc5cabf51c729f5f35ddfe7f6344565256e77df2d14ba93786ba98dd151243842e090207bfdd7642a6915f1bc80d3147221470657510b00c215df29dad337c1fb63346b8770df455d9f81193af9602337cdb1e1db724; _y18_s21_=3908ff40; __yjs_st=2_YzFiYmJhY2JjYzYyMDBlZThlNmQ4NWUyN2ZjNjA0OTc5NjA5MjU0ZjRjZDc2MmJjMmUyMjNkMThhYjcwOTc1ZDJiYzk3NzYwOGU5YWMzZjQ5YmU3NGUzOWU5ZWFjYzgzZmIzYjFkMzdiMDg1MGY5ZDY1MjM1OGE2NzI4N2I0NjdiOGQ5MjI5YzlkMzliOGZjYjJjMTExOTE4MGRjZDRiZGQzNjJlOGE5YjBmNzNiZjJjNGRkZTFjMGI2OTNiZmQyMTYzN2Q4OTMxZjEwYTZmYTIxNmYzMjhjN2IxYjBmNzhlMjUxYmFkNjc3MmI3MDBiMGFiOTViNjAwMzI3NjM1YV83X2Q5OWQ1Nzg3; RT="z=1&dm=baidu.com&si=omaf3gi6w0o&ss=ku6lyebd&sl=7&tt=4ol&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=c2o&ul=r6x"',
            'Referer': referer,
            'User-Agent': ua
        }
        return headers

url="https://aiqicha.baidu.com/s"

'''hd={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection':'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Cookie':'BIDUPSID=74E1BB0581123443B047EFE2912719C3; PSTM=1607598182; BAIDUID=74E1BB05811234434C178C92D65E4707:FG=1; H_WISE_SIDS=164371_161578_163320_160248_160662_156286_163806_159614_162898_163702_159547_163302_151532_162372_159382_164577_159937_164289_162904_160879_161125_164298_164696_127969_164164_161560_163979_161443_163338_164605_163292_131423_156071_158983_162615_163522_161567_107320_164001_163411_160573_161965_163271_144966_159797_154212_161237_158640_155689_163748_155932_163118_164284_162267_164074_161774_164448_162643_159092_162975_162156_110085_162025_163321_163568_163566_164962; BDUSS=pFV2l6UWQtZGk4ZHB5UjVwRndaam9BSXRLUEVJekxrMlRufmVSeHlLd2N6UWRnSVFBQUFBJCQAAAAAAAAAAAEAAAD4FWEib3lvY2hpbmExMTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABxA4F8cQOBfeU; BDUSS_BFESS=pFV2l6UWQtZGk4ZHB5UjVwRndaam9BSXRLUEVJekxrMlRufmVSeHlLd2N6UWRnSVFBQUFBJCQAAAAAAAAAAAEAAAD4FWEib3lvY2hpbmExMTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABxA4F8cQOBfeU; BDPPN=a78d05322f2caa8f221ecd79f988f8b7; _j54_6ae_=xlTM-TogKuTwMCEomaRR-402V6yz6-YRRQmd; Hm_lvt_baca6fe3dceaf818f5f835b0ae97e4cc=1614571809; log_guid=d78e2d4959261674c0e16be210adb9c4; _j47_ka8_=57; __yjs_duid=1_30d14ba72477e0a76bbe71538ed4f4d51619960624321; BAIDUID_BFESS=74E1BB05811234434C178C92D65E4707:FG=1; MCITY=-:; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=34651_34531_34068_34748_34654_34742_34525_34584_34518_26350_34729_34415_34697_34677; BA_HECTOR=8h8084ak242k2kah2a1glank70q; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1632618436,1632639488,1632704481,1632986427; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1632986439; ab_sr=1.0.1_N2M3MWI2YzYzYjdmMWY1OGUyMmY1ODk4ZWM1ODhjYmNiNmM2NDliZTdhMTIwZWQwNzBjMGNjYTllYTBkMDc3MzYxMDU4MDIwOTA3YWNlYzBhOTM3NDk1ZWZhNmJkNmUzZDBiMWMzYjQwM2ZlYWRjNGY0Y2RiMmU5OGRlNTA0YzlmYWYyOGZmMTU2MTE0OWZkZmEyY2U5YzAzN2ExYTEzOA==; _s53_d91_=e27d644896d1800d6f2981fcb981e321adea0c9c207d962fd7fd1650b06e7c64d352812de00d5ecddceb68e28b0a0437a4294aede271a18d392d6450c6825c053aab31022c1d3cdd996587d82da73779b641544ab9df5a0d4c3a70cd79ea1bd702c4378c500771db1789148f1ead30fc9f7b1ad612d8a8f17d27dc5cabf51c729f5f35ddfe7f6344565256e77df2d14ba93786ba98dd151243842e090207bfdd7642a6915f1bc80d3147221470657510b00c215df29dad337c1fb63346b8770df455d9f81193af9602337cdb1e1db724; _y18_s21_=3908ff40; __yjs_st=2_YzFiYmJhY2JjYzYyMDBlZThlNmQ4NWUyN2ZjNjA0OTc5NjA5MjU0ZjRjZDc2MmJjMmUyMjNkMThhYjcwOTc1ZDJiYzk3NzYwOGU5YWMzZjQ5YmU3NGUzOWU5ZWFjYzgzZmIzYjFkMzdiMDg1MGY5ZDY1MjM1OGE2NzI4N2I0NjdiOGQ5MjI5YzlkMzliOGZjYjJjMTExOTE4MGRjZDRiZGQzNjJlOGE5YjBmNzNiZjJjNGRkZTFjMGI2OTNiZmQyMTYzN2Q4OTMxZjEwYTZmYTIxNmYzMjhjN2IxYjBmNzhlMjUxYmFkNjc3MmI3MDBiMGFiOTViNjAwMzI3NjM1YV83X2Q5OWQ1Nzg3; RT="z=1&dm=baidu.com&si=omaf3gi6w0o&ss=ku6lyebd&sl=7&tt=4ol&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=c2o&ul=r6x"',
'Referer': 'https://aiqicha.baidu.com/'}'''


kv={'q':'南通永凡文化传媒有限公司','t':'0'}
r=requests.get(url,headers=build_headers(),params=kv)
content=r.text
item=parse_index(content)
#r=requests.get(url,params=kv)
r.encoding='utf-8'
#print(r.request.url)
print(item)
