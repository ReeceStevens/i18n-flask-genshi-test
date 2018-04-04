# I18n Example

This is a proof-of-concept for performing i18n using GNU gettext-style `.po`
and `.mo` localization files. Localization needs to work for:

- Genshi templates (HTML documents with format strings)
- Python strings tagged with the `_()` symbol
- Javascript strings tagged with the `_()` symbol

To generate everything from scratch:

```bash
# Extract all translatable strings into .pot file
make messages.pot

# Generate language-specific .po files for translation
make po

# You will need to fill in the appropriate translations in the .po files.

# Compile translated .po files into machine-readable .mo files
make mo

# Run the server with the specified language setting
LANG={en,es} python server.py
```

To update the locale files after modifying code:

```bash
# Regenerate the .pot file
rm messages.pot; make messages.pot

# Update the .po files
make update_po

# Add any new translations

# Compile new files
make mo

# Run the server with the specified language setting
LANG={en,es} python server.py
```
