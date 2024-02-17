from flask import Blueprint, request, jsonify
from ..models import Chambre, Reservation
from ..database import db

chambres = Blueprint('chambres', __name__)

@chambres.route('/api/chambres/disponibles')
def get_chambres_disponibles():
    date_arrivee = request.args.get('date_arrivee') # Format: YYYY-MM-DD
    date_depart = request.args.get('date_depart') # Format: YYYY-MM-DD

    if not date_arrivee or not date_depart:
        return {"success": False, "message": "Veuillez fournir une date d'arrivée et une date de départ."}
    
    chambres_disponibles = Chambre.query.filter(
        ~Chambre.reservations.any(
            (Reservation.date_arrivee <= date_depart) & (Reservation.date_depart >= date_arrivee)
        )
    ).all()

    return jsonify([{"id":chambre.id, "numero":chambre.numero, "type":chambre.type, "prix": chambre.prix} for chambre in chambres_disponibles])

@chambres.route('/api/chambres', methods=['POST'])
def add_chambre():
    data = request.get_json(silent=True)

    if not data or 'numero' not in data or 'type' not in data or 'prix' not in data:
        return {"success": False, "message": "Veuillez fournir un numéro, un type et un prix pour la chambre."}
    
    chambre = Chambre(
        numero=data['numero'],
        type=data['type'],
        prix=data['prix']
    )

    db.session.add(chambre)
    db.session.commit()

    return {"success": True, "message": "Chambre ajoutée avec succès."}

@chambres.route('/api/chambres/<int:id>', methods=['PUT'])
def update_chambre(id):
    chambre = Chambre.query.get(id)
    data = request.get_json(silent=True)

    if not chambre:
        return {"success": False, "message": "Chambre non trouvée."}    

    if not data or "numero" not in data and "type" not in data and "prix" not in data:
        return {"success": False, "message": "Veuillez fournir des informations à mettre à jour."}
    
    # Permet de mettre à jour seulement les informations qui sont fournies
    if "numero" in data:
        chambre.numero = data['numero']

    if "type" in data:
        chambre.type = data['type']

    if "prix" in data:
        chambre.prix = data['prix']

    db.session.commit()

    return {"success": True, "message": "Chambre mise à jour avec succès."}

@chambres.route('/api/chambres/<int:id>', methods=['DELETE'])
def delete_chambre(id):
    chambre = Chambre.query.get(id)

    if not chambre:
        return {"success": False, "message": "Chambre non trouvée."}

    db.session.delete(chambre)
    db.session.commit()

    return {"success": True, "message": "Chambre supprimée avec succès."}