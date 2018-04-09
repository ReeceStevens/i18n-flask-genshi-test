# import gettext

from flask import Flask, request
from flask_babel import Babel, get_translations, get_locale, refresh, gettext
from flaskext.genshi import Genshi, render_response
from genshi.filters import Translator
from genshi.template import MarkupTemplate
from werkzeug import LocalProxy

LANGUAGE_CONFIG_VAR = 'es'

translations = LocalProxy(get_translations)
_ = gettext

app = Flask(__name__, static_url_path='')
genshi = Genshi(app)
babel = Babel(app)

@app.before_request
def refresh_locale():
    refresh()

@babel.localeselector
def select_locale():
    return LANGUAGE_CONFIG_VAR

@genshi.template_parsed
def translation(template):
    translator = Translator(translations)
    translator.setup(template)

@app.route("/")
def endpoint():
    return render_response('index.html', {'fruit': _('apple'), 'locale': LANGUAGE_CONFIG_VAR})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
