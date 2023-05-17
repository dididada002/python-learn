# 推导式
# 列表推导式
names = ['jttttt', 'ljjjjjj', 'jkkk']
new_names = [name.upper() for name in names if len(name) > 0]
print(new_names)

nums = [i for i in range(30) if i % 3 == 0]
print(nums)

# 字典推导式
name_dict = {key: len(key) for key in names}
print(name_dict)
name_dict_1 = {key: len(key) + 1 for key in names}
print(name_dict_1)

num_dict = {key: key**2 for key in (2, 4, 6)}
print(num_dict)

# 集合推导式
nums_set = {i**2 for i in (1, 2, 3)}
print(nums_set)

a = {x for x in 'abcdefcdeasxfdxaseghhiu' if x not in 'abc'}
print(a)

# 元组推导式
