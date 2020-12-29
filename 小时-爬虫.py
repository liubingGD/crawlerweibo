import os
import xlwt
import requests
import re
from bs4 import BeautifulSoup
import random
# 设置代理IP
proxy_addr="122.241.72.191:808"


def txt_csv(filename,csvname):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            csv=xlwt.Workbook()
             #生成excel的方法，声明excel
            sheet = csv.add_sheet('sheet1',cell_overwrite_ok=True)
            # 页数、条数、微博地址、发布时间、微博内容、点赞数、评论数、转发数
            sheet.write(0, 0, '爬取页数')
            sheet.write(0, 1, '爬取当前页数的条数')
            sheet.write(0, 2, '用户名')
            sheet.write(0, 3, '微博内容')
            sheet.write(0, 4, '链接')
            sheet.write(0, 5, '微博发布时间')
            x = 1
            while True:
                #按行循环，读取文本文件
                line = f.readline()
                if not line:
                    break  #如果没有内容，则退出循环
                for i in range(0, len(line.split('\t'))):
                    item=line.split('\t')[i]
                    sheet.write(x,i,item) # x单元格行，i 单元格列
                x += 1 #excel另起一行
        csv.save(csvname) #保存xls文件
    except:
        raise

def get_start_end_time(start,end,file):
    header = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
          'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
           'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
          'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)',
          'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0',
          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36',
           'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
           'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
           'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
           'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
           'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36']
    for t1 in range(0,24):
         # 加一句  在保存一个小时的数据的时候输出
        print("==============================================================================================================")
        print("当前爬取"+str(t1)+"小时的数据:")
        i = 1
        headers = {
              "User-Agent":header[random.randint(0,len(header)-1)],
              "cookie":"SINAGLOBAL=2240787892101.7275.1581441790847; _ga=GA1.2.867321920.1604757001; SCF=Aoy_cxXoTgxoj133Hjr3X_CCwprxwet7WhLlb7Cp1hlw15MO05y0uK4C4YLWQa8hrFUX-YustEUscLQWZyRGKMA.; _s_tentry=login.sina.com.cn; Apache=2701524397.672461.1607759723631; ULV=1607759723643:13:4:3:2701524397.672461.1607759723631:1607396339611; cross_origin_proto=SSL; login_sid_t=ac3c9b54eb62342debe3ce61cea41353; SSOLoginState=1607759943; SUB=_2A25y0AgXDeThGeNG71oQ9ijKyzWIHXVuOqhfrDV8PUJbkNAKLUz9kW1NS1v-EymWXbK63t_rGYbCNZpevUyjfNEc; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhaC-8qEoDD5a9NML.YcdGf5NHD95Qf1hBReKqcSo54Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSKnX1h2cSoq71Btt; wvr=6; UOR=ju6y.github.io,widget.weibo.com,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1607844207678%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D"
            }
        starttime = start + "-" + str(t1)
        endtime =  end + "-" + str(t1+1)
        url = "https://s.weibo.com/weibo/%25E7%2596%25AB%25E6%2583%2585?q=%E7%96%AB%E6%83%85&typeall=1&suball=1&timescope=custom:"+starttime+":"+endtime+"&Refer=g&page="
        resp = requests.get(url,headers=headers)  # 给网址发送请求，获取       &Refer=2&page=1
        resp.content.decode("utf-8") #打印网页内容 以二进制返回内容
        html = resp.text
        soup = BeautifulSoup(html,'html.parser')
        page_num = soup.find("div",{"class":"m-page"})
        num = len(page_num.find_all("li"))
        while i<= num:
            import time
            time.sleep(2)
            try:
                j = 0
                url = "https://s.weibo.com/weibo/%25E7%2596%25AB%25E6%2583%2585?q=%E7%96%AB%E6%83%85&typeall=1&suball=1&timescope=custom:"+starttime+":"+endtime+"&Refer=g&page=&page="+str(i)
                headers = {
                  "User-Agent":header[random.randint(0,len(header)-1)],
                  "cookie":"SINAGLOBAL=2240787892101.7275.1581441790847; _ga=GA1.2.867321920.1604757001; SCF=Aoy_cxXoTgxoj133Hjr3X_CCwprxwet7WhLlb7Cp1hlw15MO05y0uK4C4YLWQa8hrFUX-YustEUscLQWZyRGKMA.; _s_tentry=login.sina.com.cn; Apache=2701524397.672461.1607759723631; ULV=1607759723643:13:4:3:2701524397.672461.1607759723631:1607396339611; cross_origin_proto=SSL; login_sid_t=ac3c9b54eb62342debe3ce61cea41353; SSOLoginState=1607759943; SUB=_2A25y0AgXDeThGeNG71oQ9ijKyzWIHXVuOqhfrDV8PUJbkNAKLUz9kW1NS1v-EymWXbK63t_rGYbCNZpevUyjfNEc; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhaC-8qEoDD5a9NML.YcdGf5NHD95Qf1hBReKqcSo54Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSKnX1h2cSoq71Btt; wvr=6; UOR=ju6y.github.io,widget.weibo.com,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1607844207678%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D"
                }
                resp = requests.get(url,headers=headers)  # 给网址发送请求，获取       &Refer=2&page=1
                resp.content.decode("utf-8") #打印网页内容 以二进制返回内容
                html = resp.text
                soup = BeautifulSoup(html,'html.parser') # 解析网页内容 选择解析器'html.parser'(内置的解析器 速度比较慢）（LxmL更快一些 需要安装）
                        #针对当前页存在的微博进行查看
                for h in soup.find_all("div",{"class":"content"}):
                    j+=1
                    print("-----正在爬取第"+str(i)+"页，第"+str(j)+"条微博------")
                    # 获取微博用户的id
                    text = h.find("p",{"class":"txt"})
                    id = text["nick-name"]

                #            print("用户id：",id)
                    # 获取微博内容
                    text = h.find("p",{"class":"txt","node-type":"feed_list_content"})
                    if "展开全文" in str(text):
                        text = h.find("p",{"class":"txt","node-type":"feed_list_content_full"})
                    text = text.text
                    new_text = re.sub(" +", "", text)  # 合并空格
                    new_text1 = re.sub("\n","",new_text)
                #   print("微博内容：",text)

                    # 获取微博的url链接
                    content_url = h.find("p",{"class":"from"}).find("a")
                    content_url = content_url["href"]

                # 获取发布微博的时间
                    for t in h.find_all("p",{"class":"from"}):
                        time1 = t.text
                        new_time = re.sub(" +", "", time1)  # 合并空格
                        new_time1 = re.sub("\n","",new_time)
                    print(new_time1)
                    # 保存文本
                    with open(file,'a',encoding='utf-8') as fh:
                        fh.write(str(i)+'\t'+str(j)+'\t'+str(id)+'\t'+str(new_text1)+'\t'+str(content_url)+'\t'+str(new_time1)+'\n')
                        print("保存第"+str(i)+"页，第"+str(j)+"条微博------")
                    # 休眠1s以免给服务器造成严重负担
                time.sleep(1)
                i+=1

            except Exception as e:
                print(e)
                pass


if __name__=="__main__":
    day = 26
    print("当前爬取的是3月"+str(day)+"日的数据")
    print("==============================================================================")
    start = "2020-03-"+str(day)
    end = "2020-03-"+str(day)
    file = "C:/Users/liubing/微博-爬虫/weibo/weibopachong/2020年3月"+str(day)+"日数据.txt"
    get_start_end_time(start,end,file)

    filename = "C:/Users/liubing/微博-爬虫/weibo/weibopachong/2020年3月"+str(day)+"日数据.txt"
    csvname = "C:/Users/liubing/微博-爬虫/weibo/weibopachong/2020年3月"+str(day)+"日数据.csv"
    txt_csv(filename,csvname)
    os.remove("C:/Users/liubing/微博-爬虫/weibo/weibopachong/2020年3月"+str(day)+"日数据.txt")
