# randomモジュールをimport
import random

# randomに表示させるリストを作る
a = ["晴れ", "曇り", "雨", "台風"]
s = ["歩き", "自転車", "車", "電車"]
n = ["昔なつかしの駄菓子", "アイス", "美味しいパン"]

# １つめの入る文言
a_x = random.randint(0, len(a)-1)

# ２つめの入る文言
s_x = random.randint(0, len(s)-1)

# ３つめの入る文言
n_x = random.randint(0, len(n)-1)

phrase = '''
あしたの天気は{}でしょう。
{}で通学すると良き👍
帰りに{}を買ってみても良いかもよん♪
'''

print(phrase.format(a[a_x], s[s_x], n[n_x]))
