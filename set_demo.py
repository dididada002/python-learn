# 创建一个集合
set_demo = {'aaaa','bbbb','ccccc'}

set_demo_two = set(
    'abc'
)

print('set_demo', set_demo)
print('set_demo_two', set_demo_two)

# 添加元素
set_demo.add('dddd')
print('set_demo add after', set_demo)

# 判断元素是否在集合内
print('元素 in 集合', 'dddd' in set_demo)

# 集合的计算 - 多个集合的差集

# 集合的计算 - 集合的交集

# 集合计算 - 返回集合的

# 移除元素，如果元素不存在，那么会报错
set_demo.remove('dddd')
print('set_demo remove after', set_demo)

# 移除元素，如果元素不存在，也不会报错
set_demo.discard('eeeee')
print('set_demo discard after', set_demo)

# 随机删除元素
set_demo.pop()
print('set_demo pop after', set_demo)

# 计算集合内元素个数
print('len', len(set_demo))

# 清空集合
set_demo.clear()
print('set_demo clear after', set_demo)


