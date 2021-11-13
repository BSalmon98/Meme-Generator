# Meme Generator Python Project

Meme Generator is a tool that allows users to create both user 
defined and random memes through the python terminal or via a 
Flask application on the web.

This project was undertaken to test a students understanding of 
interconnected systems in python and appropriate use of standard
library modules.

## Prerequisites

- At least python3
- A Windows/Mac/Linux machine
- requirements.txt has been installed on machine

##Using Meme Generator

Meme Generator can be used either from the command line or as
a Flask web application.

The command line takes a path to a local directory, the body 
of a quote and the author of the quote: 

```bash
python<version> meme.py --path <specified path>
                        --body <A quote body>
                        --author <A quote author>
```
If no path, body or author is selected they will be chosen randomly
from _data files.

The Flask app is started by running:

```bash
python<version> app.py
```

The app can either generate random memes using the same method 
as the command line method or allows the user to input a url
of an image and input a body and author of a quote.
In both cases the app displays the image within the webpage of
the app.