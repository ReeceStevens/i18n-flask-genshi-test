import gettext

from flask import Flask, g, request
from flaskext.genshi import Genshi, render_template, render_response
from flask.ext.babel import Babel
from genshi.filters import Translator
from genshi.template import MarkupTemplate

translations = gettext.translation('messages', 'localedir')

app = Flask(__name__, static_url_path='')
babel = Babel(app)
genshi = Genshi(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'es'])

@app.route("/")
def endpoint():
    template = MarkupTemplate(render_template('index.html'))
    translator = Translator(translations)
    translator.setup(template)
    return app.make_response(template.generate().render())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
