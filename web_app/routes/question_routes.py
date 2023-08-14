```python
from flask import Blueprint, request, redirect, render_template, url_for, flash
from flask_login import login_required, current_user
from web_app.models.Question import Question
from web_app.services.question_service import add_question_to_db

question_routes = Blueprint('question_routes', __name__)

@question_routes.route('/add_question', methods=['GET', 'POST'])
@login_required
def add_question():
    if request.method == 'POST':
        question_text = request.form.get('question_text')
        question = Question(question_text=question_text, user_id=current_user.id)
        add_question_to_db(question)
        flash('Question added successfully', 'question_message')
        return redirect(url_for('dashboard'))
    return render_template('question.html')
```