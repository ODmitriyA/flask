from app import app, views
from app.models import Nomenclature, NomenclatureType

typenom = NomenclatureType(10, 'Канцтовары')
nom = Nomenclature(20, 'Карандаш', typenom)

print(nom)
