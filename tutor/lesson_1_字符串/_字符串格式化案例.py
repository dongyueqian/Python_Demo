'''
使用给定的宽度打印格式化后的水果名字和价格
参考：_初识字符串1.py
'''
width = int(input('请输入宽度值：'))
price_width = 10
item_width = width - price_width
print("Name的宽度是",item_width)
print("Price的宽度是",price_width)

headerFormat = "%-*s%-*s"
contentFormat = "%-*s%-*.2f"
print("="*width)
print(headerFormat % (item_width,"Name",price_width,"Price"))
print("-"*width)
print(contentFormat % (item_width,"苹果",price_width,4.555))
print(contentFormat % (item_width,"香蕉",price_width,6.99))