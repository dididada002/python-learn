# 创建空字典
emptyDict = dict()
print(emptyDict)

# 获取字典中的值
tinydict = {'Name': 'JingTeng', 'Age': 30, 'Class': 'First'}
print(tinydict['Name'])
print(tinydict['Age'])

# 修改字典
tinydict['Age'] = 31
print(tinydict['Age'])

# 删除字典元素
del tinydict['Age']     # 删除字典中的某个键
tinydict.clear()    # 清空字典中的所有键值对
del tinydict        # 删除字典

# 内置方法
demoDict = {'Name': 'JingTeng', 'Age': 30, 'Class': 'First'}
copyDict = demoDict.copy()
print('copyDict:', copyDict)    # 复制字典
seq = ('Name', 'Age')
fromDict = demoDict.fromkeys(seq)   #从之前的字典中指定某些key，创建一个新的字典
print('fromDict', fromDict)
if 'Age' in demoDict:
    print('这个key Age在当前的字典中存在')     # in 这个字典是否包含了这个key

if 'Sex' not in demoDict:
    print('这个key Sex不在当前的字典中')

items = demoDict.items()        # items方法 返回可视图对象，keys、values、items方法都不能对原来的字典进行修改
for i,j in items:
    print('i j :', i, j)

keys = demoDict.keys()
print('keys', keys)
values = demoDict.values()
print('values', values)

name = demoDict.pop('Name')     # pop方法，删除并返回这个value
print('name:',name)
print('demoDict',demoDict)

popLast = demoDict.popitem()    # popLast方法，删除并返回最后一个键值对
print('popLast', popLast)
print('demoDict',demoDict)















