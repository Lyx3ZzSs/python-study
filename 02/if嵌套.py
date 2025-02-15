"""
@Author: yuanxin.Li
@Time：2025/2/15 21:51
@Version: 1.0
@Description:
"""
che_piao = 0  # 用1代表有车票，0代表没有车票
dao_length = 20  # 刀子的长度，单位cm
if che_piao == 1:
    print("有车票，可以进站")
    if dao_length < 10:
        print("通过安检")
        print("终于可以见到Ta了，美滋滋~~~")
    else:
        print("没有通过安检")
        print("刀子的长度超过规定，等待警察处理。。。")
else:
    print("没有车票，不能进站")
    print("亲爱的，那就下次见了")
