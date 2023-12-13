# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask, request
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/data')
def get_time():
    # Returning an api for showing in  reactjs
    return {
        'Name': "geek",
        "Age": "22",
        "Date": x,
        "programming": "python"
    }


@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if is_valid_login(request.form['username'],
                          request.form['password']):
            return login_user(request.form['username'])
        else:
            error = 'Invalid username/password'
    return error


# Running app
if __name__ == '__main__':
    app.run(debug=True)
