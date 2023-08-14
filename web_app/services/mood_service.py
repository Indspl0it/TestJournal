from flask_login import current_user
from web_app.models import Mood, db

def track_mood(mood_data):
    mood = Mood(user_id=current_user.id, mood=mood_data)
    db.session.add(mood)
    db.session.commit()

def get_moods():
    return Mood.query.filter_by(user_id=current_user.id).all()

def analyze_mood():
    moods = get_moods()
    mood_values = [mood.mood for mood in moods]
    mood_count = {i: mood_values.count(i) for i in mood_values}
    return mood_count
