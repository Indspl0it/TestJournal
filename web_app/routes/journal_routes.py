```python
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from web_app.models import Journal, Question, Mood, Image
from web_app.services import journal_service, question_service, mood_service, image_service

journal = Blueprint('journal', __name__)

@journal.route('/journal_entry', methods=['GET', 'POST'])
@login_required
def journal_entry():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        mood = request.form.get('mood')
        image_file = request.files['image_file']
        questions = request.form.getlist('questions')

        journal_entry = journal_service.create_journal_entry(current_user.id, title, content, mood, image_file, questions)
        if journal_entry:
            flash('Journal entry created successfully', 'journal_entry_message')
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash('Error creating journal entry', 'journal_entry_message')

    questions = question_service.get_all_questions()
    moods = mood_service.get_all_moods()
    return render_template('journal_entry.html', questions=questions, moods=moods)

@journal.route('/journal_entry/<int:journal_id>', methods=['GET', 'POST'])
@login_required
def edit_journal_entry(journal_id):
    journal_entry = journal_service.get_journal_entry_by_id(journal_id)
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        mood = request.form.get('mood')
        image_file = request.files['image_file']
        questions = request.form.getlist('questions')

        updated_journal_entry = journal_service.update_journal_entry(journal_entry, title, content, mood, image_file, questions)
        if updated_journal_entry:
            flash('Journal entry updated successfully', 'journal_entry_message')
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash('Error updating journal entry', 'journal_entry_message')

    questions = question_service.get_all_questions()
    moods = mood_service.get_all_moods()
    return render_template('journal_entry.html', journal_entry=journal_entry, questions=questions, moods=moods)

@journal.route('/journal_entry/<int:journal_id>/delete', methods=['POST'])
@login_required
def delete_journal_entry(journal_id):
    journal_service.delete_journal_entry(journal_id)
    flash('Journal entry deleted successfully', 'journal_entry_message')
    return redirect(url_for('dashboard.dashboard'))
```