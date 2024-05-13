

from flask import Blueprint

tipoNomina = Blueprint("tipoNomina", __name__, static_folder="static", template_folder="templates")

from . import rutas