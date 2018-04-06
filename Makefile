LOCALEDIR := ./localedir
BABEL_CONFIG := ./settings.cfg

messages.pot: $(BABEL_CONFIG)
	pybabel extract -F $< -o $@ .

po: messages.pot
	pybabel init -i $< -d $(LOCALEDIR) -l es
	pybabel init -i $< -d $(LOCALEDIR) -l en
	node parse_po_files.js es
	node parse_po_files.js en

mo:
	pybabel compile -d $(LOCALEDIR)

update_po: messages.pot
	pybabel update -i $< -d $(LOCALEDIR)
	node parse_po_files.js es
	node parse_po_files.js en
