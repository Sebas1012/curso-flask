from flask import Flask

app = Flask(__name__)

# Para crear una ruta dinamica solo basta con generar una ruta ya estatica junto al valor variable, el cual debe ir dentro de <>,
# luego de eso debemos pasarlo como parametro al metodo que ejecutaremos y en este caso como retornaremos un string usamos la funcion
# format() para que sustituya las {} por el valor variable que estamos pasando en la ruta.
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return '<p>Hola {}! Saludos desde Flask &#128083</p>'.format(nombre)


if __name__ == '__main__':
    app.run