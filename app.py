from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__, static_folder='assets', template_folder='templates')
app.config['SECRET_KEY'] = 'your_secret_key'  # Ganti dengan kunci rahasia yang sudah di encrypt

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

users = {'1': {'id': '1', 'username': 'admin', 'password': 'password'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id, users[user_id]['username'], users[user_id]['password'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((u for u in users.values() if u['username'] == username and u['password'] == password), None)

        if user:
            user_id = user['id']
            user_obj = User(user_id, user['username'], user['password'])
            login_user(user_obj)
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if any(u['username'] == username for u in users.values()):
            flash('Username already exists. Please choose a different username.', 'error')
        else:
            new_user_id = str(len(users) + 1)

            users[new_user_id] = {'id': new_user_id, 'username': username, 'password': password}

            flash('Registration successful. Please login.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

class SimpleClient:
    def __init__(self, client_socket, statusMessage):
        client = SimpleClient()
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
