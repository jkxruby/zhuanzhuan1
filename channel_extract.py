import requests
from bs4 import BeautifulSoup


start_url = 'http://bj.ganji.com/wu/'
wb_data = requests.get(start_url)
soup = BeautifulSoup(wb_data.text, 'lxml')
part_category_links = soup.select('div.main-pop dt a')  # 此变量生成一个字典的集合，无法使用的，当我们通过for in 时，会调出单独的字典，再使用字典函数get()等等

for part_category_link in part_category_links:
    category_links =  start_url.split('/')[2] + str(part_category_link.get('href'))
    print(category_links)

category_links_lists = '''


'''