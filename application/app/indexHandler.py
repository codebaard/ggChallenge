from flask import (
    Blueprint, render_template
)

from config.settings import GameSettings

bp = Blueprint('landing', __name__)

@bp.route('/')
def index():
    return render_template('base.html', branches = GameSettings.serviceBranches)
