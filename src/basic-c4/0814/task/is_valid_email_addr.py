import re

n = input("メールアドレスを入力してください＞＞")
rep = '^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
if re.search(rep, n):
    print(n, "はメールアドレス形式です")
else:
    print(n, "はメールアドレス形式ではありません")
