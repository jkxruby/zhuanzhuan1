import requests
from bs4 import BeautifulSoup
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji1 = client['ganji1_db']
item_url_list = ganji1['item_url_list_db']  # 存储所有商品的链接
item_info = ganji1['item_info_db']  # 存储商品的详细信息

#=========获取一个分类下的所有商品链接=========#
# 'bj.ganji.com/shouji/o1/'

def get_item_urls_from(category, pages):
    category_url = '{}o{}/'.format(category, str(pages))
    wb_data = requests.get(category_url)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    part_item_url1 = soup.select('tr.zzinfo.jz td.t a')  # 通过这3行代码，清除了链接中的商家商品，剩余均为个人商品
    part_item_url2 = soup.select('td.t a')
    part_item_url = list(set(part_item_url2) - set(part_item_url1))
    if soup.find('td','t'):
        for i in part_item_url:
            item_url = i.get('href').split('?')[0]
            item_url_list.insert_one( {'url':item_url} )
            print(item_url)
        else:
            pass  # 通过这个判断式来判断爬取翻页到头时自动停止，td t 是商品的标题元素，没它就证明该页面没商品了

#get_item_urls_from('http://bj.ganji.com/shouji/',1)


#=========获取一个商品的详情=========#
def get_item_info(url):
    wb_data = requests.get(url)
    if wb_data.status_code == 404:  # status_code 是requests 自带的一个方法，在一开始的时候检测网页是否有效存在
        pass
    else:
        try:
            soup = BeautifulSoup(wb_data.text, 'lxml')
            data = {
                'title': soup.title.text,
                'price':soup.select('span.price_now i')[0].text,
                'area':  soup.select('.palce_li i')[0].text,
                'url': url
            }
            item_info.insert_one(data)
            print(data)
        except AttributeError:
            pass
#get_item_info('http://zhuanzhuan.ganji.com/detail/923140825311903756z.shtml')


