#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http import PickleMixin, BaseView, Request
import cgitb

cgitb.enable()  # デバッグモード


class CounterView(PickleMixin, BaseView):
    filepath = "counter.dat"

    def get(self, request):
        self.obj['count'] = self.obj.get('count', 0) + 1
        self.save_obj()
        content = "<p>Views: %s</p>" % self.obj.get('count', 0)
        return self.generate_response(content)


if __name__ == "__main__":
    req = Request()
    print(CounterView().render(req))
