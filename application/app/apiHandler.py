from app.model.Army import Army

from flask import (
    Blueprint, request, make_response, abort
)

bp = Blueprint('api', __name__)


@bp.route('/troops')
def renderJSON():
    print("is this even rendering?")
    try:
        print("this 1")
        size = request.args.get('size')
        print("this 2")
        army = Army(size)
        army.populate()
        print("this 3")
        resp = make_response(army.toJSON())
        resp.mimetype = 'application/json'
        resp.status = 200

        print("this 4")
        return resp

    except Exception as e:
        abort(400, e)
