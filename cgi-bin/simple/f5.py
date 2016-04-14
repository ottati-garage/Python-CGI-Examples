#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = "f5.txt"  # カウンターを保存するファイル
char = "★"  # params

# カウントを読み込む
try:
    f = open(filepath, 'r')
    c = int(f.read()) + 1
except IOError:
    c = 1
else:
    f.close()

# カウントを保存する
with open(filepath, "w") as f:
    f.write(str(c))

# ヘッダ文字列の作成
header = "Content-type: text/html\n\n"

# HTML文字列の作成
html = """
<meta charset="shift-jis">
<body style="background:black">
<h1 style="color: #fff;">Views: {count}</h1>
<span style="color: cyan; font-size:{count}px;">{char}</span>
</body>
""".format(count=c, char=char)
print(header + html)
