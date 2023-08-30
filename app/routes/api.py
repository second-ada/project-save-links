from flask import Blueprint, request, abort
from app.validation import Validator

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.post('/links/')
def read():
    validation = Validator({'category': 'required', 'link': 'required'})

    return validation.data
