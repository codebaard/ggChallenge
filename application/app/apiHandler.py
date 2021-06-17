from application.app.model.troops import Army
from application.app.errorHandler import handle_400

from flask import (
    Blueprint, render_template, jsonify, request
)

bp = Blueprint('landing', __name__)

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

    return jsonify(army)