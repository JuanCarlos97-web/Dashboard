import requests
from flask import jsonify, Blueprint, render_template, request, url_for,  redirect
import matplotlib.pyplot as plt
from itertools import groupby
import itertools


tipoNomina = Blueprint("tipoNomina", __name__, static_folder="static", static_url_path="static", template_folder="templates/templatesTipoNomina")

#@tipoNomina.route("/home_tipoNomina")
@tipoNomina.route("/")
def home():
    
    #return render_template("index.html")
    return render_template("home_tipoNomina.html")


@tipoNomina.route('/consume_api', methods=['POST'])
def consume_api():
    #script_url = url_for('BDGTH/TiposdeNomina/src/static', filename='bar_chart.png')

    if request.method == 'POST':
        mes = request.form['mes']

        print(f'a ver que sale pa {mes}')

        # Hacer una solicitud GET a la API REST local
        #response = requests.get('http://127.0.0.1:5000//api/movies')  # Ejemplo de URL local
        response = requests.get('http://127.0.0.1:5000/tipoDeNomina/listarTiposDeNominas/{0}'.format(mes))  # Ejemplo de URL local

        #print(response)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Devolver los datos JSON recibidos
            #print(response.json())

            data = response.json()


        # Inicializar un diccionario para realizar el conteo
            count_by_tipo_nomina = {}

            # Contar los valores por la clave de tipo de nómina
            for item in data:
                tipo_nomina = item["CLAVE_TIPO_NOMINA"]
                count_by_tipo_nomina[tipo_nomina] = count_by_tipo_nomina.get(tipo_nomina, 0) + 1

            # Extraer las claves y los conteos del diccionario
            tipos_nomina = list(count_by_tipo_nomina.keys())
            conteos = list(count_by_tipo_nomina.values())

            #enteros = [int(s) for s in tipos_nomina]

            #print(f'eje x {tipos_nomina}')
            print(f'eje x {tipos_nomina}')
            print(f'eje y {conteos}')

            graficaBarras = graficar(tipos_nomina,conteos,mes)

            
            #return jsonify(response.json())
            return render_template('tipoNomina.html',chart_image = graficaBarras)
            #return render_template('home.html',chart_image = graficaBarras)
            #return redirect(url_for('tipoNomina.home'))

        
        else:
            # Devolver un mensaje de error si la solicitud falla
            return jsonify({'error': 'No se pudo obtener los datos de la API'}), 500
    


def graficar(ejeX,ejeY,mes):

                # Colores de las barras
        colores = ['#FB7506', '#E3CF0B', '#0B56E3']

        plt.figure(figsize=[12,8])
        # Ancho personalizado para las barras
        ancho_barras = 1

            # Crear la gráfica de barras	
        bars = plt.bar(ejeX, ejeY, color=colores, width=ancho_barras)
        plt.tight_layout()
# Ajustar el espaciado entre las barras
        # Ajustar el espaciado entre las barras y el eje y
        plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.3)
        plt.xlabel('Tipo de Nómina')
        plt.ylabel('Cantidad X tipo de nómina')
        plt.title(f'Tipo de Nomina en el mes de {mes}')
        plt.xticks(rotation=45)
       # plt.yticks(lista_y, rotation=45)

        # Añadir etiquetas de datos a las barras
        for barra in bars:
            yval = barra.get_height()
            plt.text(barra.get_x() + barra.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

        # Agregar líneas horizontales para marcar la cantidad en el eje Y
       # for y in lista_y:
         #   plt.axhline(y, color='gray', linestyle='--', linewidth=0.5)

            # Guardar la gráfica en un archivo temporal
        #image_path = 'BDGTH/TiposdeNomina/src/static/bar_chart.png'
        #image_path = url_for('tipoNomina.static', filename='bar_chart.png')
        image_path = 'BDGTH/TiposdeNomina/src/static/bar_chart.png'
        #image_path = 'tipoNomina.static/bar_chart.png'

        plt.savefig(image_path)
        #plt.close()

        return image_path
        

        
  