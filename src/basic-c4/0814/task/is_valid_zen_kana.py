import re

n = input("全角カナの文字を入力してください＞＞")
patten = re.compile(r"[\u30A1-\u30F4]+")
if patten.fullmatch(n):
    print(n, "は全角カナのみの文字列です")
else:
    print(n, "に全角カナ以外が含まれています")
