import numpy as np
import pandas as pd
import random

questions_df = pd.read_csv('questions.csv', delimiter='\n', names=['Question'])

questions = questions_df['Question'].values
questions = [question for question in questions if not question.startswith('#')]

Interview_questions = random.sample(set(questions), 5)

for each in Interview_questions:
    print(each)