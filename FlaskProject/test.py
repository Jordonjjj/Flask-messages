from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c89b5bf9629570437770d0ea5caf6891f5bf54f1a9391e2f'
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]
connection = sqlite3.connect("messages.db", check_same_thread=False)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages (title TEXT, content TEXT)")


@app.route('/')
def index():
    messagesDB = cursor.execute("SELECT title, content from messages").fetchall()
    print(messagesDB)
    return render_template('index.html', messages=messagesDB)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Content.is required')
        elif not content:
            flash('Content.is required')
        else:
            messages.append({'title': title, 'content': content})
            cursor.execute("INSERT INTO messages VAlUES (?,?)", (title, content))
            return redirect(url_for('index'))

    return render_template('create.html')
