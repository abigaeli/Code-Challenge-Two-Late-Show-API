from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models.episode import Episode
from server.models.guest import Guest
from server import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    
    if not all([rating, guest_id, episode_id]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Check if guest and episode exist
    if not Guest.query.get(guest_id):
        return jsonify({'error': 'Guest not found'}), 404
    if not Episode.query.get(episode_id):
        return jsonify({'error': 'Episode not found'}), 404
    
    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201

@appearance_bp.route('/', methods=['GET'], strict_slashes=False)
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([{
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    } for appearance in appearances]), 200
