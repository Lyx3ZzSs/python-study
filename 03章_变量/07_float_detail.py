"""
@Author: yuanxin.Li
@Time：2025/6/7 21:38
@Version: 1.0
@Description:
"""
f1 = 4.5
f2 = -3.6
print("f1=", f1)
print("f2=", f2)

# 浮点类型的表示形式
f3 = 5.12
n4 = .512
print("n4 = ", n4)

# 科学计数法形式:如:5.12e2，5.12E-2
f5 = 5.12e2  # 5.12乘以10的2次方
f6 = 5.12E-2  # 5.12除以10的2次方
print("f5 = ", f5)
print("f6 = ", f6)

# 浮点类型计算后，存在精度的损失，可以使用Decimal类型进行精确计算
# 如何解决
# 1.为了避免浮点数的精度问题，可以使用Decimal类进行精确计算
# 2.如果使用Decimal类，需要导入Decimal类

# 导入Decimal类
from decimal import Decimal

# b = 8.1 / 3 # 2.6999999999999997
b = Decimal("8.1") / Decimal("3")
print("b = ", b)
