#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http import PickleMixin, BaseView, Request
import cgitb


cgitb.enable()  # デバッグモード


# フォーム用テンプレート (HTML)
FORM_TEMPLATE = """
<form method="POST" action="">
<p>好きな軽量言語は？</p>
{}
<p><button type="submit">投票</button></p>
</form>
"""

# ラジオボタン用の部品 (HTML)
RADIO_TEMPLATE = """
<p>
<input type="radio" name="language" value="{language}">
{language}<br>
{meter} {num}人
</p>
"""


class PollView(PickleMixin, BaseView):
    filepath = "favorite_language.dat"

    def get(self, request):
        radios_html = ""
        for lang in ['Perl', 'PHP', 'Python', 'Ruby']:
            num = self.obj.get(lang, 0)
            meter = "".join(["◆" for _ in range(num)])
            radios_html += RADIO_TEMPLATE.format(language=lang, num=num,
                                                 meter=meter)
        content = FORM_TEMPLATE.format(radios_html)
        return self.generate_response(content)

    def post(self, request):
        """投票されたときの処理
        """
        if 'language' in request.form:
            lang = request.form['language'].value
            self.obj[lang] = self.obj.get(lang, 0) + 1
            self.save_obj()
        content = '<h1>ありがとうございました！</h1>'
        content += '<a href="/cgi-bin/classview/poll.py">＜＜ 投票画面に戻る</a>'
        return self.generate_response(content)


if __name__ == "__main__":
    req = Request()
    print(PollView().render(req))
