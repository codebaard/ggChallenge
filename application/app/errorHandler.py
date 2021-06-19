from flask import (
    make_response
)

from app.model.Error import Error

def handle_400(e):
    err = Error(400, e)
    resp = make_response(err.toJSON())
    resp.mimetype = 'application/json'

    return resp,400

def handle_404(e):
    err = Error(404, e)
    resp = make_response(err.toJSON())
    resp.mimetype = 'application/json'

    return resp,404
