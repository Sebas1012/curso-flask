from flask import Flask

app = Flask(__name__)

@app.route('/palabra/<texto>')
def tamaño(texto):
    return '<p>La palabra <b>{}</b> tiene un tamaño de <b>{}</b> letras</p>'.format(texto, len(texto))

if __name__ == '__main__':
    app.run