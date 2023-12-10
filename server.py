from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)
app.secret_key = 'my precioussss'

@app.route('/')
def nothing():
    return redirect('/users')

@app.route('/users')
def showUsers():
    return render_template('users.html', users = User.get_users())

@app.route('/users/new')
def newUsers():
    return render_template('create.html')

@app.route('/user/create' , methods = ['Post'])
def createNew():
    data = {}
    data['first_name'] = request.form['first']
    data['last_name'] = request.form['last']
    data['email'] = request.form['email']
    User.save(data)
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)