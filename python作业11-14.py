"""
    1.利用map函数，把用户输入的不规范输入统一变为首字母大写，例如：
    输入['adam','LISA','barT']，得到['Adam', 'Lisa', 'Bart']

    2.sum函数可以接受一个list并求和，试编写prod函数，传入list并用reduce函数求积

    #code with python 3.6.9
"""

#question1
from functools import reduce


def transfer(name):
    for char in name:
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            if 'A' <= char <= 'Z':
                char.lower()  #将大写变为小写，已经是小写的则不变
        else:
            print('Not a regular name!\n')  #非常规字符输入则报错
    return name.title()


print(list(map(transfer, ['adam', 'LISA', 'barT'])))
    #python3 map()返回一个迭代器，需要转换为list输出


#question2


def prod(lst):
    result = reduce(lambda x, y: x*y, lst)
    return result


TEST_LIST = [var for var in range(1, 10)]
            #预期结果为 9!=362880
print("The test list for the function is:", TEST_LIST)
print("The result is:", prod(TEST_LIST))


