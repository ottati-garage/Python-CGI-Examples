#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb


cgitb.enable()  # デバッグモード


def get_cost(pair, data):
    if len(pair) == 1:
        return 0
    for d in data:
        if d['pair'] == pair:
            return d['cost']
    return 0


DATA = [
    {'pair': set(['Shinjuku', 'Nakano']), 'cost': 154},
    {'pair': set(['Shinjuku', 'Mitaka']), 'cost': 216},
    {'pair': set(['Mitaka', 'Nakano']), 'cost': 165},
]


form = cgi.FieldStorage()
from_ = form.getvalue('from', 'Shinjuku')
to = form.getvalue('to', 'Nakano')
pair = set([from_, to])
num = int(form.getvalue('n', 1))
cost = get_cost(pair, DATA) * num


# ヘッダ文字列の作成
header = "Content-type: text/html\n\n"

# HTML文字列の作成
html = """
<meta charset="shift-jis">
<h1>{cost}円</h1>

<form method="GET" action="">
出発: <input type="text" name="from" value="{from_}">
<br>
到着: <input type="text" name="to" value="{to}">
<br>
人数: <input type="number" name="n" value="{num}">
<p><input type="submit"></p>
</form>

""".format(cost=cost, from_=from_, to=to, num=num)
print(header + html)
