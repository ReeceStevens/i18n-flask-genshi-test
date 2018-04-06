import gettext

from flask import Flask
from flaskext.genshi import Genshi
from genshi.filters import Translator
from genshi.template import MarkupTemplate

LANGUAGE_CONFIG_VAR = 'en'

translations = gettext.translation('messages', 'localedir', languages=[LANGUAGE_CONFIG_VAR])
_ = translations.gettext

app = Flask(__name__, static_url_path='')
genshi = Genshi(app)

@app.route("/")
def endpoint():
    with open('./templates/index.html') as tmpl_f:
        template = MarkupTemplate(tmpl_f)
    translator = Translator(translations)
    translator.setup(template)
    final_template_str = template.generate(fruit=_('apple'), locale=LANGUAGE_CONFIG_VAR).render()
    return app.make_response(final_template_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
