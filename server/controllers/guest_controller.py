from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('/', methods=['GET'], strict_slashes=False)
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation
    } for guest in guests]), 200
