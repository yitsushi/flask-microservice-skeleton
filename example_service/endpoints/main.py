from flask import Blueprint, jsonify

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Home view.
    This view will return an simple JSON mapping.

        {
            "valid_endpoint": true
        }
    """
    return jsonify({'valid_endpoint': True})
