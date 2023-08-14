```python
from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from web_app.models.Mood import Mood
from web_app.services.mood_service import save_mood, get_moods, analyze_mood

mood = Blueprint('mood', __name__)

@mood.route('/mood', methods=['GET', 'POST'])
@login_required
def track_mood():
    if request.method == 'POST':
        mood = request.form.get('mood')
        mood_entry = Mood(user_id=current_user.id, mood=mood)
        save_mood(mood_entry)
        flash('Mood tracked successfully', 'mood_message')
        return redirect(url_for('dashboard'))
    moods = get_moods(current_user.id)
    return render_template('mood.html', moods=moods)

@mood.route('/mood/analyze', methods=['GET'])
@login_required
def mood_analysis():
    moods = get_moods(current_user.id)
    mood_analysis = analyze_mood(moods)
    return render_template('dashboard.html', mood_analysis=mood_analysis)
```