import gettext
import os
import re

from flask import Flask, g, request
from flaskext.genshi import Genshi, render_template, render_response
from flask_babel import Babel
from genshi.filters import Translator
from genshi.template import MarkupTemplate

translations = gettext.translation('messages', 'localedir')
_ = translations.gettext

app = Flask(__name__, static_url_path='')
babel = Babel(app)
genshi = Genshi(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['es', 'en'])

@app.route("/<path>")
def static_endpoint(path):
    full_static_path = os.path.join("static", path)
    with open(full_static_path) as static_file:
        static_str = static_file.read()
    gettext_pattern = re.compile(r'_\("(.*?)"\)')
    translation_dict = {translatable_str: _(translatable_str)
                        for translatable_str in gettext_pattern.findall(static_str)}
    for key in translation_dict:
        static_str = static_str.replace(key, translation_dict[key])
    return app.make_response(static_str)

@app.route("/")
def endpoint():
    with open('./templates/index.html') as tmpl_f:
        template = MarkupTemplate(tmpl_f)
    translator = Translator(translations)
    translator.setup(template)
    final_template_str = template.generate(fruit=_('apple')).render()
    print("{!r}".format(final_template_str))
    return app.make_response(final_template_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
