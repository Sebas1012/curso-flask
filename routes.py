from flask import Flask

app = Flask(__name__)

# Generamos 2 rutas nuevas, en este caso /saludo y /adios, las cuales no dependen de la ruta principal, que es /
@app.route('/saludo')
def saludo():
    return '<p>Hola! &#128077</p>'

@app.route('/adios')
def adios():
    return '<p>Adios! &#128075</p>'

if __name__ == '__main__':
    app.run