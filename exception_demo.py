# -*- coding: UTF-8 -*-
def except_demo():
    raise Exception('我错了')

while True:
    try:
        x = int(input("请输入一个整数："))
        except_demo()
        break
    except ValueError:
        print("非数字重新输入")
    except Exception:
        print('未知错误')
    else:
        print('没有出错')
    finally:
        print('结束了')

