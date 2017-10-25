import requests
from bs4 import BeautifulSoup


start_url = 'http://bj.ganji.com/wu/'
wb_data = requests.get(start_url)
soup = BeautifulSoup(wb_data.text, 'lxml')
part_category_links = soup.select('div.main-pop dt a')  # 此变量生成一个字典的集合，无法使用的，当我们通过for in 时，会调出单独的字典，再使用字典函数get()等等

for part_category_link in part_category_links:
    category_links =  start_url.split('/')[2] + str(part_category_link.get('href'))
    print(category_links)

category_links_list = '''

bj.ganji.com/shouji/
bj.ganji.com/shoujipeijian/
bj.ganji.com/bijibendiannao/
bj.ganji.com/taishidiannaozhengji/
bj.ganji.com/diannaoyingjian/
bj.ganji.com/wangluoshebei/
bj.ganji.com/shumaxiangji/
bj.ganji.com/youxiji/
bj.ganji.com/xuniwupin/
bj.ganji.com/jiaju/
bj.ganji.com/jiadian/
bj.ganji.com/zixingchemaimai/
bj.ganji.com/rirongbaihuo/
bj.ganji.com/yingyouyunfu/
bj.ganji.com/fushixiaobaxuemao/
bj.ganji.com/meironghuazhuang/
bj.ganji.com/yundongqicai/
bj.ganji.com/yueqi/
bj.ganji.com/tushu/
bj.ganji.com/bangongjiaju/
bj.ganji.com/wujingongju/
bj.ganji.com/nongyongpin/
bj.ganji.com/xianzhilipin/
bj.ganji.com/shoucangpin/
bj.ganji.com/baojianpin/
bj.ganji.com/laonianyongpin/
bj.ganji.com/gou/
bj.ganji.com/qitaxiaochong/
bj.ganji.com/xiaofeika/
bj.ganji.com/menpiao/

'''