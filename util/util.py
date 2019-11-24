import datetime


def getReturnTime(startTime):
    year, month, day = [i for i in startTime.split('-')]  # 根据空格，将值读出
    time = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(days=30)
    return time.isoformat()