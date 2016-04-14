#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from httphandler import PickleMixin, BaseView, Request
import cgitb

cgitb.enable()  # デバッグモード


class CounterView(PickleMixin, BaseView):
    filepath = "counter.dat"

    def get(self, request):
        self.obj['count'] = self.obj.get('count', 0) + 1
        self.save_obj()

    def get_content(self, request):
        return "<p>Views: %s</p>" % self.obj.get('count', 0)


if __name__ == "__main__":
    req = Request()
    print(CounterView().render(req))
