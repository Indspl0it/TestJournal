from flask_login import current_user
from web_app.models import Journal, db

def create_journal_entry(title, content, mood_id, image_id):
    new_entry = Journal(title=title, content=content, mood_id=mood_id, image_id=image_id, user_id=current_user.id)
    db.session.add(new_entry)
    db.session.commit()

def get_all_entries():
    return Journal.query.filter_by(user_id=current_user.id).all()

def get_entry_by_id(entry_id):
    return Journal.query.get(entry_id)

def update_entry(entry_id, title, content, mood_id, image_id):
    entry = get_entry_by_id(entry_id)
    if entry:
        entry.title = title
        entry.content = content
        entry.mood_id = mood_id
        entry.image_id = image_id
        db.session.commit()

def delete_entry(entry_id):
    entry = get_entry_by_id(entry_id)
    if entry:
        db.session.delete(entry)
        db.session.commit()