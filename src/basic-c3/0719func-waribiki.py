# スーパーの割引計算

def calcvalue(who, hour, count, value):
    '''
    割引計算をする

    parameters
    ----------
    who:
    hour:
    count:
    value:

    Returns
    なし
    '''

    info = '割引なし'
    # １４時に商品を３つ以上で１割引
    if (hour == 14) and (count >= 3):
        value *= 0.9
        info = '１割引'
    # １５時に商品を５つ以上で２割引
    elif (hour == 15) and (count >= 5):
        value *= 0.8
        info = '２割引'

    # 結果を表示
    value = int(value)
    print('{}さんは{}={}円'.format(who, info, value))

calcvalue('A', 15, 3, 1200)
calcvalue('B', 14, 4, 2000)
calcvalue('C', 15, 8, 5400)
