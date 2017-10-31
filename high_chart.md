### 记录jupyter使用

### 目标
统计北京各区二手市场活跃度
### 工作流程
清洗数据；更新数据，整理思路；可视化数据
### 具体方法
```
import charts
import pymongo
```
```
client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
item_info = ceshi['item_infoS']
```
```
# 数据库内的数据是这个样子的
for i in item_info.find().limit(300):
    print(i)
```
下面为打印结果：
`{'pub_date': '2016.01.12', 'time': 0, '_id': ObjectId('5698f524a98063dbe9e91ca8'), 'price': 450, 'url': 'http://bj.58.com/jiadian/24541664530488x.shtml', 'look': '-', 'cates': ['北京58同城', '北京二手市场', '北京二手家电', '北京二手冰柜'], 'title': '【图】95成新小冰柜转让 - 朝阳高碑店二手家电 - 北京58同城', 'area': ['朝阳', '高碑店']}
{'pub_date': '2016.01.14', 'time': 2, '_id': ObjectId('5698f525a98063dbe4e91ca8'), 'price': 1500, 'url': 'http://bj.58.com/jiadian/24349380911041x.shtml', 'look': '-', 'cates': ['北京58同城', '北京二手市场', '北京二手家电', '北京二手洗衣机'], 'title': '【图】洗衣机，小冰箱，小冰柜，冷饮机 - 朝阳定福庄二手家电 - 北京58同城', 'area': ['朝阳', '定福庄']}`
```
pipeline = [
    {'$match':{'$and':[{'pub_date':{'$in':['2015.12.25','2015.12.27']}},{'time':1}]}},     #  筛选函数，这里筛选条件是pub_date和time
    {'$group':{'_id':{'$slice':['$area',1]},'counts':{'$sum':1}}},    # group接收2个参数，_id表示你以什么作为分组，counts为命名，后来跟函数表示你要做什么,sum表示发现一个加1，即计数作用。 主要用于数据的组团计算的,$price区别其他的$,它是表示调用原来的price
    {'$sort' :{'counts':-1}},    # 1表示从小到大正序排列，-1反之
    #{'$limit':3}   # 筛选出出现频率最高三组数
]
# {'pub_date':'2015.12.24'}
```
```
for i in item_info.aggregate(pipeline):
    print(i)
```
打印结果如下：
```
{'_id': ['朝阳'], 'counts': 60}    # 打印结果，非程序
{'_id': ['不明'], 'counts': 59}
{'_id': ['海淀'], 'counts': 38}
{'_id': ['丰台'], 'counts': 26}
{'_id': ['昌平'], 'counts': 18}
```
```
def data_gen(date,time):   # 定义成函数
    pipeline = [
        {'$match':{'$and':[{'pub_date':{'$in':date}},{'time':time}]}},
        {'$group':{'_id':{'$slice':['$area',1]},'counts':{'$sum':1}}},
        {'$sort' :{'counts':-1}},
    ]
    for i in item_info.aggregate(pipeline):
        yield [i['_id'][0],i['counts']]
```
```
for i in data_gen(['2015.12.25','2015.12.27'],1):
    print(i)
```
打印出的结果如下：
```
['朝阳', 60]   # 打印结果，这种格式正式图示化所需要的
['不明', 59]
['海淀', 38]
['丰台', 26]
['昌平', 18]
['通州', 13]
['大兴', 13]
['房山', 9]
['西城', 7]
```
图示化结果：
```
options = {          #  这些都是套路，在highchart 的js代码里找到
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': '饼图'},
    'subtitle': {'text': '城区交易量分布'},
    }


series =  [{
    'type': 'pie',
    'name': 'pie charts',
    'data':[i for i in data_gen(['2015.12.25','2015.12.27'],1)]

        }]
charts.plot(series,options=options,show='inline')
```

![图示](http://upload-images.jianshu.io/upload_images/4265870-b5f4df64c94122c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
