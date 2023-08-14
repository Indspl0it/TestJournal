```python
from flask import jsonify
from web_app.models.Question import Question
from web_app import db

def add_question(question_text, user_id):
    new_question = Question(question_text=question_text, user_id=user_id)
    db.session.add(new_question)
    db.session.commit()
    return jsonify({"message": "Question added successfully!"}), 200

def get_questions(user_id):
    questions = Question.query.filter_by(user_id=user_id).all()
    return jsonify({"questions": [question.question_text for question in questions]}), 200

def delete_question(question_id):
    question = Question.query.get(question_id)
    if question:
        db.session.delete(question)
        db.session.commit()
        return jsonify({"message": "Question deleted successfully!"}), 200
    else:
        return jsonify({"message": "Question not found!"}), 404

def update_question(question_id, question_text):
    question = Question.query.get(question_id)
    if question:
        question.question_text = question_text
        db.session.commit()
        return jsonify({"message": "Question updated successfully!"}), 200
    else:
        return jsonify({"message": "Question not found!"}), 404
```