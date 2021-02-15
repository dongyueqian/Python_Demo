'''
多态
'''


class Animal:
    def run(self):
        # return 'Animal is running~'
        print('Animal is running~')

class Cat(Animal):
    def run(self):
        # return 'Cat is running~'
        print('Cat is running~')

class Pig(Animal):
    def run(self):
        # return 'Pig is running~'
        print('Pig is running~')

cat = Cat()
cat.run()

pig = Pig()
pig.run()

print('------------------------------')

animal_list = [Animal(),Cat(),Pig()]
for item in animal_list:
    item.run()
print('------------------------------')

# 不必对run_tow进行任何修改，任何依赖animal做为参数的函数或方法
# 都可以不加修改的正常运行，这就是多态
def run_tow(animal):
    animal.run()
    animal.run()

run_tow(Animal())
run_tow(Cat())
run_tow(Pig())