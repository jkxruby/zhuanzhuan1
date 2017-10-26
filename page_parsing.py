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
    soup = BeautifulSoup(wb_data.text, 'lxml')
    part_item_url1 = soup.select('tr.zzinfo.jz td.t a')  # 通过这3行代码，清除了链接中的商家商品，剩余均为个人商品
    part_item_url2 = soup.select('td.t a')
    part_item_url = list(set(part_item_url2) - set(part_item_url1))

    for i in part_item_url:
        item_url = i.get('href').split('?')[0]
        #item_url_list.insert_one( {'url':item_url} )
        print(item_url)

get_item_urls_from('http://bj.ganji.com/shouji/',1)


#=========获取一个商品的详情=========#
#def get_item_info(url,) 剔除商家链接