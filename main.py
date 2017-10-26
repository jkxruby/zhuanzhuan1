import requests
from bs4 import BeautifulSoup
import time
import pymongo
from channel_extract import get_category_urls
from page_parsing import get_item_urls_from
from page_parsing import get_item_info
from page_parsing import item_url_list
from page_parsing import item_info
#=============获取所有的链接==============#
def get_all_urls_from(start_url,pages):
    for i in get_category_urls(start_url):
        j = get_item_urls_from(i, pages)
        item_url_list.insert_one({ 'url':j })

#get_all_urls_from(start_url, 10)

#================获取所有商品的详情=================#
def get_all_item_info(url):
    for k in j:
        m = get_item_info(j)
        item_info.insert_one({'goods':m})
#get_all_item_info(url)
