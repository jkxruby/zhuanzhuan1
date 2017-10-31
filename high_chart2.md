### 问题：某段时间内，北京各个城区发帖数量的 top3 类目

所需数据结构：
原始 :`series = [{'name': 'name','data': [100]},{'name': 'name','data': [100]}]`

实际上：`{name:类目，data:发帖量}`

目标：`{'_id': ['北京二手家电'], 'counts': 175}`

### 柱形图所需数据格式如下:
```
series = [
    {
    'name': 'name',
    'data': [100],
    'type': 'column'
},{
    'name': 'name2',
    'data': [102],
    'type': 'column'
}]
    

options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': '发帖数量最大的类目'},
    'subtitle': {'text': '数据图表'},
    'yAxis'   : {'title': {'text': '数量'}}
    }

charts.plot(series,options=options,show='inline')
```
<hr>

```
pipeline1 = [
    {'$match':{'$and':[{'pub_date':{'$gte':'2015.12.25','$lte':'2015.12.27'}},{'area':{'$all':['朝阳']}}]}},
    {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
    {'$limit':3}
]

for i in item_info.aggregate(pipeline1):
    print(i)
```

打印的结果如下：
```
{'_id': ['北京二手图书/音像/软件'], 'counts': 32}
{'_id': ['北京其他二手物品'], 'counts': 26}
{'_id': ['北京二手办公用品/设备'], 'counts': 86}
```

```
def data_gen(date1,date2,area,limit):
    pipeline1 = [
    {'$match':{'$and':[{'pub_date':{'$gte':date1,'$lte':date2}},{'area':{'$all':area}}]}},
    {'$group':{'_id':{'$slice':['$cates',2,1]},'counts':{'$sum':1}}},
    {'$limit':limit},
    {'$sort':{'counts':-1}}
]

    for i in item_info.aggregate(pipeline1):
        data = {
            'name': i['_id'][0],
            'data': [i['counts']],
            'type': 'column'
        }
        yield data
```

```
for i in data_gen('2015.12.25','2015.12.27',['朝阳'],3):
    print(i)
```

打印结果如下：
```
{'name': '北京二手图书/音像/软件', 'type': 'column', 'data': [32]}
{'name': '北京其他二手物品', 'type': 'column', 'data': [26]}
{'name': '北京二手办公用品/设备', 'type': 'column', 'data': [86]}
```
柱形图展示套路
```
series = [i for i in data_gen('2015.12.25','2015.12.27',['朝阳'],5)]
options = {
    'chart'   : {'zoomType':'xy'},
    'title'   : {'text': '发帖数量最大的类目'},
    'subtitle': {'text': '数据图表'},
    'yAxis'   : {'title': {'text': '数量'}}
    }

charts.plot(series,options=options,show='inline')
```

![Snip20171031_34.png](https://i.loli.net/2017/10/31/59f8712b39bd8.png)








