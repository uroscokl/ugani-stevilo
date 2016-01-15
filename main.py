#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2


def ugani(num):

    if num == 42:
        return 1
    elif num >= 50:
        return 2
    elif (num >= 31 and num <= 40) or (num >= 44 and num <= 49):
        return 3
    elif num == 43 or num == 41:
        return 4
    elif num <= 30:
        return 5


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("ugani.html")

    def post(self):
        numX = int(self.request.get("stX"))
        resitev = ugani(numX)

        if resitev == 1:
            return self.render_template("bravo.html")

        params = {"rezultat":resitev}
        return self.render_template("ugani.html", params)

class BravoHandler(BaseHandler):
    def get(self):
        return self.render_template("bravo.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/bravo', BravoHandler),
], debug=True)

