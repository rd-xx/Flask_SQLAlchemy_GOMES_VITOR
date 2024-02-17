# Flask_SQLAlchemy_GOMES_VITOR

## Installation

Après avoir cloné le projet, il faudra exécuter les conteneurs avec `docker compose up --build`. Une fois cela fait, il faudra accéder au conteneur `web` pour y faire tourner les migrations (qui permettent d'initialiser la base de données) :

```bash
docker exec -it <id_conteneur_web> bash

flask db upgrade
```

## Routes

L'API est disponible à l'adresse <http://localhost:5001/api>.

- [POST] `/clients` : Créer un client
  - JSON BODY: `{"nom": "string", "email": "string"}`

- [GET] `/chambres/disponibles` : Récupérer les chambres disponibles pour une période donnée
  - PARAMS: `date_arrivee`, `date_depart` (sous le format `YYYY-MM-DD`)
  
- [POST] `/chambres` : Créer une chambre
  - JSON BODY: `{"numero": "integer", "type: "string", "prix": "float"}`

- [PUT] `/chambres/<id>` : Mettre à jour une chambre
  - JSON BODY: `{"numero": "integer", "type: "string", "prix": "float"}`

- [DELETE] `/chambres/<id>` : Supprimer une chambre

- [POST] `/reservations` : Créer une réservation
  - JSON BODY: `{"id_client": "integer", "id_chambre": "integer", "date_arrivee": "YYYY-MM-DD", "date_depart": "YYYY-MM-DD"}`
