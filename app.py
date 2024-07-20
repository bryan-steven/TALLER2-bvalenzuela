from flask import Flask, render_template
from models.perro import Perro
from models.gato import Gato
from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bienvenido a la API de sonidos de animales!"

@app.route("/sonido/perro", methods=['GET'])
def perro():
    perro_1 = Perro("Dakota", 20.00, 3)
    return perro_1.hacer_sonido()

@app.route("/sonido/huron", methods=['GET'])
def huron():
    huron_1 = Huron("Huroncito", 2.00, 1)
    return huron_1.hacer_sonido()

@app.route("/sonido/gato", methods=['GET'])
def gato():
    gato_1 = Gato("Michi", 5.00, 2)
    return gato_1.hacer_sonido()

@app.route("/sonido/boa", methods=['GET'])
def boa():
    boa_1 = Boa_Constrictor("Mamba", 3.00, 5)
    return boa_1.hacer_sonido()

@app.route("/sonidos", methods=['GET'])
def sonidos():
    return render_template("pagina_web.html")

if __name__ == '__main__':
    app.run(debug=True)