from app.model.Army import Army

from flask import (
    Blueprint, request, make_response, abort
)

bp = Blueprint('api', __name__)


@bp.route('/troops')
def renderJSON():
    try:
        size = request.args.get('size')
        army = Army(size)
        army.populate()
        resp = make_response(army.toJSON())
        resp.mimetype = 'application/json'

        return resp,200

    except Exception as e:
        abort(400, e)
