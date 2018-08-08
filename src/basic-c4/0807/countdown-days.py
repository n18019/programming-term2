import datetime
t1 = datetime.date(2020, 7, 24)
t2 = datetime.date.today()
diff = t1 - t2
print("今日:", t2.strftime("%Y/%m/%d"))
print("あと", diff.days, "日")
