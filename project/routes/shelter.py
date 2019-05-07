from flask import Blueprint, jsonify
from project.models.shelter import Shelter
from project.models import db_session

shelter_bp = Blueprint('shelter_bp', __name__, url_prefix='/shelters')


@shelter_bp.route('/', methods=['GET'])
def shelters():
    query = Shelter.select()
    shelters = db_session.execute(query)
    result = [dict(shelter) for shelter in shelters]
    return jsonify(result)


@shelter_bp.route('/<string:shelter_uuid>', methods=['GET'])
def shelter(shelter_uuid):
    query = Shelter.select().where(Shelter.c.shelter_uuid == shelter_uuid)
    shelter = db_session.execute(query).first()
    return jsonify(dict(shelter))


@shelter_bp.route('/', methods=['POST'])
def createShelter():
    she = Shelter.insert().values(name='Второй', description='Описание второго')
    db_session.execute(she)
    db_session.commit()
    query = Shelter.select()
    shelters = db_session.execute(query)
    result = [dict(shelter) for shelter in shelters]
    return jsonify(result)
