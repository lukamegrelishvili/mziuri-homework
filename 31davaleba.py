from flask import Flask

app = Flask(__name__)

@app.route('/register')
def register():
    return '<h2>Register</h2>'

@app.route('/login')
def login():
    return '<h2>Login</h2>'

@app.route('/profile')
def profile():
    return '<h2>Profile</h2>'

@app.route('/')
def home():
    return '''
    <h2>Welcome!</h2>
    <ul>
        <li><a href="/register">Register</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/profile">Profile</a></li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)
