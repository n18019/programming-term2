import tkinter.messagebox as mb
ans = mb.askyesno("質問", "そばはすきですか？")
if ans == True:
    mb.showinfo("同意", "うちもすきです")
else:
    mb.showinfo("本当？", "おいしいのになぁ")
