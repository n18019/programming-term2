import sys
menu = {
    'DripCoffee': 280,
    'ColdBrewCoffee': 320,
    'CafeLatte': 330,
    'SoyLatte': 380,
    'Cappuccino': 330,
    'CaramelFrappuccino': 470,
    'MacchaCreamFrappuccino': 470,
}

option = {
    'LowFatMilk': 0,
    'NonFatMilk': 0,
    'SoyMilk': 50,
    'DeepCoffee': 60,
    'WhipCream': 70,
    'CaramelShrup': 60,
    'ChocoSource': 0,
    'DeCafe': 50,
}
# 値を入れる空のリスト
menu_v = []
menu_f = []

while True:
    user_main = input('メインメニューを入力してください>>>')
    if user_main in menu.keys():
        menu_v.append(user_main)
        menu_f.append(menu[user_main])
        break
    elif user_main == 'q' or user_main == '':
        print('注文をキャンセルします')
        sys.exit()   # qとenterが押されれば強制終了
    else:
        print('存在しないメニューです。')

print('メインメニューを承りました。')

while True:
    user_option = input('オプションメニューを選んでください>>>')
    if user_option in option.keys():
        menu_v.append(user_option)
        menu_f.append(option[user_option])
        break
    elif user_option == 'q' or user_option == '':
        break
    else:
        print('存在しないメニューです')
        continue
# 表示内容を変えてループさせるために新しいループを作成
while True:
    user_option2 = input('他にオプションメニューの注文はございますか？>>>')
    if user_option2 in option.keys():
        menu_v.append(user_option2)
        menu_f.append(option[user_option2])
    elif user_option2 == 'q' or user_option2 == '':
        break
    else:
        print('存在しないメニューです')


# sum関数でappendで入れてきた値を足す
money = sum(menu_f)
print('注文内容は{}です'.format(menu_v))
print('合計金額は{}円です。右奥のカウンターでお待ちください'.format(money))
