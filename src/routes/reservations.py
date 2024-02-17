from flask import Blueprint, request, jsonify
from ..models import Chambre, Reservation, Client
from ..database import db

reservations = Blueprint('reservations', __name__)

@reservations.route('/api/reservations', methods=['POST'])
def add_reservation():
    data = request.get_json(silent=True)

    if not data or 'id_client' not in data or 'id_chambre' not in data or 'date_arrivee' not in data or 'date_depart' not in data:
        return {"success": False, "message": "Veuillez fournir un client, une chambre, une date d'arrivée et une date de départ pour la réservation."}
    
    chambre = Chambre.query.get(data['id_chambre'])
    if not chambre:
        return {"success": False, "message": "Chambre non trouvée."}
    
    client = Client.query.get(data['id_client'])
    if not client:
        return {"success": False, "message": "Client non trouvé."}

    reservations = chambre.reservations.filter(
        (Reservation.date_arrivee <= data['date_depart']) & (Reservation.date_depart >= data['date_arrivee'])
    ).all()

    if reservations:
        return {"success": False, "message": "La chambre n'est pas disponible pour les dates demandées."}

    reservation = Reservation(
        id_client=data['id_client'],
        id_chambre=data['id_chambre'],
        date_arrivee=data['date_arrivee'],
        date_depart=data['date_depart'],
        statut="confirmé"
    )

    db.session.add(reservation)
    db.session.commit()

    return {"success": True, "message": "Réservation créée avec succès."}