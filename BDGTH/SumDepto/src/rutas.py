import requests
from flask import jsonify, Blueprint, render_template, request, url_for,  redirect
import matplotlib.pyplot as plt
from itertools import groupby
import itertools
import numpy as np


SumDepto = Blueprint("SumDepto", __name__, static_folder="static", static_url_path="static", template_folder="templates")


#@SumDepto.route("/home")
@SumDepto.route("/")
def home():

    #return render_template("index.html")
    return render_template("home_SumDepto.html")
    #return "Hola"


@SumDepto.route('/consume_api', methods=['GET'])
def consume_api():
    #script_url = url_for('BDGTH/TiposdeNomina/src/static', filename='bar_chart.png')

    if request.method == 'GET':
        #mes = request.form['mes']

        #print(f'a ver que sale pa {mes}')

        # Hacer una solicitud GET a la API REST local
        #response = requests.get('http://127.0.0.1:5000//api/movies')  # Ejemplo de URL local
        #response = requests.get('http://127.0.0.1:5000/sumaMovDepto/listarSumDepto')  # Ejemplo de URL local
        response = requests.get('http://127.0.0.1:5000/sumMovDepto2/')  # Ejemplo de URL local

        #print(response)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Devolver los datos JSON recibidos
            #print(response.json())

            data = response.json()

                        # Inicializar cuatro listas nuevas
            lista_A = []
            lista_B = []
            lista_DESCRIPCION = []
            lista_R = []

            # Iterar sobre los elementos del JSON
            for elemento in data:
                # Inicializar cuatro listas nuevas
                lista_A = [elemento.get("A", 0) if elemento.get("A") is not None else 0 for elemento in data]
                lista_B = [elemento.get("B", 0) if elemento.get("B") is not None else 0 for elemento in data]
                lista_DESCRIPCION = [elemento.get("descripcion", "") for elemento in data]
                lista_R = [elemento.get("R", 0) if elemento.get("R") is not None else 0 for elemento in data]

            # Imprimir las listas
            print("Lista de valores para la clave 'A':", lista_A)
            print(" ")
            print("Lista de valores para la clave 'B':", lista_B)
            print(" ")
            print("Lista de valores para la clave 'DESCRIPCION':", lista_DESCRIPCION)
            print(" ")
            print("Lista de valores para la clave 'R':", lista_R)

            graficar_barra(lista_DESCRIPCION,lista_A,lista_B,lista_R)

            
            #return jsonify(response.json())
            #return render_template('tipoNomina.html',chart_image = graficaBarras)
            return render_template('SumDepto.html',chart_image = graficar_barra)
            #return redirect(url_for('SumDepto.home',chart_image = graficar_barra))

        
        else:
            # Devolver un mensaje de error si la solicitud falla
            return jsonify({'error': 'No se pudo obtener los datos de la API'}), 500
        
def graficar_barra(lista_DESCRIPCION,lista_A,lista_B, lista_R):
        
        # Crear figuras y ejes
        fig, ax = plt.subplots(figsize=(10, 15))

        # Ajustar el espacio entre las barras en la figura
        plt.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.1)


        

        # Gráfico 1
        bars1 = ax.barh(np.arange(len(lista_DESCRIPCION))-0.2, lista_A, height=0.4, color='skyblue', label='A')

        # Gráfico 2
        bars2 = ax.barh(np.arange(len(lista_DESCRIPCION)), lista_B, height=0.4, color='lightgreen', label='B')

        # Gráfico 3
        bars3 = ax.barh(np.arange(len(lista_DESCRIPCION))+0.2, lista_R, height=0.4, color='lightcoral', label='R')

        # Etiquetas y título
        ax.set_xlabel('Valores')
        ax.set_ylabel('DEPARTAMENTOS')
        ax.set_yticks(np.arange(len(lista_DESCRIPCION)))
        ax.set_yticklabels(lista_DESCRIPCION)
        ax.set_title('Suma de movimientos A/R/B por depto BDGTH 2024')


        # Ajustar el espacio entre las barras
        plt.tight_layout()

        # Mostrar leyenda
        plt.legend()

        # Mostrar gráfico
        #plt.show()

        # Etiquetas de valores y descripciones
        for i, (val1, val2, val3) in enumerate(zip(lista_A, lista_B, lista_R)):
            ax.text(val1, i - 0.2, f'{val1}', ha='left', va='center')
            ax.text(val2, i, f'{val2}', ha='left', va='center')
            ax.text(val3, i + 0.2, f'{val3}', ha='left', va='center')
        

        image_path = 'BDGTH/SumDepto/src/static/bar_chart_SumDepto.png'
       
        plt.savefig(image_path)
        #plt.close()

        return image_path