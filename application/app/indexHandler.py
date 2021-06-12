from flask import (
    Blueprint, render_template, jsonify
)

bp = Blueprint('landing', __name__)

@bp.route('/troops')
def renderJSON():
    army = {
        'spearmen': '33',
        'swordsmen': '33',
        'archers': '34'
    }

    return jsonify(army)


@bp.route('/')
def index():
    return render_template('base.html')
