from flask import Flask

app = Flask(__name__)

@app.route('/edad/<nombre>/<edad>')
def concatenar(nombre, edad):
    return '<p>Hola {}! Tu edad es {}</p>'.format(nombre, edad)
