import flask
import sys
import numpy as np
import pandas as pd
import random

sys.path.append("..")
from src import main

APP = flask.Flask(__name__)
@APP.route('/')
def get_input():
    return '''
        <style>
        h1 {
            font-size: 35px;
            text-align: center;
        }
        header {
            text-align: center;
        }
        form {
            font-size: 20px;
            text-align: center;
        }
        select {
            font-size: 15px;
        }
        input {
            font-size: 18px;
        }
        footer {
            padding: 5%;
        }
        </style>
        <header><img src="https://blog.gurock.com/wp-content/uploads/2015/08/interview.png" style="height:200px"></header>
        <h1>Mock Interview Question Generator</h1>
        <form action="/interview" method = 'POST'>
        <label for="mode">Choose Interview Mode:</label><br>
        <select name="mode" id="mode">
            <option value="1">Behavioral and Data Science</option>
            <option value="2">Behavioral Only</option>
            <option value="3">Behavioral and Tech (No Data Science)</option>
            <option value="4">Data Science Only (No Behavioral)</option>
        </select>
        <br><br>
        <label for="num_questions">Select Number of Questions</label><br>
        <select name="num_questions" id="num_questions">
            <option value="5">5</option>
            <option value="10">10</option>
            <option value="15">15</option>
            <option value="20">20</option>
        </select>
        <br><br>
        <input type="submit" value="Start Mock Interview">
        </form>
        <br><br><br><br><br><br>
        <footer>Created by Jacob Budnick<br>
        Connect with me:<br>
        <a href="https://www.linkedin.com/in/jacobbudnick/">
        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" alt="LinkedInJbudnick" style="width:30px;"></a>&nbsp;
        <a href="https://github.com/Jbudnick/">
        <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.12.3/icons/github.svg" alt="GithubJbudnick" style="width:30px;"></a>&nbsp;
        <a href="mailto:Jbudnick5@gmail.com">
        <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.5.0/icons/gmail.svg" alt="Jbudnick5@gmail.com" style="width:30px;"></a>
        </footer>
        '''

@APP.route('/interview', methods = ["GET","POST"])
def interview():
    mode = flask.request.form['mode']
    num_questions = int(flask.request.form['num_questions'])
    Interview_df = main.import_question_db()
    Interview_df = main.select_mode(Interview_df, mode_select= int(mode))
    question_list = []
    first_question = np.random.choice(
        Interview_df[Interview_df['Category'] == 'Introduction']['Question'].values)
    probe_q = Interview_df[Interview_df['Category']
                        == 'PROBES']['Question'].values
    questions = Interview_df[(Interview_df['Category'] != 'PROBES') &
                            (Interview_df['Category'] != 'Introduction')]['Question'].values
    Interview_questions = [first_question]
    Interview_questions.extend(random.sample(set(questions), num_questions - 1))
    return flask.render_template("index.html", len = len(Interview_questions), Interview_questions = Interview_questions)

if __name__ == '__main__':
    APP.run(host = '0.0.0.0', port = 8080, debug = True)