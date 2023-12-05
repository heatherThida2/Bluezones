from flask import Flask, render_template, request
from flask.helpers import redirect
from flask_sqlalchemy import SQLAlchemy

from model import connect_to_db

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

#sign up 
@app.route('/createAccount')
def create_account():
    return render_template('createAccount.html')
    
@app.route('/createAccount', methods=['POST'])
def sign_up():
    #getting informatrion from sign up form
    username = request.form.get['username']
    userlastname = request.form.get['userlastname']
    email = request.form.get['email']
    password = request.form.get['password']

    #need logic to check if username already exists
    #if username exists, return error message
    #if username doesn't exist, create user and return success message
    return redirect('/createAccount.html')

#login page
@app.route('/login')
def login():
    return render_template('loginPage.html')
@app.route('/loginPage', methods=["POST"])
def login_page():
    #getting information from login form
    email = request.form.get['email']
    password = request.form.get['password']
    
    #check if username and password are correct, checks database
    #if correct, return to main page 
    #if incorrect, return error message
    #save data in cookies/session 
    
    return redirect('/')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)