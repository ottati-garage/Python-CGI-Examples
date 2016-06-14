#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb


cgitb.enable()  # デバッグモード


def get_cost(pair, data):
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
pair = set([form['from'].value, form['to'].value])
num = int(form['n'].value)
cost = get_cost(pair, DATA) * num

# ヘッダ文字列の作成
header = "Content-type: text/html\n\n"

# HTML文字列の作成
html = """
<meta charset="shift-jis">
<h1>{}円</h1>
""".format(cost)
print(header + html)
