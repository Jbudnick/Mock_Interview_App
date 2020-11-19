import flask
import numpy as np
import pandas as pd
import random

import main

APP = flask.Flask(__name__)
@APP.route('/')
def get_input():
    return flask.render_template("home.html")

@APP.route('/interview', methods = ["GET","POST"])
def interview():
    mode = flask.request.form['mode']
    num_questions = int(flask.request.form['num_questions'])
    Interview_df = main.import_question_db()
    Interview_df = main.select_mode(Interview_df, mode_select= int(mode))
    question_list = []
    introQuestions_list = Interview_df[Interview_df['Category']
                                    == 'Introduction']['Question'].values
    first_question = np.random.choice(introQuestions_list)
    questions = Interview_df[(Interview_df['Category'] != 'PROBES') &
                            (Interview_df['Category'] != 'Introduction')]['Question'].values
    Interview_questions = [first_question]
    Interview_questions.extend(random.sample(set(questions), num_questions - 1))
    return flask.render_template("index.html", len = len(Interview_questions), Interview_questions = Interview_questions)

@APP.route('/showdf', methods = ["GET", "POST"])
def showdf():
    Interview_df = main.import_question_db()
    pd.set_option('display.max_colwidth', -1)
    return Interview_df.to_html()

if __name__ == '__main__':
    APP.run(host = '0.0.0.0', port = 80, debug = True)
