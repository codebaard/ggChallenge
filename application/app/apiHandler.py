from app.model.troops import Army
from app.errorHandler import handle_400

from flask import (
    Blueprint, render_template, jsonify, request, make_response
)

bp = Blueprint('api', __name__)

@bp.route('/troops')
def renderJSON():

    size = 100
    func = 'gaussian'

    try:
        size = request.args.get('size')
        func = request.args.get('func')
    except:
        handle_400("no such query parameter")

    army = Army(size)
    army.populate(func)

    resp = make_response(army.toJSON())
    resp.mimetype = 'application/json'

    return resp