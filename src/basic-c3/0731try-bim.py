while True:
    try:
        weight = float(input('体重は？'))
        height = float(input('身長は？'))
        height = height / 100
        bmi = weight / (height * height)
        break;
    except:
        print('入力ミスがあります。再度にゅうりょくしてください')

result = ""
if bmi < 18.5:  result = '痩せ型'
elif bmi < 25:  result = '標準体重'
elif bmi < 30:  result = '肥満（軽）'
else:  result = '肥満（重）'

print('bmi :', bmi)
print('判定 :', result)
