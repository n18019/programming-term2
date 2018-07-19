
arithmetic = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
        }

print('四則計算プログラムです')
while True:
    try:
        user_word = float(input('第１パラメーターを入力してくだい>>>'))
    except ValueError:   # 数値が入らなければエラー表示されループが回る
        print('エラーです。再度入力してください')
        continue
    else:
        break

while True:
    try:
        user_word2 = float(input('第２パラメーターを入力してくだい>>>'))
    except ValueError:
        print('エラーです。再度入力してください')
        continue
    else:
        break

while True:
    arithmetic_word = input('演算方法を入力してください>>>')
    if arithmetic_word in arithmetic.keys():
        break
    else:
        print('エラーです。再度入力してください')

# arithmetic_wordが文字列としてしか認識されないためifで条件を指定し計算
if arithmetic_word == '+':
    result = user_word + user_word2
elif arithmetic_word == '-':
    result = user_word - user_word2
elif arithmetic_word == '*':
    result = user_word * user_word2
elif arithmetic_word == '/':
    result = user_word / user_word2

# 小数点第３位まで丸める
result = round(result, 3)
print('結果は{}です'.format(result))
