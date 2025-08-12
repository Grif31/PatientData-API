from flask import Flask, jsonify, request
from models import db, Patient
from flask_migrate import Migrate
import os

app = Flask(__name__)
migrate = Migrate()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate.init_app(app, db)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'age':p.age, 'condition':p.condition} for p in patients])
    
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(name=data['name'], age=data.get('age'), condition=data.get('condition'))
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added!'}), 201
