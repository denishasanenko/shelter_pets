from app import app
from flask import jsonify
from app.db import db_session
from app.schemas import shelters_chema


@app.route('/shelters/', methods=['GET'])
def pets():
    from app.db import db_session
    from app.models import Shelters
    # she = Shelters('68f5b2f4-8616-402e-934b-d47493acc705', 'Первый', 'Описание первого')
    # db_session.add(she)
    # db_session.commit()

    query = Shelters.select()
    shelters = db_session.execute(query)
    result = [dict(shelter) for shelter in shelters]
    return jsonify(result)


@app.route('/shelters/<string:shelter_uuid>', methods=['GET'])
def pet(shelter_uuid):
    from app.db import db_session
    from app.models import Shelters

    query = Shelters.select().where(Shelters.c.shelter_uuid == shelter_uuid)
    shelters = db_session.execute(query).first()
    result = dict(shelters)
    return jsonify(result)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()