from flask import render_template
import app


@app.main.route('/<p>')
def index(p):
    if p == 'Номенклатура':
         noms = app.models.Nomenclature.objects
    else:
        noms = app.models.NomenclatureType.objects

    return render_template(
        'message.html',
        noms = noms
    )
