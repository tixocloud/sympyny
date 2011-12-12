Sympyny - HTML site generator
=======

Sympyny is a HTML site generator that uses Django for templating and yaml
for content.

This allows you to maintain your content separately from your template
design and allows you to apply optimizations such as JS combination,
JS optimization, CSS combination, CSS minification and etc.





Need a auto-generate sites script
1. Create a site directory
2. Auto-generate files inside the site directory
    - dir build
    - dir templates
        - header
        - footer
    - dir pages
    - dir css
    - dir js
    - file builder script (compose.py)
    - settings file?
3. compose.py script
    - takes the templates
    - renders the pages
    - copies the css and js directories


File structure in build
- js
- css
- images
- *.html
- *.* (contents of htdocs)
