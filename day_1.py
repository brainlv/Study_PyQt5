temp = input("请输入今天气温（单位 摄氏度）:")
pa = input("请输入今天气压（单位 帕）:")

temp = float(temp)
pa = int(pa)


def feel(x, y):
    if (x > 30 or x < -8) and (y > 300 or y < 20):
        print("不舒适")
    elif 25 < x <= 30 and 200 < y <= 300:
        print("比较舒适")
    elif 10 < x <= 25 and 100 < y <= 200:
        print("特别舒适")
    elif -8 < x <= 10 and 20 <= y <= 100:
        print("比较舒适")
    else:
        print("本程序不能判断")
    return 0


feel(temp, pa)
