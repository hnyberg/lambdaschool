from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods=['POST'])
def addfood():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        print('Trying insertion')
        name = request.form['name']
        calories = request.form['calories']
        cuisine = request.form['cuisine']
        is_vegetarian = request.form['is_vegetarian']
        is_gluten_free = request.form['is_gluten_free']
        print('name: ' + name)
        print('calories: ' + calories)
        print('cuisine: ' + cuisine)
        print('is_vegetarian: ' + is_vegetarian)
        print('is_gluten_free: ' + is_gluten_free)
        cursor.execute('INSERT INTO foods (name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?,?,?,?,?)', (name, calories, cuisine, is_vegetarian, is_gluten_free))
        connection.commit()
        message = 'Insertion successful'
    except:
        connection.rollback()
        message = 'Insertion failed'
    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/search', methods=['GET'])
def search():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        word = request.args['word']
        print('searching for "' + word + '"')
        cursor.execute('SELECT * FROM foods WHERE name IS ?', (word,))
        message = cursor.fetchone()
    except:
        connection.rollback()
        message = 'Failed to get search results'
    finally:
        return render_template('result.html', message=message)
        connection.close()

@app.route('/favorite')
def favorite():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        print('Trying quering favorite food')
        cursor.execute('SELECT * FROM foods WHERE name IS "Pancakes"')
        message = cursor.fetchone()
        print(message)
        #message = jsonify(message)
    except:
        connection.rollback()
        message = 'Failed FIND'
    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/drop')
def drop():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        cursor.execute('DROP TABLE foods')
        message = 'dropped'
    except:
        connection.rollback()
        message = 'Drop failed'
    finally:
        return render_template('result.html', message=message)
