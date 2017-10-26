import requests
from bs4 import BeautifulSoup


start_url = 'http://bj.ganji.com/wu/'

def get_category_urls(start_url):
    wb_data = requests.get(start_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    part_category_urls = soup.select('div.main-pop dt a')  # 此变量生成一个字典的集合，无法使用的，当我们通过for in 时，会调出单独的字典，再使用字典函数get()等等

    for part_category_url in part_category_urls:
        category_url =  'http://' + start_url.split('/')[2] + str(part_category_url.get('href'))
        print(category_url)

#get_category_urls(start_url)

category_url_list = '''
http://bj.ganji.com/shouji/
http://bj.ganji.com/shoujipeijian/
http://bj.ganji.com/bijibendiannao/
http://bj.ganji.com/taishidiannaozhengji/
http://bj.ganji.com/diannaoyingjian/
http://bj.ganji.com/wangluoshebei/
http://bj.ganji.com/shumaxiangji/
http://bj.ganji.com/youxiji/
http://bj.ganji.com/xuniwupin/
http://bj.ganji.com/jiaju/
http://bj.ganji.com/jiadian/
http://bj.ganji.com/zixingchemaimai/
http://bj.ganji.com/rirongbaihuo/
http://bj.ganji.com/yingyouyunfu/
http://bj.ganji.com/fushixiaobaxuemao/
http://bj.ganji.com/meironghuazhuang/
http://bj.ganji.com/yundongqicai/
http://bj.ganji.com/yueqi/
http://bj.ganji.com/tushu/
http://bj.ganji.com/bangongjiaju/
http://bj.ganji.com/wujingongju/
http://bj.ganji.com/nongyongpin/
http://bj.ganji.com/xianzhilipin/
http://bj.ganji.com/shoucangpin/
http://bj.ganji.com/baojianpin/
http://bj.ganji.com/laonianyongpin/
http://bj.ganji.com/gou/
http://bj.ganji.com/qitaxiaochong/
http://bj.ganji.com/xiaofeika/
http://bj.ganji.com/menpiao/

'''