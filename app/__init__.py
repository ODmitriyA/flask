from flask import Flask
from flask_mongoengine import MongoEngine

main = Flask(__name__)
main.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'host': '192.168.0.101'
}
db = MongoEngine(main)
