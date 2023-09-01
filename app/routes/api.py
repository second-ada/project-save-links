from flask import Blueprint
from app.validation import Validator

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.post('/category/')
def create_category():
    validation = Validator({'title': 'required|not_empty'}).check_errors()

    return ''


@bp.post('/links/')
def create_link():
    validation = Validator({
        'category': 'required|not_empty',
        'link': 'required|not_empty'
    }).check_errors()

    data = validation.data

    return data
