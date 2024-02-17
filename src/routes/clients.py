from flask import Blueprint, request, jsonify
from ..models import Client
from ..database import db

clients = Blueprint('clients', __name__)

@clients.route('/api/clients', methods=['POST'])
def add_client():
    data = request.get_json(silent=True)

    if not data or 'nom' not in data or 'email' not in data:
        return {"success": False, "message": "Veuillez fournir un nom, un prénom et un email pour le client."}
    
    client = Client(
        nom=data['nom'],
        email=data['email']
    )

    db.session.add(client)
    db.session.commit()

    return {"success": True, "message": "Client ajouté avec succès."}