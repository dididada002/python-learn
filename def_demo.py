# 无参函数
def hello() :
    print("hello world")

hello()

# 有参函数
def max(a, b) :
    if a > b:
        return a
    else:
        return b

a = 4
b = 5
print(max(a, b))

# 关键词参数：传递参数时使用参数名进行标识，可以不考虑传参的顺序
print(max(b=1, a=3))

# 函数增加默认参数
def friend(friend, me='jt') :
    print(friend,'和', me,'是好朋友')

friend(friend='lj')

# 不定长参数 只能放在函数的最后面，如果不放在函数的最后面，则*后面的所有参数都需要使用关键字传入
def printInfo(args1, *vartuple):
    print('输出：')
    print(args1)
    print(vartuple)
printInfo(70,69,'aaa')

# 不定长参数 **用于匹配一个字典
def printMap(**keymap) :
    print('**keymap',keymap)

printMap(a=1,b='lp',c=123)

# 不定长参数 *不放在最后面
def printNotLast(args1,*args2,args3) :
    print('args1', args1)
    print('args2', args2)
    print('args3', args3)

printNotLast(1,2,3,4,5,args3='abc')


# 匿名函数
sum = lambda x,y: x + y
print(sum(1,2))
