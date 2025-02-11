"""
@Author: yuanxin.Li
@Time：2025/2/11 19:27
@Version: 1.0
@Description:
"""

"""
算数运算符
+ 加
- 减
* 乘
/ 除
// 整除
% 取余
** 指数
() 小括号
"""
num1 = 1 + 1
num2 = 1 - 1
num3 = 2 * 2
num4 = 10 / 2
num5 = 9 // 4
num6 = 9 % 4
num7 = 2 ** 3

# 赋值运算符
# 单个变量赋值
num = 1
print(num)
# 多个变量赋值
num_a, float_a, str_a = 10, 0.5, "hello world"
print(num_a)
print(float_a)
print(str_a)

# 多变量赋相同值
a = b = 10
print(a)
print(b)

"""
复合赋值运算符
+=  加法赋值运算符 c += a 等于 c = c + a
-=  减法赋值运算符 c -= a 等于 c = c - a
*=  乘法赋值运算符 c *= a 等于 c = c * a
/=  除法赋值运算符 c /= a 等于 c = c / a
//= 整除赋值运算符 c //= a 等于 c = c // a
%=  取余赋值运算符 c %= a 等于 c = c % a
**= 幂赋值运算符   c **= a 等于 c = c ** a
"""
a = 100
a += 1
print(a)

b = 2
b *= 3
print(b)

c = 10
c += 1 + 2
print(c)

"""
比较运算符
==
!=
>
<
>=
<=   
"""
d = 7
e = 9
print(d == e)
print(d != e)
print(d > e)
print(d < e)
print(d >= e)
print(d <= e)

"""
逻辑运算符
and
or
not
"""
r = 1
t = 2
y = 3
print(r < t) and (t < y)
print(r > t) and (t > y)
print(r > t) or (t < y)
print(not (a > b))
