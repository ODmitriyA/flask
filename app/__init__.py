from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap



main = Flask(__name__)
Bootstrap(main)
main.config['BOOTSTRAP_SERVE_LOCAL'] = True
main.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'host': '192.168.0.101'
}
db = MongoEngine(main)
