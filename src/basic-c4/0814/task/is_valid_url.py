import re

n = input("URLを入力してください＞＞")

if re.match(r"^https?:\/\/", n):
    print(n, "はURLの形式です")
else:
    print(n, "はURLの形式ではありません")
