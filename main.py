
from multiprocessing import Pool
from page_parsing import get_item_urls_from
from page_parsing import get_item_info
from page_parsing import item_url_list
from page_parsing import item_info
from channel_extract import category_url_list

#=============防止程序中断===============#
db_urls = [ item['url'] for item in item_url_list.find() ]  # 从数据库中find字典元素，用item调用出key 'url'对应的value,也就是网址，并形成列表
index_urls = [ item['url'] for item in item_info.find() ]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x - y

#=============获取所有的链接==============#

def get_all_urls_from(category):
    for i in range(1,10):
        get_item_urls_from(category,i)

if __name__=='__main__':
    pool = Pool(processes= 4)
    result1 = pool.map(get_all_urls_from, category_url_list.split())  # split()会将长字符串变成一个 列表，map直接从列表里依次拿元素
    pool.close()
    pool.join()
    if result1.successful():
        print('result1 successful')

#================获取所有商品的详情=================#

def get_all_item_info(url):
    for i in rest_of_urls:
        get_item_info(i)

    pool = Pool(processes= 4)
    result2 = pool.map( get_all_item_info,  rest_of_urls )
    pool.close()
    pool.join()
    if result2.successful():
        print('result2 successful')



