# ---- Flask Hello Worls ---- #

# Importamos la clase Flask desde el paquete flask
from flask import Flask

# Creamos el objeto aplicación
app = Flask(__name__)

# Usamos el patrón decorator para
# enlazar la función de la vista con una url
@app.route("/")
@app.route("/hello")
def hello_world(): # Definimos la vista con una función que devuelve una cadena
	return "¡Hola, mundo! en Flask."

# Arrancamos el servidor de desarrollo
if __name__ == "__main__":
	app.run()
