# 打开文件 区分不同的模式
# file = open('name.txt', 'a')
#
# # 写入 w模式会覆盖 a模式会续写
# file.write('我是第一行')
# file.write('\n')
# file.write('我是第二行')
# file.close()

# 读 read 无参代表读取所有数据，有参代表读取到指定的光标
file_read = open('name.txt', 'rb')
print(file_read.read())


# 读 readline 读取一行
file_read_line = open('name.txt', 'r')
print(file_read_line.readlines())


# 读 readlines 读取所有行 无参数代表返回所有行，有参数代表读取行数的限制
file_read_lines = open('name.txt', 'r')
print(file_read_lines.readlines())

# 光标 文件中光标指针所处的位置
print('光标所处的位置', file_read.tell())

# 光标 改变光标指针所处的位置 seek(offset, from_what)
# offset 偏移量
# from_what 0-代表从文件开始处向后移动 1-代表从光标当前位置向后移动 2-代表从文件末尾开始向前移动
print('光标所处的位置', file_read.tell())
print(file_read.read(1))
file_read.seek(1, 1)
print('光标所处的位置', file_read.tell())





file_read.close()
file_read_line.close()
file_read_lines.close()
