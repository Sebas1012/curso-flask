from flask import Flask

# Instanciamos la clase Flask
app = Flask(__name__)

# Creamos nuestra primera ruta, que en este caso hace referencia a la ruta principal o index de nuestra web y ejecutamos la funcion saludo()
@app.route('/')
def saludo():
    return '<p>Hola desde Flask! &#128187</p>'

# Validamos que este fichero sea el principal y en caso de ser asi, ejecutamos nuestro codigo.
# TODO: Investigar por qué se debe realizar esta comprobacion. 
if __name__ == '__main__':
    app.run

# Para ejecutar nuestra aplicacion, solo debebemos ejecutar en nuestra consola el comando flask --app nombredelarchivo run,
# aunque mi recomendacion es que a la hora de desarrollar lo ejecutemos en modo debug con el comando flask --app nombredelarchivo --debug run