from datetime import datetime, timedelta 

def process(target_date):
    """
    メインロジックを実行する
    Parameters
    ----------
    target_date : datetime
        処理対象の日付
    Returns
    -------
    list
        表示されるメッセージを要素に含むリスト
    """

    res_list = []   # 結果として返すリスト

    day_of_the_week = target_date.strftime("%a")
    reshape = target_date.strftime("%Y/%m/%d")
    if day_of_the_week == "Sat":
        res_list.append("{}は{}です。平日ではありません。".format(reshape, day_of_the_week))
        weekday = target_date + timedelta(days=2)
        weekday_fe = weekday.strftime('%Y/%m/%d')
        res_list.append("次の平日は{}です。".format(weekday_fe))
    elif day_of_the_week == "Sun":
        res_list.append("{}は{}です。平日ではありません。".format(reshape, day_of_the_week))
        weekday2 = target_date + timedelta(days=1)
        weekday2_fe = weekday2.strftime('%Y/%m/%d')
        res_list.append("次の平日は{}です。".format(weekday2_fe))
    else:
        res_list.append("{}は{}です。平日です。".format(reshape, day_of_the_week))

    return res_list

def display(msgs):
    """
    結果を表示する
    Parameters
    ----------
    msgs: list
        表示するメッセージが格納されたリスト
    Returns
    -------
    なし
    """
    print(*msgs, sep="\n")

# メイン処理
if __name__ == '__main__':
    while True:
        try:
            input_date = input('日付を入力してください。')
            target_date = datetime.strptime(input_date, '%Y/%m/%d')

            display(process(target_date))
            break
        except:
            print('入力された日付が不正です。再入力してください。')

