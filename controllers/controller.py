from flask import render_template, request, redirect
from app import app
from models.books import *

@app.route('/library')
def index():
    return render_template('index.html', title = 'Give a Hoot! Read a Book!', books = books)

@app.route('/library/<index>')
def single_book(index):
   rent_this_book = books[int(index)]

   return render_template('book.html', book = rent_this_book)


@app.route('/library', methods = ['POST'])
def add_new_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    description = request.form['description']
    checked_out = True if 'checked_out' in request.form else False

    newbook = Book(title=title, author=author, genre = genre, description = description, checked_out = checked_out)
    add_book(newbook)
    
    return redirect ('/library')

@app.route('/library/delete/<title>', methods=['POST'])
def delete(title):
  delete_book(title)

  return redirect('/library')



