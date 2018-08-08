import tkinter.filedialog as fd

path = fd.askopenfilename(
title="処理対象のファイルをしていください",
filetypes=[('HTML','html')])
print(path)
