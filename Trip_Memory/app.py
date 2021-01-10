from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
from init_db import *

def get_db_connection(table):
    conn=sqlite3.connect(table)
    conn.row_factory=sqlite3.Row #set the row_factory attribute to sqlite3.Row so that you can have name-based access to columns
                                    #This means that the database connectio will return rows that behave like regular Python dictionaries.
    return conn # returns the conn connection object to access the database

def get_post(post_id):
    conn=get_db_connection('database.db')
    post=conn.execute('SELECT * FROM posts WHERE id=?',
                     (post_id,)).fetchone()

    conn.close()
    if post is None:
        abort(404)
    return post

app=Flask(__name__)
app.config['SECRET_KEY']='A long random string'

@app.route('/',methods=('GET','POST'))
def home():
    return render_template('login.html')

@app.route('/login',methods=('GET','POST'))
def login():
    global username;
    if request.method=='POST':
        username=request.form['user']
        password=request.form['pwd']

        if not username:
            return redirect(url_for('register'))
        conn=get_db_connection('user.db')
        user=conn.execute('SELECT * FROM users WHERE username=? AND password=?',
                         (username,password)).fetchone()
        conn.close()
        if not user:
            flash('Invalid username or password, please try again!')
            return render_template('login.html')
        else:
            flash('Succesfully signed!')
            return redirect(url_for('index',username=username))
    return render_template('login.html')

@app.route('/register',methods=('GET','POST'))
def register():
    if request.method=='POST':
        email=request.form['email']
        username=request.form['user']
        password=request.form['pwd']
        if not email or not username or not password:
            flash('Please fill all the entries!')
        conn=get_db_connection('user.db')
        conn.execute('INSERT INTO users(email,username,password) VALUES(?,?,?)',(email,username,password))
        conn.commit()
        conn.close()
        flash('Thank you for the registration!')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/<username>/memories',methods=('GET','POST'))
def index(username):
    conn=get_db_connection('database.db')
    posts=conn.execute("SELECT * FROM posts"). fetchall()
    conn.close()
    if conn:
        conn.close()
        print('The sqlite connection is closed.')
    return render_template('index.html', posts=posts) # pass the posts object as an argument we got from the database to index.html,

@app.route('/<username>/memories/<int:id>', methods=('GET','POST'))
def post(username, id):
    post=get_post(id)
    return render_template("post.html", post=post)

@app.route('/create', methods=('GET','POST'))
def create():
    if request.method=='POST':
        title=request.form['title']
        content=request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn=get_db_connection()
            conn.execute('INSERT INTO posts(title,content) VALUES(?,?)',(title,content))
            conn.commit()
            conn.close()
            flash('New post is added!')
            return redirect(url_for('index',username=username))
    return render_template('create.html')
@app.route('/<int:id>/edit', methods=('GET','POST'))
def edit(id):
    post=get_post(id)
    if request.method=='POST':
        title=request.form['title']
        content=request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn=get_db_connection('database.db')
            conn.execute('UPDATE posts SET title=?, content=? WHERE id=?',
                        (title,content,id))
            conn.commit()
            conn.close()
            return redirect(url_for('index',username=username))
    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post=get_post(id)
    conn=get_db_connection('database.db')
    conn.execute('DELETE FROM posts WHERE id=?',(id,))
    conn.commit()
    conn.close()
    flash("'{}' was successfully deleted!".format(post['title']))
    return redirect(url_for('index',username=username))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.debug=True
    app.run()
