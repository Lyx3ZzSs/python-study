"""
@Author: yuanxin.Li
@Time：2025/10/2 14:14
@Version: 1.0
@Description:
"""
# 1) 赋值运算符案例
num1 = 10
i = 100
i += 100
print("i=", i)
i -= 100
print("i=", i)
i *= 3
print("i=", i)

# 2)有两个变量，a和b，要求将其进行交换，最终打印结果
a = 30
b = 40
"""
    1. 先定义一个中间变量temp
    2. temp = a  # 先把a的值保存到temp
    3. a = b # 把b的值赋给a
    4. b = temp #把temp(即a)的值赋给b
"""
print(f"没有交换之前a={a},b={b}")
temp = a
a = b
b = temp
print(f"交换之后a={a},b={b}")

"""
    在python中支持一个简单的方式实现变量交换
    x , y = y, x
"""
print(f"没有交换之前a={a},b={b}")
a, b = b, a
print(f"交换之后a={a},b={b}")
