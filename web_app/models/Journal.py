from web_app import db
from web_app.models.User import User
from web_app.models.Question import Question
from web_app.models.Mood import Mood
from web_app.models.Image import Image
from sqlalchemy.orm import relationship

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    text = db.Column(db.Text, nullable=False)
    mood_id = db.Column(db.Integer, db.ForeignKey('mood.id'))
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))

    user = relationship('User', backref='journals')
    mood = relationship('Mood', backref='journals')
    image = relationship('Image', backref='journals')
    questions = relationship('Question', secondary='journal_question', backref='journals')

    def __repr__(self):
        return f"Journal('{self.date}', '{self.user_id}', '{self.mood_id}', '{self.image_id}')"

journal_question = db.Table('journal_question',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('journal_id', db.Integer, db.ForeignKey('journal.id'), primary_key=True)
)