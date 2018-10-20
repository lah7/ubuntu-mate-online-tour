# Ubuntu MATE Guide

An interactive tour, demo and guide for the
[Ubuntu MATE](http://ubuntu-mate.org)
operating system inside a modern web browser.

Originally based on the [Ubuntu Online Tour](https://launchpad.net/ubuntu-online-tour).

**ABANDONED: This project was an experiment for Ubuntu MATE, but has been discontinued.**

### Objectives:

* Ensure new users are familiar before their first boot.
* Deliver a visually stunning experience very close to the live environment.
* Provide interactive documentation and walkthroughs for common questions.
* Readable in multiple languages so anyone around the world can get started.


### Supported Browsers:

* Firefox
* Chromium / Chrome


*More browsers may be more thoroughly tested in future.*


## Testing

First, build the project to compile and optimise the assets.

    build.py

Host `build/` on a web server, Python includes a simple one:

    python -m SimpleHTTPServer 8000

And visiting <http://localhost:8000/en/>.


## Multilingual

You can use the translation script to generate translated versions of the tour.

First, install [python polib](https://pypi.python.org/pypi/polib)
(`sudo apt install python-polib` on Ubuntu), then run:

    translate-html/bin/translate-html -t


This will generate translated versions of the `index/` folder for each available language.

For further help using the translator, run `translate-html/bin/translate-html --help`.


## Compress the site files

To ensure the Online Tour has optimal download page weight
and in-browser performance, the tour is optimised on publishing, using `gulp`:

``` bash
npm install           # First install required node modules
gulp compress-html    # Minify HTML and bundle in optimised CSS and JS. NB: compresses HTML in-place
gulp compress-images  # Optimise image files to make them smaller
```


## Dependencies

 * gulp
 * gulp-htmlmin
 * gulp-imagemin
 * gulp-inline-source
 * imagemin-pngquant


