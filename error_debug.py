from flask import Flask

app = Flask(__name__)

@app.route('/palabras/<texto>')
def saludo(texto):
    return '<p>La letra en la posicion 5 es: {}<p>'.format(texto[5])

if __name__ == '__main__':
    app.run()

# Es importante tener encuenta que a la hora de desarrollar es posible que tengamos posibles errores en nuestro codigo, por lo mismo
# para el manejo de los mismos y tener informacion mas detallada, he incluso una consola interactiva en el navegador, debemos ejecutar nuestra 
# app en modo debug con el comando: flask --app nombredelarchivo --debug run Esto solamente en desarrollo.

# * Este codigo tiene un posible error y es que si la palabra es de menos caracteres lanzaria un error que sin el modo debug no tendriamos
# * mucha informacion.