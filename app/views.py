from flask import render_template, redirect
import app
import app.models as mod
from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()
topbar = Navbar(
    View('Nomenclature', 'index', p = 'Nomenclature'),
    View('NomenclatureType', 'index', p = 'NomenclatureType')
)

nav.register_element('top', topbar)
nav.init_app(app.main)

@app.main.route('/<p>')
def index(p):
    try:
        noms = getattr(mod, p).objects
    except:
        return redirect('/error')
        
    return render_template(
        'message.html',
        noms = noms
    )

@app.main.route('/error')
def error():
    return 'Страница не существует!'
