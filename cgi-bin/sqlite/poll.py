#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
import sqlite3

cgitb.enable()

# HTMLのテンプレート
TEMPLATE = """
<meta charset="shift-jis">
<form method="POST" action="">
<h1>好きな軽量言語は？ SQLite版</h1>
%s
<p><button type="submit">投票</button></p>
</form>
"""

# ラジオボタン用の部品 (HTML)
RADIO_TEMPLATE = """
<p><input type="radio" name="language" value="{language}">{language}<br>
{meter} {num}人</p>"""

con = sqlite3.connect('poll.sqlite3.dat')  # コネクションオブジェクト
cur = con.cursor()  # カーソルオブジェクト


def incrementvalue(cur, lang_name):
    """指定された言語のカウントをインクリメントする
    or 指定された言語がDBにない場合はあたらしく作る
    """
    # 言語を選択
    cur.execute("SELECT value FROM language_pole WHERE name='%s';" % lang_name)
    item = None
    for item in cur.fetchall():
        # インクリメントして更新
        cur.execute("UPDATE language_pole SET value=%d WHERE name='%s';" % (
            item[0] + 1, lang_name
        ))
    # データベースに更新したい言語のデータがない場合は新しく作成
    if item is None:
        cur.execute("INSERT INTO language_pole (name, value) VALUES('%s', 1);"
                    % lang_name)

# テーブル作成を試みる (DBファイルがない場合は自動的に作成)
try:
    cur.execute("CREATE TABLE language_pole (name text, value int);")
except sqlite3.OperationalError:
    pass  # すでに作成されていた

# データの更新
form = cgi.FieldStorage()
if 'language' in form:
    incrementvalue(cur, form['language'].value)

# データの読み込み
content = ""
lang_dic = {}
cur.execute("SELECT name, value FROM language_pole;")
for res in cur.fetchall():
    lang_dic[res[0]] = res[1]

# データベースの更新を反映
con.commit()

# HTML書き出し
for lang in ['Perl', 'PHP', 'Python', 'Ruby']:
    num = lang_dic.get(lang, 0)
    meter = "".join(["◆" for _ in range(num)])
    content += RADIO_TEMPLATE.format(language=lang, meter=meter, num=num)
header = "Content-type: text/html\n\n"
html = TEMPLATE % content
print(header + html)
