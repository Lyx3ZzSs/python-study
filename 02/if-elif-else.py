"""
@Author: yuanxin.Li
@Time：2025/2/15 20:21
@Version: 1.0
@Description:
if ***1：
    事情1
elif ***2：
    事情2
else ***3：
    事情3
"""
score = 77
if score >= 90 and score <= 100:
    print("本次考试，等级为A")
elif score >= 80 and score < 90:
    print("本次考试，等级为B")
elif score >= 70 and score < 80:
    print("本次考试，等级为C")
elif score >= 60 and score < 70:
    print("本次考试，等级为D")
elif score >= 0 and score < 60:
    print("本次考试，等级为E")
