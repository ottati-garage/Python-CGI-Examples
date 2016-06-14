#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb


cgitb.enable()  # デバッグモード


form = cgi.FieldStorage()
price = 300
num = int(form.getvalue('n', 0))

# ヘッダ文字列の作成
header = "Content-type: text/html\n"

# HTML文字列の作成
html = """
<meta charset="shift-jis">
<h1>カート</h1>
<p>りんご {price}円: {num}個</p>
<p>合計: {sum_price}円</p>
<p>Thank you!</p>
""".format(price=price, num=num, sum_price=num*price)
print(header + html)
