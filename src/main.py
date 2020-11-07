import numpy as np
import pandas as pd
import random

num_questions = 5
current_category = ''
line_num = 0
follow_up_prob = 0.40

def select_mode(df):
    print('Select a mode: \n 1. All Questions (Data Science + Behavioral) \n 2. Behavioral Only \n 3. Behavioral + Tech (No Data Science) \n 4. Tech Only (Data Science) ')
    mode_select = None
    while mode_select not in (1, 2, 3, 4):
        mode_select = int(input('Select Mode 1, 2, 3, or 4: '))
    if mode_select == 1:
        new_df = df
    elif mode_select == 2:
        new_df = df[df['Category'] == 'Behavioral']
    elif mode_select == 3:
        new_df = df[(df['Category'] != 'Data Science') &
                    (df['Category'] != 'Statistics')]
    else:
        new_df = df[df['Category'] != 'Behavioral']
    return new_df

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

probe_q = Interview_df[Interview_df['Category'] == 'PROBES']['Question'].values
Interview_df = select_mode(Interview_df)
questions = Interview_df[Interview_df['Category'] != 'PROBES']['Question'].values
num_questions = int(input('Enter number of questions: '))

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
