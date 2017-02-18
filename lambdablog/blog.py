from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')
print('Database opened')
connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')
print('Table created succesuflly')
connection.close()
print('Connection closed')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/addpost', methods = ['POST'])
def addPost():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        title = request.form['title']
        post = request.form['post']
        print('title: ' + title)
        print('post: ', post)
        cursor.execute('INSERT INTO posts (title, post) VALUES (?,?)', (title, post))
        print('Execute success')
        connection.commit()
        print('comit success')
        message = 'Post successfully saved'
    except:
        connection.rollback()
        message = 'Error in insert operation'
    finally:
        return render_template('result.html', message = message)
        connection.close()
