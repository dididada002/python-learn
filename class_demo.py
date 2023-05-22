# -*- coding: UTF-8 -*-

class MyClass:
    i = 12345
    def __int__(self):
        print('init function')
    def f(self):
        return 'hello world'

x = MyClass()

print('MyClass 类的属性i为',x.i)
print('MyClass类的方法f输出为：',x.f())

class people:
    name = ''
    age = 0
    # 私有属性 以‘__’为前缀的属性
    __weight = 100
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speek(self):
        print('%s 说：我%s岁'%(self.name, self.age))
    def getWeight(self):
        return self.__weight

pp = people('linjie',20,130)
print(pp.getWeight())
pp.speek()

# 类的继承
class Student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self, n, a, w)
        self.grade = g
    def speek(self):
        print('%s说：我%s岁了，我在读%d年级'%(self.name, self.age, self.grade))

s = Student('jt', 33, 120, 2)
s.speek()

# 多继承
class Speeker():
    topic = ''
    def __init__(self, t):
        self.topic = t
    def speek(self):
        print('今天演讲主题是：%s' % self.topic)
# 多继承，如果当前类没有这个方法，那么就会从父类中搜索这个方法，顺序是从左到右，下面这个例子中，DemoSpeeker没有speek方法，那就从Speeker找这个方法，如果没有，那就从Student找这个方法
class DemoSpeeker(Speeker,Student):
    def __init__(self, n, a, w, g, t):
        Student.__init__(self,n,a,w,g)
        Speeker.__init__(self,t)

test = DemoSpeeker('jt', 33, 120, 2, 'doi')
test.speek()
print(test.getWeight())