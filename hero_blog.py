from flask import Flask, render_template, url_for 
app = Flask(__name__)

posts = [
    {
        'author': 'Deku',
        'title': 'I forgot the cake',
        'content': 'No seriously, I have no cake.',
        'date_posted': 'April 19, 2019'
    },
        {
        'author': 'Bakugo',
        'title': 'Shut up',
        'content': 'Shut up Deku!',
        'date_posted': 'April 20, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)