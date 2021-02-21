
import cgi
# class dummy:
#     def __init__(self, myname=None, myage=None, mysex=None, myurl=None):
#         self.myname = myname
#         self.myage = myage
#         self.mysex = mysex
#         self.myurl = myurl
# # 自己构造的form对象
# form = {
#     'name': dummy(myname='liy'),
#     'age': dummy(myage=18),
#     'sex': dummy(mysex='male'),
#     'url': dummy(myurl='/test/')
# }
# # 如何调用
# print(form['name'].myname)
# print(form['age'].myage)
# print(form['sex'].mysex)
# print(form['url'].myurl)



# cgi方法生成的form对象
# form = '/cgi-bin/test.py?name=菜鸟教程&url=http://www.runoob.com'
form = cgi.FieldStorage('/cgi-bin/test.py?name=菜鸟教程&url=http://www.runoob.com')
print()
site_name = form.getvalue('name')
site_url = form.getvalue('url')
print(site_url,site_name)