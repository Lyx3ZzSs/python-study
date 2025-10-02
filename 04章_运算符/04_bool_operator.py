"""
@Author: yuanxin.Li
@Time：2025/10/2 13:38
@Version: 1.0
@Description:
"""
# and x and y 布尔“与” ： 如果x为False，x and y 返回x的值，否则返回y的计算值。（a and b）返回20
# or x or y 布尔“或”：如果x是True，它返回x的值，否则它返回y的计算值。（a or b）返回 10
# not not x 布尔“非”：如果x 为True，返回False。如果x为False，它返回True。not （a and b）返回False
a = 10
b = 20
print(a and b)  # a 为false 返回a，否则返回b
print(a or b)  # a 为 True 返回a，否则返回b
print(not (a and b))  # F
