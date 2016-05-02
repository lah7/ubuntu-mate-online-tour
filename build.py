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

################################################################################
# Directory for deployment
root_dir = os.path.dirname(os.path.realpath(__file__))
build_dir = root_dir + '/build/'
print(col.SUCCESS + "======== Ubuntu MATE Guide Build Script ========")
print(col.INFO + "Source path: " + root_dir)
print(col.INFO + "Build path:  " + build_dir)

################################################################################
# Prepare build directory.
if os.path.exists(build_dir):
    print(col.INFO + "Previous build directory deleted.")
    shutil.rmtree(build_dir)
os.mkdir(build_dir)

################################################################################
# Load language configuration
try:
    lang_json = root_dir + '/translations/lang.json'
    with open(lang_json) as data_file:
        lang_data = json.load(data_file)
    lang_list = list(lang_data.keys())
    lang_list.sort()
except Exception as e:
    print(col.ERROR + 'ERROR: Failed to load lang.json!')
    print("       -- " + str(e))

################################################################################
# Copy and translate each HTML page from the base 'template'.
for lang in lang_list:
    code = lang_data[lang]['locale']
    language = lang_data[lang]['name']
    print(col.WARN + '\n-- Processing: ' + language + ' (' + code + ')')

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

################################################################################
# Copy source files
print(col.WARN + '\nCopying CSS files...')
shutil.copytree(root_dir + '/css/', build_dir + '/css/')

print(col.WARN + '\nCopying JS files...')
shutil.copytree(root_dir + '/js/', build_dir + '/js/')

print(col.WARN + '\nCopying IMG files...')
# FIXME: Does not omit .xcf source files.
shutil.copytree(root_dir + '/img/', build_dir + '/img/')

################################################################################
# Generate language selector screen
print(col.WARN + '\nGenerating Language Selection Screen...')
html_file = build_dir + '/index.html'
html_buffer = ''
# NOTE: This does not automatically generate the sprite sheet.

for lang in lang_list:
    locale = lang_data[lang]['locale']
    name = lang_data[lang]['name']
    help_text = lang_data[lang]['help'].replace("'", "&#8217;")
    # Sprite sheet position is determined by ID in lang.json
    pos = int(lang) * 16
    div = '<a href="/' + locale + '/" onmouseover="$(\'#lang-text\').html(\'' + help_text + '\')">' + \
          '<li class="lang-opt">'+ \
          '<div class="flag" style="background-position: -' + str(pos) + 'px 0px;"></div>' + \
          '&nbsp; ' + name + '</li></a>'
    html_buffer = html_buffer + div

shutil.copyfile(root_dir + '/html/lang-selector.html', build_dir + '/index.html')
with open(build_dir + '/index.html', 'r') as f:
    html_data = f.read()

html_data = html_data.replace('<!--LANGUAGE-LIST-PLACEHOLDER-->', html_buffer)
with open(build_dir + '/index.html', 'w') as f:
    f.write(html_data)

################################################################################
# Compress CSS
print(col.ERROR + 'fixme:compress-css')
print(col.ERROR + 'fixme:minify-page')
print(col.ERROR + 'fixme:strip-whitespace')
print(col.ERROR + 'fixme:strip-console-debug')
print(col.ERROR + 'fixme:strip-comments')

################################################################################
# Compress JS
print(col.ERROR + 'fixme:compress-js')
print(col.ERROR + 'fixme:minify-page')
print(col.ERROR + 'fixme:strip-whitespace')
print(col.ERROR + 'fixme:strip-console-debug')
print(col.ERROR + 'fixme:strip-comments')

################################################################################
# Compress images
print(col.ERROR + 'fixme:compress-img')
print(col.ERROR + 'fixme:minify-page')
print(col.ERROR + 'fixme:strip-whitespace')
print(col.ERROR + 'fixme:strip-console-debug')
print(col.ERROR + 'fixme:strip-comments')

################################################################################
# Build finished!
print(col.SUCCESS + '\n========================')
print('Build Complete!')
print('========================')
print(col.NORMAL)

################################################################################
