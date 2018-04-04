LOCALEDIR := ./localedir
BABEL_CONFIG := ./settings.cfg

messages.pot: $(BABEL_CONFIG)
	pybabel extract -F $< -o $@ .

po: messages.pot
	pybabel init -i $< -d $(LOCALEDIR) -l es

mo:
	pybabel compile -d $(LOCALEDIR)

update_po: messages.pot
	pybabel update -i $< -d $(LOCALEDIR)
