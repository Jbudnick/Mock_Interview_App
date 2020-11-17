import numpy as np
import pandas as pd
import random
from os import system

def import_question_db():
    line_num = 0
    current_category = ''
    Interview_df = pd.DataFrame(columns=['Question', 'Category'])
    fhand = open('questions.csv')
    for line in fhand:
        if line == '\n':
            continue
        if line.startswith('#'):
            current_category = line.replace('#', '').replace('\n', '')
        else:
            Interview_df.loc[line_num] = [line.replace('\n', ''), current_category]
            line_num += 1
    return Interview_df

def select_mode(df, mode_select = None):
    if mode_select == None:
        system('clear')
        print('\nSelect a mode: \n 1. All Questions (Data Science + Behavioral) \n 2. Behavioral Only \n 3. Behavioral + Tech (except Data Science) \n 4. Data Science/Tech Only ')
        mode_select = None
        while mode_select not in (1, 2, 3, 4):
            mode_select = int(input('Select Mode 1, 2, 3, or 4: '))
    if mode_select == 1:
        new_df = df
    elif mode_select == 2:
        new_df = df[(df['Category'] == 'Behavioral')
                    | (df['Category'] == 'Introduction')]
    elif mode_select == 3:
        new_df = df[(df['Category'] != 'Data Science') &
                    (df['Category'] != 'Statistics')]
    else:
        new_df = df[df['Category'] != 'Behavioral']
    return new_df

def options_select():
    options = ''
    while options.lower() not in ('y', 'n'):
        options = input('Use default options? Y/N: ')
    if options.lower() == 'y':
        num_questions = 5
        follow_up_prob = 0
    else:
        num_questions = int(input('Enter number of questions: '))
        follow_up_prob = float(input(
            '\nNote: Some follow ups may not make sense\nEnter follow up question probability (0 to 1): '))
        if follow_up_prob > 1:
            follow_up_prob = follow_up_prob/100
            input('Greater than 1 detected. Converted to probability {}. Enter any key to continue: '.format(
                follow_up_prob))
    return num_questions, follow_up_prob

def ask_questions(Interview_df, num_questions, question_list = []):
    system('clear')
    first_question = np.random.choice(
        Interview_df[Interview_df['Category'] == 'Introduction']['Question'].values)
    questions = Interview_df[(Interview_df['Category'] != 'PROBES') &
                             (Interview_df['Category'] != 'Introduction')]['Question'].values
    Interview_questions = [first_question]
    Interview_questions.extend(random.sample(set(questions), num_questions - 1))
    for i, question in enumerate(Interview_questions):
        print('\n---------------------------------------------------------------------\n\n')
        question_list.append(question)
        print(question)
        probe = np.random.rand(1)[0]
        if len(question_list) > 1 and probe <= follow_up_prob:
            follow_up = np.random.choice(probe_q)
            question_list.append(follow_up)
            print(follow_up)
        print('\n\n---------------------------------------------------------------------')
        num_questions -= 1
        next = input('\n\nEnter any key for next question ({} Remaining): '.format(num_questions))
        system('clear')
        if next in ('quit', 'q', 'exit'):
            break
    return question_list

if __name__ == '__main__':
    Interview_df = import_question_db()
    probe_q = Interview_df[Interview_df['Category'] == 'PROBES']['Question'].values
    Interview_df = select_mode(Interview_df)
    num_questions, follow_up_prob = options_select()
    question_list = ask_questions(Interview_df, num_questions)

    print("\nQuestions Asked:\n---------------------------\n")
    for q in question_list:
        print(q)
    print('\n---------------------------')