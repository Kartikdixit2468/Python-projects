from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """ This will servres the root or main index.html file to the server. """

    return render_template('index.html')

@app.route('/post')
def post():
    """ This will servres the post.html file to the server. """
    message = "Sorry, Nothing here right now...."

    return render_template('post.html', message=message)

@app.route('/downloads')
def downloads():
    """ This will servres the downloads.html file to the server. """

    return render_template('downloads.html')

app.run(debug=True)
