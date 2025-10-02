"""
@Author: yuanxin.Li
@Time：2025/10/2 13:31
@Version: 1.0
@Description:
"""
a = 9
b = 8
print(a > b)
print(a >= b)
print(a <= b)
print(a < b)
print(a == b)
print(a != b)

# 表示a>b比较的结果，赋给flag
flag = a > b
print("flag = ", flag)
print(a is b)
print(a is not b)

str1 = "abc#"
str2 = "abc#"

print("----------------")
print(str1 == str2)
print(str1 is str2)
