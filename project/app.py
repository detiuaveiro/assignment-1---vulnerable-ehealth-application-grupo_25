from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contactform')
def contactform():
    return render_template('contactform.html')

@app.route('/logged')       #mudar isto futuramente
def logged():
    return render_template('logged.html')

@app.route('/create-acc')
def createacc():
    return render_template('createacc.html')

if __name__ == '__main__':
    app.run(use_reloader = True)
