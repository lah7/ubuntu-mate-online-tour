#!/usr/bin/python3

import os
import sys
import json
import shutil

class col:
    SUCCESS = '\033[92m'
    WARN =    '\033[93m'
    ERROR =   '\033[91m'
    INFO =    '\033[94m'
    NORMAL =  '\033[0m'

# Directory for deployment
root_dir = os.path.dirname(os.path.realpath(__file__))
build_dir = root_dir + '/build/'
print(col.SUCCESS + "======== Ubuntu MATE Guide Build Script ========")
print(col.INFO + "Build path: " + build_dir)

# Prepare build directory.
if os.path.exists(build_dir):
    print(col.INFO + "Previous build directory deleted.")
    shutil.rmtree(build_dir)
os.mkdir(build_dir)

# Load language configuration
try:
    lang_json = root_dir + '/translations/lang.json'
    with open(lang_json) as data_file:
        lang_data = json.load(data_file)
except Exception as e:
    print(col.DANGER + 'ERROR: Failed to load lang.json!')
    print("       -- " + str(e))

# Generate each part of the website
for lang in lang_data:
    code = lang_data[lang]['code']
    language = lang_data[lang]['string']
    print(col.WARN + '-- Processing: ' + language + ' (' + code + ')')

    # Generate translated index pages
    print(col.ERROR + 'fixme:copy-base-page')
    print(col.ERROR + 'fixme:translate-index-pages')

    # Strip page
    #   -- Del: whitespace, debugging, comments
    print(col.ERROR + 'fixme:strip-whitespace')
    print(col.ERROR + 'fixme:strip-console-debug')
    print(col.ERROR + 'fixme:strip-comments')

    # Minify/Compress page
    print(col.ERROR + 'fixme:minify-page')

# Generate language selector screen
print(col.ERROR + 'fixme:geneate-lang-page')

# Copy and compress CSS
os.mkdir(build_dir + '/css')
print(col.ERROR + 'fixme:copy-css')
print(col.ERROR + 'fixme:compress-css')

# Copy and compress JS
os.mkdir(build_dir + '/js')
print(col.ERROR + 'fixme:copy-js')
print(col.ERROR + 'fixme:compress-js')

# Copy images
os.mkdir(build_dir + '/img')
print(col.ERROR + 'fixme:copy-img')
print(col.ERROR + 'fixme:compress-img')

# Build finished!
print(col.SUCCESS + '\n========================')
print('Build Complete!')
print('========================')
print(col.NORMAL)
