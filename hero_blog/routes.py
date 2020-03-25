from hero_blog.models import User, Post
from flask import render_template, url_for, flash, redirect
from hero_blog.forms import RegistrationForm, LoginForm
from hero_blog import app

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
