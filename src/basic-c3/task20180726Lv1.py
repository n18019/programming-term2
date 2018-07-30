import random
import sys
goal = 20
# ランダムに入ってきた整数
cur_x = []

print('ゴールは２０です！')
def shake_dice():
    '''
    ランダムなサイコロを振る関数

    parameters
    ----------
    なし

    Return
    ------
    random.randint(1, 6)
    １から６までのランダムな整数
    '''
    return random.randint(1, 6)
help(shake_dice)

def go_forward(Advance_forward):
    '''
    リストを合計する
    parameters
    ----------
    Advance_forward : リスト[]
    リスト名を入れる

    Return
    ------
    sum関数で合計した値
    '''
    return sum(Advance_forward)

help(go_forward)
while True:
    user = input('サイコロをふってください')
    if user == '':
        s = shake_dice()
        cur_x.append(s)
        if go_forward(cur_x) >= goal:
            print('{}がでました。おめでとうございます、ゴールです！'.format(s))
            sys.exit()
        else:
            print('{}がでました。現在位置は{}です。'.format(s, go_forward(cur_x)))
    else:
        print('サイコロを振るにはenterキーを押してください')

