"""
@Author: yuanxin.Li
@Time：2025/2/11 17:49
@Version: 1.0
@Description:
"""
"""
格式话符号：
%s:格式话输出字符串
%d:格式化输出整数
%f:格式化输出浮点数
"""
# 需求：输出"今年我的年龄是18岁"
age = 18
name = "TOM"
weight = 75.5
student_id = 1

# 我的名字是TOM
print("我的名字是%s" % name)
print(f"我的名字是{name}")

# 我的序号是0001  %04d，表示输出的正式显示位数，不足以0补全，超出当前位数则原样输出
print("我的学号是%04d" % student_id)

# 我的体重是75.50公斤 %.2f，表示小数点后显示的小数位数
print("我的体重是%.2f" % weight)

# 我的名字是TOM，明年19岁了
print("我的名字是%s,明年%d岁了" % (name, age + 1))

print(f"我的名字是{name},明年{age + 1}岁了")

"""
    Python中，print()，默认自带end="\n"这个换行结束符，所以导致每两个print直接会换行展示，用户可以按需求更改结束符。
      转义字符：\n 换行
              \t 制表符，一个tab键的距离
"""
print("输出的内容", end="\n")
