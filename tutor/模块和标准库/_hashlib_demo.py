
import hashlib

# md5()
psw1 = hashlib.md5()
psw1.update('123456'.encode('utf-8'))   # 默认为Unicode 需要的是bit 所以需要转换
print("密码'123456'用 md5加密后为：",psw1.hexdigest()) #  e10adc3949ba59abbe56e057f20f883e

# sha1()
psw2 = hashlib.sha1()
psw2.update('123456'.encode('utf-8'))
print("密码'123456'用sha1加密后为：",psw2.hexdigest())

# sha3_256()
psw3 = hashlib.sha3_256()
psw3.update('123456'.encode('utf-8'))
print("密码'123456'用sha3_256加密后为：",psw3.hexdigest())

# sha512()
psw4 = hashlib.sha512()
psw4.update('123456'.encode('utf-8'))
print("密码'123456'用sha512加密后为：",psw4.hexdigest())

psw5 = hashlib.sha512('R'.encode('utf-8'))   # 加盐
print("密码'123456'用sha512加盐加密后为：",psw5.hexdigest())


'''
随机生成4位salt，与原始密码组合，通过md5加密

'''
# 导入随机模块
import random

# 获取4位随机大小写字母、数字组成的salt值
def create_salt(length = 4):

    salt = ''

    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

    for i in range(length):

        index = random.randint(0, len(chars))

        salt += chars[index]

    return salt


# 获取原始密码，+salt，用md5加密
def create_md5(mypsw,salt):

    blackpsw = hashlib.md5()

    blackpsw.update((mypsw+salt).encode('utf-8'))

    return blackpsw.hexdigest()


s = create_salt()
mypsw = input('请输入您的密码：')
print("您的密码已加密：",create_md5(mypsw,s))  # 7adf5a3ebac52588ab5b87b24f1bf89e