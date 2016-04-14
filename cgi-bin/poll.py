#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from httphandler import PickleMixin, BaseView, Request
import cgitb


cgitb.enable()  # デバッグモード


# フォーム用テンプレート (HTML)
FORM_TEMPLATE = """
<form method="POST" action="">
<p>好きな軽量言語は？</p>
%s
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
    filepath = "./data/favorite_language.dat"

    def post(self, request):
        """投票されたときの処理
        """
        if 'language' in request.form:
            lang = request.form['language'].value
            self.obj[lang] = self.obj.get(lang, 0) + 1
            self.save_obj()

    def get_content(self, request):
        radios_html = ""
        for lang in ['Perl', 'PHP', 'Python', 'Ruby']:
            num = self.obj.get(lang, 0)
            meter = "".join(["◆" for _ in range(num)])
            radios_html += RADIO_TEMPLATE.format(language=lang, num=num, meter=meter)
        return FORM_TEMPLATE % radios_html

if __name__ == "__main__":
    req = Request()
    print(PollView().render(req))
