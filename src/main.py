import numpy as np
import pandas as pd
import random

num_questions = 5
current_category = ''
line_num = 0
follow_up_prob = 0.80

Interview_df = pd.DataFrame(columns=['Question', 'Category'])

fhand = open('questions.csv')
for line in fhand:
    if line.startswith(","):
        continue
    if line.startswith('"#'):
        current_category = line.replace('#', '').replace('\n', '').lstrip('"').rstrip(',"')
    else:
        Interview_df.loc[line_num] = [line.replace('\n', '').rstrip(',"').lstrip('"'), current_category]
        line_num += 1

#Add category designation function here

num_questions = int(input('Enter number of questions: '))

if num_questions <= 0:
    print('test')


probe_q = Interview_df[Interview_df['Category'] == 'PROBES']['Question'].values
questions = Interview_df[Interview_df['Category'] != 'PROBES']['Question'].values

Interview_questions = random.sample(set(questions), num_questions)

for i, each in enumerate(Interview_questions):
    print('\n')
    print(each)
    probe = np.random.rand(1)[0]
    if probe <= follow_up_prob:
        print(np.random.choice(probe_q))
    
    next = input('\n\nEnter any key for next question ({} Remaining): '.format(num_questions - 1 - i))
    if next == 'quit':
        break
