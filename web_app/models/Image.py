from web_app import db
from datetime import datetime

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    journal_id = db.Column(db.Integer, db.ForeignKey('journal.id'), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Image('{self.user_id}', '{self.journal_id}', '{self.image_file}', '{self.timestamp}')"