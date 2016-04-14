#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# カウンターを保存するファイル
filepath = "f5.txt"

# params
char = "★"
levelup_rate = 0.2

# カウントを読み込む
try:
    f = open(filepath, 'r')
    level = int(f.read())
    if random.random() < levelup_rate:
        level += 1
except IOError:
    level = 1
else:
    f.close()

# カウントを保存する
with open(filepath, "w") as f:
    f.write(str(level))

# ヘッダ文字列の作成
header = "Content-type: text/html\n\n"

# HTML文字列の作成
html = """
<meta charset="shift-jis">
<body style="background:black">
<h1 style="color: #fff;">F5 Level: {level}</h1>
<span style="color: cyan; font-size:{level}px;">{char}</span>
</body>
""".format(level=level, char=char)
print(header + html)
