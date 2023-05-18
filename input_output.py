# 输出,str函数、repr函数
s = 'hello,jt'
print(str(s))
print(repr(s))
print('{}和{}是好朋友'.format('jt', 'tj'))
# 指定格式化的顺序
print('{1}和{0}是好朋友'.format('jt', 'tj'))
# 根据关键字指定顺序
print('{name1}和{name2}是好朋友'.format(name2='张三', name1='李四'))
# 指定填充宽度
print('{name1:10}和{name2:10}是好朋友'.format(name2='张三', name1='李四'))


#输入
str = input('请输入：')
print('您输入的内容是：', str)
