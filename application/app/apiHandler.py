from app.model.Army import Army

from flask import (
    Blueprint, request, make_response, abort
)

bp = Blueprint('api', __name__)


@bp.route('/troops')
def renderJSON():
    """
        This function fetches the size attribute from the GET-request of the user and creates
        an army according to the given parameter. This is subsequently parsed to json
        and sent back to the user as response.
    """
    try:
        size = request.args.get('size')
        army = Army(size)
        army.populate()
        resp = make_response(army.toJSON())
        resp.mimetype = 'application/json'

        return resp,200

    except Exception as e:
        abort(400, e)
