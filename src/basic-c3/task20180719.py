
arithmetic = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
        }

# 計算方法を関数に
def mul(a, b):
    '''
    掛け算を行う

    Parameters
    ----------
    a: float
    b: float

    Returns
    -------
    aとbをかけた値
    '''
    return a * b

def sub(a, b):
    '''
    引き算を行う

    Parameters
    ----------
    a: float
    b: float

    Returns
    -------
    aとbを引いた値
    '''
    return a - b

def add(a, b):
    '''
    足し算を行う

    Parameters
    ----------
    a: float
    b: float

    Returns
    -------
    aとbを足した値
    '''
    return a + b

def div(a, b):
    '''
    割り算を行う

    Parameters
    ----------
    a: float
    b: float

    Returns
    -------
    aとbを割った値
    '''
    return a / b

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

# 入力された値を作った関数で計算
if arithmetic_word == '+':
    result = add(user_word, user_word2)
elif arithmetic_word == '-':
    result = sub(user_word, user_word2)
elif arithmetic_word == '*':
    result = mul(user_word, user_word2)
elif arithmetic_word == '/':
    result = div(user_word, user_word2)

# 小数点第３位まで丸める
result = round(result, 3)
print('結果は{}です'.format(result))
