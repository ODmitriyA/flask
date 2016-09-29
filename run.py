import app.views
import app.models as mod

typenom = mod.NomenclatureType(name='Товар').save()
nom = mod.Nomenclature(name='Карандаш простой', nomType=typenom, comment='ТМ').save()
app.main.config['TEMPLATES_AUTO_RELOAD'] = True
app.main.run()