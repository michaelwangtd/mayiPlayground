#!/usr/bin python
# -*- coding:utf-8 -*-

from utils import fileops
import re

if __name__ == '__main__':

    fr = open('../data/traceinit_analysis_beta.log','r',encoding='utf-8')
    fw = open('../data/traceinit_analysis_gamma.log','w',encoding='utf-8')
    i = 1
    while True:
        line = fr.readline()
        if line:
            line = line.replace('tenant:','').replace('landlord:','').strip()
            if not line.isdigit():
                if not re.search('^您好，我们一行.*',line,re.S):
                    re1 = '\d+个人|\d+分钟|\d+元|\d+个半|\d*点|价格是\d+|\d+层|一宿\d+|\d+m|\d+米\d+|\d+站|\d+楼|\d+室|\d+人' \
                          '|\d+公里|密码\d+|短信是\d+|\d+F|\d+号线|\d+岁|\d+\.\d+米|\d+\-\d+公里|\d+套|\d+张|\d+\-\d+人' \
                          '|\d+折|\d+\.\d+折|\d+天|\d+个站|\d+路|\d+居|\d+度|\d+成交|一张\d+\.\d+|\d+米|\d+个大人|\d+个' \
                          '|打车\d+|\d+\*\d+|\d+左右|\d+w|\d+W|\d+晚|\d+\?|\d+\？|\d+个月|手机号码.*\d+|\d+那套|\d+这套' \
                          '|\d+吧|\d+一次|\d+座|\d+的|\d+得了|\d+\:\d+|\.\d+|\d+号中午|\d+号早上|\d+中午|\d+号退房|坐\d+' \
                          '|\d+啊|\d+一夜|\d+一天|\d+一晚|\d+年|\d+平|\d+多平|\d+行不行|\d+周|\d+\.\d+宽|一个\d+\.\d+' \
                          '|订\d+号|\d+号\？|\d+号\?|\d+行吗|\d+\：\d+|订金\d+|\d+订金|\d+千|每晚\d+|平时是\d+|\d+房间|A' \
                          '\d+|\d+里路|周末是\d+|\d+\s*人|\d+\s*楼|\d+小时|一个月\d+|最低\d+|\d+每月|\d+吗|\d+月份|\d+呢' \
                          '|\d+退房|B\d+|\d+乘\d+|\d+位|价位.*\d+|\d+单元|押金\d+|\d+每天|\d+间|每天\d+|\d+号线|订单号\d+|优惠\d+' \
                          '|节假日\d+|\d+一个月|今天\d+|\d+号晚上|\d+号上午|\d+号之后|\d+多分钟|\d+块|\d+号早|\d+号到|\d+号退|'
                    line = re.sub(re1,'',line).strip()
                    if line:
                        if re.search('(\d+)', line, re.S):
                            flag = False
                            targetList = ['月','日','-','.','，',',','～','~','到','至','号','天']
                            for target in targetList:
                                if target in line:
                                    flag = True
                                    break
                            if flag:
                                # print('-------',line)
                                # 将之前匹配的正则都匹配完，剩下的就是其他类型的
                                re1 = '\d+月\d+日\-\d+月\d+日'
                                re2 = '\d+[\.|\,|\，]\d+[\-|到|\～|至|\~]\d+[\.|\,|\，]\d+'
                                # if re.search(re1 + '|' + re2,line,re.S):
                                line = re.sub(re1+'|'+re2,'',line)
                                re3 = '\d+月\d+[日|号][\-|至|到|\～|\~]\d+[日|号]'
                                line = re.sub(re3,'',line)
                                re4 = '\d+[到|\-|\～|至|\~]\d+[日|号]'
                                re5 = '\d+[号|日][到|至|\-|\～|\~]\d+[号|日]'
                                line = re.sub(re4+'|'+re5,'',line)
                                re6 = '\d+\.\d+\.\d+[号|日]'
                                re7 = '\d{3,6}号'
                                re8 = '\d+\.\d+\.\d+三.'
                                line = re.sub(re6+'|'+re7+'|'+re8,'',line)
                                re9 = '\d+[和]\d+两.'
                                line = re.sub(re9,'',line)
                                re10 = '\d+[\.|\,|\，|\,]\d[号|日]'
                                line = re.sub(re10,'',line)
                                re11 = '\d+\.\d+'
                                line = re.sub(re11,'',line)
                                if re.search('(\d+)', line, re.S):
                                    print(i,line)
                                    fw.write(line + '\n')
                                    i += 1
    fw.close()
    fr.close()
