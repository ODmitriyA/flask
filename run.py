import app
import app.views
import app.models as mod

typenom = mod.NomenclatureType(name='Товар').save()
nom = mod.Nomenclature(name='Карандаш простой', nomType=typenom, comment='ТМ').save()

app.main.run()