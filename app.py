from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hadiah')
def hadiah():
    return render_template('hadiah.html')

if __name__ == '__main__':
    app.run(debug=True)
