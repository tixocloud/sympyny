#!/usr/bin/env python

import os
import yaml
import django

from shutil import rmtree, copytree
from django.template import Context
from django.template.loader import get_template

BUILD_DIR='build'
PACKAGE_DIR = os.path.join(BUILD_DIR, 'package')
TEMPLATE_DIR = ('templates',)
BASE_TEMPLATE='base.tmpl'
PAGES_DIR = 'pages'
DEFAULT_EXTENSION = '.html'

# Switch to the current working directory

# Attempt to figure out if there's a settings file

#exit(1)

# We should really merge builder into composer and provide it as an option
# Say composer.py -b new-site-name --> creates a new site
# Say composer.py -c --> builds the site

# Clean everything in build directory before building
# Remove package dir and zip file
if os.path.exists(PACKAGE_DIR):
    rmtree(PACKAGE_DIR)

# Initialization steps
django.conf.settings.configure(TEMPLATE_DIRS=TEMPLATE_DIR)

# Create a package folder
# Copy contents in htdocs
copytree('./htdocs', PACKAGE_DIR)

# Render the html pages from the yaml pages
for yaml_page in os.listdir(PAGES_DIR):
    file_contents = file(os.path.join(PAGES_DIR,yaml_page), 'r')
    content = yaml.load(file_contents)

    # At this point we can process the shpaml
    template = get_template(BASE_TEMPLATE) 
    page = template.render(Context(content))
    page = page.encode('UTF-8')


    # Save html file into package folder
    filename = os.path.splitext(yaml_page)[0]
    html_file = open(os.path.join(PACKAGE_DIR, filename + DEFAULT_EXTENSION),'w')
    html_file.write(page)
    html_file.close()

# Package it in a zip file 
