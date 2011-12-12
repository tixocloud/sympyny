#!/usr/bin/env python

# This file creates the structure for a new site
# Depends on Python 2.7

import argparse
import os
from shutil import copytree

# Get the sitename and the default build directory if there is one
# Default build directory is set to current directory
parser = argparse.ArgumentParser(description='Generate directory structure of a new site.')
parser.add_argument('sitename', 
    help='Name of the site you\'re creating. This will be used as the directory name.')
parser.add_argument('-b', default='.',
    help='Directory to create your site. Defaults to current working directory.')
args = parser.parse_args()

SITENAME = args.sitename.lower()
BUILD_DIR = args.b
WORKING_DIR = os.path.join(BUILD_DIR, SITENAME)
BASESITE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'basesite')

# Need to verify if site already exists and if not, die
if os.path.exists(WORKING_DIR):
    print 'Site \'{}\' already exists'.format(SITENAME) 
    exit(1)

# Create new site and copy contents from base site
print "Creating new site \'{}\' ... ".format(SITENAME)
copytree(BASESITE_DIR, WORKING_DIR)
