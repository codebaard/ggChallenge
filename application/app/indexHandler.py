from flask import (
    Blueprint, render_template
)

from app.config.settings import GameSettings

bp = Blueprint('landing', __name__)

@bp.route('/')
def index():
    return render_template('index.html', branches = GameSettings.serviceBranches)
