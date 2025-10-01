"""
@Author: yuanxin.Li
@Time：2025/10/1 15:36
@Version: 1.0
@Description:
"""

# Python 根据变量使用的上下文（即当前值）在运行时决定的类型
var1 = 10
print(type(var1))
var1 = 1.1
print(type(var1))
var1 = "Lyx3ZzSs"
print(type(var1))

# 在运算的时候，数据类型会向高精度转换，float的精度高于int
var2 = 10
var3 = 1.2
var4 = var2 + var3
print("var4=", var4, "var4的类型：", type(var4))
var2 = var2 + 0.1
print("var2=", var2, "var2的类型：", type(var2))
