"""
@Author: yuanxin.Li
@Time：2025/2/11 18:18
@Version: 1.0

输入功能：input("提示文字")
输入的特点：
    一般将input接收的数据存储到变量
    input接收的任何数据默认都是字符串数据类型
"""
password = input("请输入您的密码")
print(f"您输入的密码是{password}")
print(type(password))
