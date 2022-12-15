import pandas as pd
# sncookie, fcookie, pcookie, tcookie
df = pd.read_csv('survey3_pilot.csv')

sncookie_correct = 0
fcookie_correct = 0
pcookie_correct = 0
tcookie_correct = 0

correct_count = {'Strictly Necessary': 0, 
    'Necessary': 0, 
    'Functional': 0, 
    'Personalization': 0, 
    'Preferences': 0, 
    'Personalized Experience': 0, 
    'Customization': 0, 
    'Performance': 0, 
    'Anonymous Analytics': 0, 
    'Aggregated Analytics': 0, 
    'Advertising': 0, 
    'Targeting': 0, 
    'Marketing': 0, 
    'Personalized Advertising': 0, 
    'Targeted Advertising': 0
    }

# we need to look at each row and see which cookie category they selected
# print(list(df.columns.values))
# print(df["sncookie"])
# print(df)

row_indices = ['Strictly Necessary', 'Necessary', 'Functional', 'Personalization', 'Preferences', 'Personalized Experience', 'Customization', 'Performance', 'Anonymous Analytics', 'Aggregated Analytics', 'Advertising', 'Targeting', 'Marketing', 'Personalized Advertising', 'Targeted Advertising']
col_indices = ['Strictly Necessary', 'Necessary', 'Functional', 'Personalization', 'Preferences', 'Personalized Experience', 'Customization', 'Performance', 'Anonymous Analytics', 'Aggregated Analytics', 'Advertising', 'Targeting', 'Marketing', 'Personalized Advertising', 'Targeted Advertising']
incorrect_df = pd.DataFrame(0, row_indices, col_indices)
# print(result_df)

for index in df.index:
    # pull out what the cookie terms are
    sncookie = df.loc[index, 'sncookie']
    fcookie = df.loc[index, 'fcookie']
    pcookie = df.loc[index, 'pcookie']
    tcookie = df.loc[index, 'tcookie']
    # print(sncookie, fcookie, pcookie, tcookie)
    # print()
    # print(df.loc[index, 'Functional_1'])
    # we need to do a regex matching thing
    # never mind we're doing split
    # print('index:', index, 'value: ', df.loc[index, 'Functional_1'])
    
    # getting the answers that participants put in
    stricly_necessary1_answer = df.loc[index, 'Strictly_Necessary_1'].split('}')[0].split('/')[-1]
    # need to do the correct check
    if stricly_necessary1_answer == 'sncookie':
        correct_count[sncookie] += 1
    elif stricly_necessary1_answer == 'fcookie':
        # so the first value is the column and the second value is the rows
        # this way, it's easier to pull values out
        incorrect_df[sncookie][fcookie] += 1
    elif stricly_necessary1_answer == 'pcookie':
        incorrect_df[sncookie][pcookie] += 1
    elif stricly_necessary1_answer == 'tcookie':
        incorrect_df[sncookie][tcookie] += 1

    stricly_necessary2_answer = df.loc[index, 'Strictly_Necessary_2'].split('}')[0].split('/')[-1]
    if stricly_necessary2_answer == 'sncookie':
        correct_count[sncookie] += 1
    elif stricly_necessary2_answer == 'fcookie':
        # so the first value is the correct answer/col and the second value is the incorrect/row
        # this way, it's easier to pull values out
        incorrect_df[sncookie][fcookie] += 1
    elif stricly_necessary2_answer == 'pcookie':
        incorrect_df[sncookie][pcookie] += 1
    elif stricly_necessary2_answer == 'tcookie':
        incorrect_df[sncookie][tcookie] += 1

    functional1_answer = df.loc[index, 'Functional_1'].split('}')[0].split('/')[-1]
    if functional1_answer == 'fcookie':
        correct_count[fcookie] += 1
    elif functional1_answer == 'sncookie':
        incorrect_df[fcookie][sncookie] += 1
    elif functional1_answer == 'pcookie':
        incorrect_df[fcookie][pcookie] += 1
    elif functional1_answer == 'tcookie':
        incorrect_df[fcookie][tcookie] += 1
    
    functional2_answer = df.loc[index, 'Functional_2'].split('}')[0].split('/')[-1]
    if functional2_answer == 'fcookie':
        correct_count[fcookie] += 1
    elif functional2_answer == 'sncookie':
        incorrect_df[fcookie][sncookie] += 1
    elif functional2_answer == 'pcookie':
        incorrect_df[fcookie][pcookie] += 1
    elif functional2_answer == 'tcookie':
        incorrect_df[fcookie][tcookie] += 1
    
    functional3_answer = df.loc[index, 'Functional_3'].split('}')[0].split('/')[-1]
    if functional3_answer == 'fcookie':
        correct_count[fcookie] += 1
    elif functional3_answer == 'sncookie':
        incorrect_df[fcookie][sncookie] += 1
    elif functional3_answer == 'pcookie':
        incorrect_df[fcookie][pcookie] += 1
    elif functional3_answer == 'tcookie':
        incorrect_df[fcookie][tcookie] += 1

    performance1_answer = df.loc[index, 'Performance_1'].split('}')[0].split('/')[-1]
    if performance1_answer == 'pcookie':
        correct_count[pcookie] += 1
    elif performance1_answer == 'sncookie':
        incorrect_df[pcookie][sncookie] += 1
    elif performance1_answer == 'fcookie':
        incorrect_df[pcookie][fcookie] += 1
    elif performance1_answer == 'tcookie':
        incorrect_df[pcookie][tcookie] += 1

    performance2_answer = df.loc[index, 'Performance_2'].split('}')[0].split('/')[-1]
    if performance2_answer == 'pcookie':
        correct_count[pcookie] += 1
    elif performance2_answer == 'sncookie':
        incorrect_df[pcookie][sncookie] += 1
    elif performance2_answer == 'fcookie':
        incorrect_df[pcookie][fcookie] += 1
    elif performance2_answer == 'tcookie':
        incorrect_df[pcookie][tcookie] += 1

    advertising1_answer = df.loc[index, 'Advertising_1'].split('}')[0].split('/')[-1]
    if advertising1_answer == 'tcookie':
        correct_count[tcookie] += 1
    elif advertising1_answer == 'sncookie':
        incorrect_df[tcookie][sncookie] += 1
    elif advertising1_answer == 'fcookie':
        incorrect_df[tcookie][fcookie] += 1
    elif advertising1_answer == 'pcookie':
        incorrect_df[tcookie][pcookie] += 1

    advertising2_answer = df.loc[index, 'Advertising_2'].split('}')[0].split('/')[-1]
    if advertising2_answer == 'tcookie':
        correct_count[tcookie] += 1
    elif advertising2_answer == 'sncookie':
        incorrect_df[tcookie][sncookie] += 1
    elif advertising2_answer == 'fcookie':
        incorrect_df[tcookie][fcookie] += 1
    elif advertising2_answer == 'pcookie':
        incorrect_df[tcookie][pcookie] += 1
    
    # print(stricly_necessary1_answer, stricly_necessary2_answer)
    # print(functional1_answer, functional2_answer, functional3_answer)
    # print(performance1_answer, performance2_answer)
    # print(advertising1_answer, advertising2_answer)
    # print('\n')

# so this will print the "Strictly Necessary" Column - this will give us the amount of times ppl selected
# other options over the correct answer (Strictly Necessary)
# print(incorrect_df["Strictly Necessary"])
# print(correct_count)

print(correct_count)
print(incorrect_df)
incorrect_df.to_csv('incorrect_answers.csv')