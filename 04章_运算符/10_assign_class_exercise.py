"""
@Author: yuanxin.Li
@Time：2025/10/2 14:25
@Version: 1.0
@Description:
"""
# 有两个变量, a和b, 要求将其进行交换, 动动脑筋, 要求不使用前面两种方式完成
a = 1
b = 2
print(f"交换前a = {a} b = {b}")
a = a + b
b = a - b
a = a - b
print(f"交换后a = {a} b = {b}")
