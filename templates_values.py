from flask import Flask, render_template

app = Flask(__name__)

@app.route('/empleado')
def valores():
    empleado = 'Oscar'
    tipo = "TI"
    datos = {'tipo':'perro', 'lenguaje':'ruby'}
    lenguajes = ['ruby', 'crystal', 'go']
    # Para pasar valores desde nuestro script python a nuestro html, solo basta con luego de cargar nuestro html crear las "variables"
    # que se van a mostrar en nuestro html, en este caso a empleado(que sera la que llamaremos en nuestro html) le cargaremos
    # la variable empleado que creamos anteriormente con el nombre Oscar lo mismo pasa con el tipo.

    # Luego de eso solo basta en el html, en la etiqueta que queramos llamar nuestro valor, abrir llaves dobles y poner el nombre de la variable
    # por ejemplo <h1> {{ empleado }} </h1>
    # *VER EJEMPLO EN index.html
    return render_template('index.html', empleado=empleado, tipo=tipo, datos=datos, lenguajes=lenguajes)

if __name__ == '__main__':
    app.run