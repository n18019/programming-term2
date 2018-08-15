import re

n = input("テキスト形式のファイル名を入力してください＞＞")
patten = r"\.txt$"
if re.search(patten, n):
    print(n, "は拡張子が.txtのテキストファイルです")
else:
    print(n, "は拡張子が.txtのテキストファイルではありません")
