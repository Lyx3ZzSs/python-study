"""
@Author: yuanxin.Li
@Time：2025/10/2 14:52
@Version: 1.0
@Description:
"""
# 请使用前面讲的 if-else方式, 得到3个数的最大值
a = 30
b = 40
c = 50
max1 = a if a > b else b
max2 = max1 if max1 > c else c
print("max2=", max2)
