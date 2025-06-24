from server.app import create_app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

app = create_app()

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create users
        user1 = User(username='admin')
        user1.set_password('password')
        db.session.add(user1)

        # Create guests
        guest1 = Guest(name='John Doe', occupation='Comedian')
        guest2 = Guest(name='Jane Smith', occupation='Actor')
        db.session.add_all([guest1, guest2])

        # Create episodes
        episode1 = Episode(date=date(2023, 1, 1), number=1)
        episode2 = Episode(date=date(2023, 1, 8), number=2)
        db.session.add_all([episode1, episode2])

        db.session.commit()

        # Create appearances
        appearance1 = Appearance(rating=4, guest_id=guest1.id, episode_id=episode1.id)
        appearance2 = Appearance(rating=5, guest_id=guest2.id, episode_id=episode2.id)
        db.session.add_all([appearance1, appearance2])

        db.session.commit()
        print("Seed data created successfully.")

if __name__ == '__main__':
    seed_data()
