// A script for converting .po files into dictionary lookups

var gettextParser = require("gettext-parser")
var fs = require('fs')

var locale = process.argv[2]
var po_path = `localedir/${locale}/LC_MESSAGES/messages.po`
var output_path = `static/i18n_${locale}.js`

var in_file = fs.readFileSync(po_path)
var po_file = gettextParser.po.parse(in_file);

var translations = po_file.translations['']
var i18n_function = `
    var translations = ${JSON.stringify(translations)}
    _ = function (string) {
        return translations[string]['msgstr']
    }
`
fs.writeFileSync(output_path, i18n_function)
console.log(translations['apple'].msgstr)
