import time
from page_parsing import item_url_list
from page_parsing import item_info

while True:
    time.sleep(5)
    print(item_url_list.find().count())
    print(item_info.find().count())
