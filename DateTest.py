import datetime

def date_test():
    now = datetime.datetime.now()
    print(now)
    print(now.year)  # 输出当前年份，如2025
    print(now.strftime("%A"))  # 输出当前星期的名称，如Sunday
    print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 输出示例: 2025-03-23 14:59:48
    #日期格式符号
    # %Y  完整年份  2025
    # %m  月份(01 - 12)  03
    # %d  日期(01 - 31)  23
    # %H  小时(24小时制)    14
    # %M  分钟      59
    # %S  秒数      48
    # %A  完整星期几   Sunday
    # %B  完整月份名称  March
    # %c  本地日期时间表示 Sun Mar 23 14:59:48 2025

    #新建日期
    special_date = datetime.datetime(2020, 5, 17)
    print(special_date)

if __name__ == '__main__':
    date_test()