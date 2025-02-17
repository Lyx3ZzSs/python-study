"""
@Author: yuanxin.Li
@Time：2025/2/11 18:40
@Version: 1.0
@Description:
"""
# 1.接受用户输入
# num = input("请输入您的幸运数字：")

# 2.打印结果
# print(f"您的幸运数字是{num}")

# 3.检查接收到的用户输入的数据类型 -- str类型
# print(type(num))

# 4.转换数据类型为整型 -- int类型
# print(type(int(num)))

# 实验
# 1.float -- 转换成浮点型
num1 = 1
print(float(num1))
print(type(float(num1)))

# 2.str() -- 转换成字符串类型
num2 = 10
print(str(num2))
print(type(str(num2)))

# 3.tuple() -- 将一个列表转换成元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))

# 4.list() -- 将一个元组转换成序列
t1 = (10, 20, 30)
print(list(t1))
print(type(list(t1)))

# 5.eval() -- 将字符串中的数据转换成Python表达式原本类型
str1 = "10"
str2 = "[10,20,30]"
str3 = "(100,200,300)"
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))

