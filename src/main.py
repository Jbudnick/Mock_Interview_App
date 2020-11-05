import numpy as np
import pandas as pd
import random

num_questions = 5

Interview_df = pd.DataFrame(columns = ['Question', 'Category'])
current_category = ''
line_num = 0

fhand = open('questions.csv')
for line in fhand:
    if line.startswith('#'):
        current_category = line.replace('#', '').replace('\n', '')
    else:
        Interview_df.loc[line_num] = [line.replace('\n', ''), current_category]
        line_num += 1

#Add category designation function here

questions = Interview_df['Question'].values

Interview_questions = random.sample(set(questions), num_questions)

for i, each in enumerate(Interview_questions):
    print('\n')
    print(each)
    input('\n\nEnter any key for next question ({} Remaining): '.format(num_questions - 1 - i))