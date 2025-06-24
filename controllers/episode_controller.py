from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.app import db
from server.models.episode import Episode
from server.models.appearance import Appearance

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    result = []
    for episode in episodes:
        result.append({
            'id': episode.id,
            'date': episode.date.isoformat(),
            'number': episode.number
        })
    return jsonify(result), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    appearances_list = []
    for appearance in appearances:
        appearances_list.append({
            'id': appearance.id,
            'rating': appearance.rating,
            'guest_id': appearance.guest_id
        })
    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': appearances_list
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"msg": "Episode and related appearances deleted"}), 200
