from flask import Flask, render_template, request
import os

app = Flask(__name__)

template_dir = os.path.abspath('frontend/src/templates')
static_dir = os.path.abspath('frontend/src/static')
app.template_folder = template_dir
app.static_folder = static_dir


def get_recommendation(subjects, scores, desired_profession):

    recommendation = f"Рекомендация: Поступите на направление X"

    return recommendation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation', methods=['POST'])
def recommendation():
    subjects = int(request.form['subjects'])
    scores = request.form['scores']
    desired_profession = request.form['desired_profession']
    
    recommendation = get_recommendation(subjects, scores, desired_profession)
    
    return recommendation

if __name__ == '__main__':
    app.run(debug=True)
