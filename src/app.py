from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Here you would typically validate the credentials
    print(f"User logged in: {username}")
    
    # Redirect to portal page after successful login
    return redirect(url_for('portal'))

@app.route('/portal')
def portal():
    return render_template('portal.html')

if __name__ == '__main__':
    app.run(debug=True)