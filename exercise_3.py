from flask import Flask

app = Flask(__name__)

@app.route('/numero/<uno>/<dos>')
def suma(uno, dos):
    resultado = int(uno) + int(dos)
    return '<p>La suma de {} + {} es {}</p>'.format(uno, dos, resultado)

if __name__ == '__main__':
    app.run