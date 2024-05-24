from flask import Flask, render_template
from BDGTH.TiposdeNomina.src.rutas import tipoNomina
from BDGTH.SumDepto.src.rutas import SumDepto
from waitress import serve

app = Flask(__name__, template_folder='BDGTH/templates')

app.register_blueprint(tipoNomina, url_prefix="/tipoDeNomina")
app.register_blueprint(SumDepto, url_prefix="/sumaMovDepto")


@app.route("/")
def index():

    return render_template('index.html')

def pagina_no_encontrada(error):
    return '<h1>La pagina que intentas buscar no existe ...</h1>', 404


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    serve(app, host='0.0.0.0', port=3000)
    #app.run(port = 3000, debug=True)
