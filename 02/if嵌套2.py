"""
@Author: yuanxin.Li
@Time：2025/2/15 22:04
@Version: 1.0
@Description:
"""
money = float(input("请输入公交卡余额："))
zuiwei = False
if money >= 2:
    print("欢迎乘坐110路公交车！")
    if zuiwei:
        print("车上有空座位，可以坐下。")
    else:
        print("车上暂时没有座位，请耐心等待！")
else:
    print("公交卡中余额不足，请及时充值！")
