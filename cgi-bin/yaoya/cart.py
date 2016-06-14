#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()  # デバッグモード


form = cgi.FieldStorage()
price = 300

num = int(form.getvalue('n', 0))
recipt_url = "/cgi-bin/yaoya/recipt.py?n={}".format(num)


# ヘッダ文字列の作成
header = "Content-type: text/html\n"


increment_url = '/cgi-bin/yaoya/cart.py?n={}'.format(num+1)
decrement_url = '/cgi-bin/yaoya/cart.py?n={}'.format(num-1)

# HTML文字列の作成
html = """
<meta charset="shift-jis">
<h1>カート</h1>
<div>
<p>
りんご {price}円: {num}個
<a href="{inc_url}">+</a>
<a href="{dec_url}">-</a>
</p>

<p>合計: {sum_price}円</p>
<p><a href="{recipt_url}">チェックアウト</a></p>
</div>
""".format(price=price, num=num, sum_price=num*price, recipt_url=recipt_url,
           dec_url=decrement_url, inc_url=increment_url)
print(header + html)
