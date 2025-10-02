"""
@Author: yuanxin.Li
@Time：2025/10/2 13:23
@Version: 1.0
@Description:
"""
# 假如还有97天放假，问：合多少个星期零多少天

days = 97
week = days // 7
left_day = 97 % 7
print(f"假如还有{days}天放假，则：合{week}个星期零{left_day}天")

# 定义一个变量保存华氏温度，华氏温度转换摄氏温度的公式为: 5/9*(华氏温度-100),
# 请求出华氏温度对应的摄氏温度。[234.5]
hua_shi = 234.5
she_shi = 5 / 9 * (hua_shi - 100)
print(f"华氏温度{hua_shi} 对应的摄氏温度 {she_shi}")
print("华氏温度 %.2f 对应的摄氏温度 %.2f" % (hua_shi, she_shi))
