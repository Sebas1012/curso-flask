from flask import Flask, render_template

app = Flask(__name__)

@app.route('/singup')
def singup():
    return render_template('sign_up.html')

if __name__ == "__main__":
    app.run