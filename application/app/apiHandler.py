from app.model.Army import Army
from app.errorHandler import handle_400

from flask import (
    Blueprint, render_template, jsonify, request, make_response
)

bp = Blueprint('api', __name__)

@bp.route('/troops')
def renderJSON():

    size = 100

    try:
        size = request.args.get('size')
    except:
        handle_400("something bad happened")

    army = Army(size)
    army.populate()

    resp = make_response(army.toJSON())
    resp.mimetype = 'application/json'

    return resp