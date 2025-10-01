"""
@Author: yuanxin.Li
@Time：2025/10/1 15:47
@Version: 1.0
@Description:
"""
# 显示类型转换注意事项

# 不管什么值的int，float都可以转换成str，str(x)将对象x转换为字符串
n1 = 100
n2 = 123.65
print(str(n1))
print(str(n2))

# int转换成float时，会增加小数部分，比如123->123.0，
# float转换成int时，会去掉小数部分，比如123.65 -> 123

print(float(n1))
print(int(n2))

# str转int，float使用int（x),float（x)将对象x转换为int/float
n3 = "12.3"
print(float(n3))
# print(int(n3))

# 在将str类型转换成基本数据类型时，要确保str值能够转成有效的数据，比如 我们可以把"123"，转成一个整数，但是不能把“hello” 转换成一个整数，
# 如果格式不正确，程序会报ValueError，程序就会终止
n4 = "hello"
# print(float(n4))
# print(int(n4))

i = 10
j = float(i)
print("i的值：", i, "i的类型：", type(i))  # 10,int
print("j的值：", j, "j的类型：", type(j))  # 10.0,float

k = str(i)
print("i的值：", i, "i的类型：", type(i))  # 10,int
print("k的值：", k, "k的类型：", type(k))  # "10",str
