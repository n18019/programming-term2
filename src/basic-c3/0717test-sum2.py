# あるクラスの国語のテストの点数
points = [88, 76, 67, 43, 79, 80, 91]
sum_v = sum(points)  # sum()関数で合計を求める
ava_v = sum_v // len(points)
print("合計は", sum_v, "点")
print("平均は", ava_v, "点")
