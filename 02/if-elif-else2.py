"""
@Author: yuanxin.Li
@Time：2025/2/15 20:52
@Version: 1.0
@Description:
"""
age = int(input("请输入您的年龄"))
if age < 18:
    print(f"您的年龄是{age},童工一枚")
elif (age >= 18) and (age <= 60):
    print(f"您的年龄是{age},合法工作年龄")
elif age > 60:
    print(f"您的年龄{age},可以退休")

# if实现三元运算操作
a = 10
b = 20
max = a if a > b else b
print("较大值为%d" % max)
