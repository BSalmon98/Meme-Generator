import random
import os
import requests
from flask import Flask, render_template, abort, request, url_for

from QuoteEngine import Ingestor
from MemeEngine import ImageHandler as make_meme

app = Flask(__name__)


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        file_quotes = Ingestor.parse(file)
        for quote in file_quotes:
            quotes.append(quote)

    images_path = "./_data/photos/dog/"
    imgs = []
    for path in os.listdir(images_path):
        imgs.append(os.path.join(images_path, path))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = make_meme.process_image(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    try:
        r = requests.get(url)
        img = open('./tmp.jpg', 'wb')
        img.write(r.content)

        path = make_meme.process_image('./tmp.jpg', body, author)
        img.close()
        os.remove('./tmp.jpg')
        return render_template('meme.html', path=path)
    except:
        print("Invalid file type entered")
        return render_template('meme_error.html')




if __name__ == "__main__":
    app.run()

