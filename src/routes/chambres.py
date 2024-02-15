from flask import Blueprint
from ..models import Chambre
from ..database import db

chambres = Blueprint('chambres', __name__)

@chambres.route('/api/chambres/disponibles')
def get_chambres():
    chambres = Chambre.query.all()
    return {"chambres": [chambre.to_dict() for chambre in chambres]}
