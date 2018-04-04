LOCALEDIR := ./localedir
BABEL_CONFIG := ./settings.cfg

messages.pot: $(BABEL_CONFIG)
	pybabel extract -F $< -o $@ .

po_files: messages.pot
	pybabel init -i $< -d $(LOCALEDIR) -l es

mo_files:
	pybabel compile -d $(LOCALEDIR)

update_po_files: messages.pot
	pybabel update -i $< -d $(LOCALEDIR)
