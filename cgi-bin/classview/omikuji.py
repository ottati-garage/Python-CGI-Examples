#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import BaseView, Request
import random


class OmikujiView(BaseView):
    sushi_list = ['はまち', 'まぐろ', 'さば', 'さーもん', 'いくら', 'ほたて', 'たい',
                  'えび', 'たこ', 'いくら']

    def get(self, request):
        sushi = random.choice((self.sushi_list))
        content = "<h1>すしランダム</h1><p>つ「%s」</p>" % sushi
        return self.generate_response(content)


if __name__ == "__main__":
    req = Request()
    print(OmikujiView().render(req))
