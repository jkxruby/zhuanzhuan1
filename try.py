# 略错程序，防止小错误导致程序终止，选择忽略该错误

def try_to_make(ass):
    try:
        print(1/ass)
    except (ZeroDivisionError,TypeError):
        print('ok~')
try_to_make('0')
#  如上，通过 try except 实现忽略错误，可添加在正常程序中，这里只是示范(重要程序有错必究，不能忽略的)