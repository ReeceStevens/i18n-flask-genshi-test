import gettext

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
