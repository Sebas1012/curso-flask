# Para poder cargar o renderizar archivos HTML es importante importar la libreria render_template, la cual sera la encargada de renderizar
# el documeno HTML.

# *Tambien es importante que en la ruta de nuestro proyocto, creemos una carpeta llamada templates, que sera donde estaran todos los archivos
# *HTML que cargaremos, ya que la libreria render_template por defecto carga los archivos que esten en dicha carpeta.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    # Para renderizarlo solo hace falta llamar la funcion render_template() y pasarle como parametro el nombre del archivo HTML
    return render_template('index.html')

if __name__ == '__main__':
    app.run