import re

n = input("電話番号を入力してください＞＞")
pattern = r'[\(]{0,1}[0-9]{2,4}[\)\-\(]{0,1}[0-9]{2,4}[\)\-]{0,1}[0-9]{3,4}'
if re.findall(pattern, n):
    print(n, "は電話番号の形式です")
else:
    print(n, "は電話番号の形式ではありません")
