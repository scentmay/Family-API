"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Recuperar todos los miembros de la familia
@app.route('/members', methods=['GET'])
def getAllMembers():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Insertar un miembro en la familia
@app.route('/member', methods=['POST'])
def createMember():
    info_request = request.json
    if (jackson_family.add_member(info_request) == True):
        return jsonify("Usuario creado"), 200
    else:
        return jsonify("Ocurrió un error al agregar el miembro de la familia"), 400
       
    
# Recuperar uno de los miembros de la familia
@app.route('/member/<int:id>', methods=['GET'])
def getOneMember(id):
    member = jackson_family.get_member(id)
    if member is False:
        return "Ocurrió un error al agregar el miembro", 404
    else:
        response_body = {
        "family": member
    }
    return jsonify(response_body), 200

# Eliminar uno de los miembros de la familia
@app.route('/members/<int:id>', methods=['DELETE'])
def deleteOneMember(id):
    estado = jackson_family.delete_member(id)
    if (estado == True):
        return "Miembro de la familia eliminado correctamente", 200
    else:
        return "Ocurrió un error al agregar el miembro", 400


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
