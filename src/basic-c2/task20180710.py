# 勝ってしまうプログラム
# じゃんけんを変数に
a = "グー"
b = "チョキ"
c = "パー"
print("じゃーんけーん")
print("a=グー b=チョキ c=パー aかbかcを入力")

# 入力値が入る変数
user = input('>>> ')

if user == "a":
    print(c)
    print("CPUがパーを出しました。あなたの負けです。")
elif user == "b":
    print(a)
    print("CPUがグーを出しました。あなたの負けです。")
elif user == "c":
    print(b)
    print("CPUがチョキを出しました。あなたの負けです。")
else:
    print("入力が不正です。終了します。")
