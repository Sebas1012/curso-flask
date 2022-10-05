from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hijo1')
def hijo1():
    return render_template('hijo1.html')

@app.route('/hijo2')
def hijo2():
    return render_template('hijo2.html')

if __name__ == '__main__':
    app.run