import pandas as pd
# sncookie, fcookie, pcookie, tcookie
df = pd.read_csv('survey3_prolificpilot.csv')

# dictionaries that we need
participants_shown = {'Strictly Necessary': 0, 
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

sn1_dict = {
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
sn2_dict = {
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
fun1_dict = {'Strictly Necessary': 0, 
    'Necessary': 0,  
    'Performance': 0, 
    'Anonymous Analytics': 0, 
    'Aggregated Analytics': 0, 
    'Advertising': 0, 
    'Targeting': 0, 
    'Marketing': 0, 
    'Personalized Advertising': 0, 
    'Targeted Advertising': 0
    }
fun2_dict = {'Strictly Necessary': 0, 
    'Necessary': 0,  
    'Performance': 0, 
    'Anonymous Analytics': 0, 
    'Aggregated Analytics': 0, 
    'Advertising': 0, 
    'Targeting': 0, 
    'Marketing': 0, 
    'Personalized Advertising': 0, 
    'Targeted Advertising': 0
    }
fun3_dict = {'Strictly Necessary': 0, 
    'Necessary': 0,  
    'Performance': 0, 
    'Anonymous Analytics': 0, 
    'Aggregated Analytics': 0, 
    'Advertising': 0, 
    'Targeting': 0, 
    'Marketing': 0, 
    'Personalized Advertising': 0, 
    'Targeted Advertising': 0
    }
perf1_dict = {'Strictly Necessary': 0, 
    'Necessary': 0, 
    'Functional': 0, 
    'Personalization': 0, 
    'Preferences': 0, 
    'Personalized Experience': 0, 
    'Customization': 0, 
    'Advertising': 0, 
    'Targeting': 0, 
    'Marketing': 0, 
    'Personalized Advertising': 0, 
    'Targeted Advertising': 0
    }
perf2_dict = {'Strictly Necessary': 0, 
    'Necessary': 0, 
    'Functional': 0, 
    'Personalization': 0, 
    'Preferences': 0, 
    'Personalized Experience': 0, 
    'Customization': 0, 
    'Advertising': 0, 
    'Targeting': 0, 
    'Marketing': 0, 
    'Personalized Advertising': 0, 
    'Targeted Advertising': 0
    }
ad1_dict = {'Strictly Necessary': 0, 
    'Necessary': 0, 
    'Functional': 0, 
    'Personalization': 0, 
    'Preferences': 0, 
    'Personalized Experience': 0, 
    'Customization': 0, 
    'Performance': 0, 
    'Anonymous Analytics': 0, 
    'Aggregated Analytics': 0
    }
ad2_dict = {'Strictly Necessary': 0, 
    'Necessary': 0, 
    'Functional': 0, 
    'Personalization': 0, 
    'Preferences': 0, 
    'Personalized Experience': 0, 
    'Customization': 0, 
    'Performance': 0, 
    'Anonymous Analytics': 0, 
    'Aggregated Analytics': 0
    }

# need to make 9 data frames where each frame's rows correspond to all the possible terms that are the correct answer for that question
sn1_df = pd.DataFrame(0, ['Strictly Necessary', 'Necessary'], ['correct', 'incorrect'])
# print(sn1_df)
sn2_df = pd.DataFrame(0, ['Strictly Necessary', 'Necessary'], ['correct', 'incorrect'])

fun1_df = pd.DataFrame(0, ['Functional', 'Personalization', 'Preferences', 'Personalized Experience', 'Customization'], ['correct', 'incorrect'])
fun2_df = pd.DataFrame(0, ['Functional', 'Personalization', 'Preferences', 'Personalized Experience', 'Customization'], ['correct', 'incorrect'])
fun3_df = pd.DataFrame(0, ['Functional', 'Personalization', 'Preferences', 'Personalized Experience', 'Customization'], ['correct', 'incorrect'])

perf1_df = pd.DataFrame(0, ['Performance', 'Anonymous Analytics', 'Aggregated Analytics'], ['correct', 'incorrect'])
perf2_df = pd.DataFrame(0, ['Performance', 'Anonymous Analytics', 'Aggregated Analytics'], ['correct', 'incorrect'])

ad1_df = pd.DataFrame(0, ['Advertising', 'Targeting', 'Marketing', 'Personalized Advertising', 'Targeted Advertising'], ['correct', 'incorrect'])
ad2_df = pd.DataFrame(0, ['Advertising', 'Targeting', 'Marketing', 'Personalized Advertising', 'Targeted Advertising'], ['correct', 'incorrect'])

for index in df.index:
    # pull out what the cookie terms are
    sncookie = df.loc[index, 'sncookie']
    fcookie = df.loc[index, 'fcookie']
    pcookie = df.loc[index, 'pcookie']
    tcookie = df.loc[index, 'tcookie']

    # mark when the cookie has been shown
    participants_shown[sncookie] += 1
    participants_shown[fcookie] += 1
    participants_shown[pcookie] += 1
    participants_shown[tcookie] += 1

    # print(sncookie, fcookie, pcookie, tcookie)
    # print()
    # print(df.loc[index, 'Functional_1'])
    # print('index:', index, 'value: ', df.loc[index, 'Functional_1'])
    
    # getting the answers that participants put in
    stricly_necessary1_answer = df.loc[index, 'Strictly_Necessary_1'].split('}')[0].split('/')[-1]
    # need to do the correct check
    
    if stricly_necessary1_answer == 'sncookie':
        correct_count[sncookie] += 1
        sn1_df['correct'][sncookie] += 1
    elif stricly_necessary1_answer == 'fcookie':
        # so the first value is the column and the second value is the rows
        # this way, it's easier to pull values out
        incorrect_df[sncookie][fcookie] += 1
        sn1_df['incorrect'][sncookie] += 1
        sn1_dict[fcookie] += 1
    elif stricly_necessary1_answer == 'pcookie':
        incorrect_df[sncookie][pcookie] += 1
        sn1_df['incorrect'][sncookie] += 1
        sn1_dict[pcookie] += 1
    elif stricly_necessary1_answer == 'tcookie':
        incorrect_df[sncookie][tcookie] += 1
        sn1_df['incorrect'][sncookie] += 1
        sn1_dict[tcookie] += 1

    stricly_necessary2_answer = df.loc[index, 'Strictly_Necessary_2'].split('}')[0].split('/')[-1]
    if stricly_necessary2_answer == 'sncookie':
        correct_count[sncookie] += 1
        sn2_df['correct'][sncookie] += 1
    elif stricly_necessary2_answer == 'fcookie':
        incorrect_df[sncookie][fcookie] += 1
        sn2_df['incorrect'][sncookie] += 1
        sn2_dict[fcookie] += 1
    elif stricly_necessary2_answer == 'pcookie':
        incorrect_df[sncookie][pcookie] += 1
        sn2_df['incorrect'][sncookie] += 1
        sn2_dict[pcookie] += 1
    elif stricly_necessary2_answer == 'tcookie':
        incorrect_df[sncookie][tcookie] += 1
        sn2_df['incorrect'][sncookie] += 1
        sn2_dict[tcookie] += 1

    functional1_answer = df.loc[index, 'Functional_1'].split('}')[0].split('/')[-1]
    if functional1_answer == 'fcookie':
        correct_count[fcookie] += 1
        fun1_df['correct'][fcookie] += 1
    elif functional1_answer == 'sncookie':
        incorrect_df[fcookie][sncookie] += 1
        fun1_df['incorrect'][fcookie] += 1
        fun1_dict[sncookie] += 1
    elif functional1_answer == 'pcookie':
        incorrect_df[fcookie][pcookie] += 1
        fun1_df['incorrect'][fcookie] += 1
        fun1_dict[pcookie] += 1
    elif functional1_answer == 'tcookie':
        incorrect_df[fcookie][tcookie] += 1
        fun1_df['incorrect'][fcookie] += 1
        fun1_dict[tcookie] += 1
    
    functional2_answer = df.loc[index, 'Functional_2'].split('}')[0].split('/')[-1]
    if functional2_answer == 'fcookie':
        correct_count[fcookie] += 1
        fun2_df['correct'][fcookie] += 1
    elif functional2_answer == 'sncookie':
        incorrect_df[fcookie][sncookie] += 1
        fun2_df['incorrect'][fcookie] += 1
        fun2_dict[sncookie] += 1
    elif functional2_answer == 'pcookie':
        incorrect_df[fcookie][pcookie] += 1
        fun2_df['incorrect'][fcookie] += 1
        fun2_dict[pcookie] += 1
    elif functional2_answer == 'tcookie':
        incorrect_df[fcookie][tcookie] += 1
        fun2_df['incorrect'][fcookie] += 1
        fun2_dict[tcookie] += 1
    
    functional3_answer = df.loc[index, 'Functional_3'].split('}')[0].split('/')[-1]
    if functional3_answer == 'fcookie':
        correct_count[fcookie] += 1
        fun3_df['correct'][fcookie] += 1
    elif functional3_answer == 'sncookie':
        incorrect_df[fcookie][sncookie] += 1
        fun3_df['incorrect'][fcookie] += 1
        fun3_dict[sncookie] += 1
    elif functional3_answer == 'pcookie':
        incorrect_df[fcookie][pcookie] += 1
        fun3_df['incorrect'][fcookie] += 1
        fun3_dict[pcookie] += 1
    elif functional3_answer == 'tcookie':
        incorrect_df[fcookie][tcookie] += 1
        fun3_df['incorrect'][fcookie] += 1
        fun3_dict[tcookie] += 1

    performance1_answer = df.loc[index, 'Performance_1'].split('}')[0].split('/')[-1]
    if performance1_answer == 'pcookie':
        correct_count[pcookie] += 1
        perf1_df['correct'][pcookie] += 1
    elif performance1_answer == 'sncookie':
        incorrect_df[pcookie][sncookie] += 1
        perf1_df['incorrect'][pcookie] += 1
        perf1_dict[sncookie] += 1
    elif performance1_answer == 'fcookie':
        incorrect_df[pcookie][fcookie] += 1
        perf1_df['incorrect'][pcookie] += 1
        perf1_dict[fcookie] += 1
    elif performance1_answer == 'tcookie':
        incorrect_df[pcookie][tcookie] += 1
        perf1_df['incorrect'][pcookie] += 1
        perf1_dict[tcookie] += 1

    performance2_answer = df.loc[index, 'Performance_2'].split('}')[0].split('/')[-1]
    if performance2_answer == 'pcookie':
        correct_count[pcookie] += 1
        perf2_df['correct'][pcookie] += 1
    elif performance2_answer == 'sncookie':
        incorrect_df[pcookie][sncookie] += 1
        perf2_df['incorrect'][pcookie] += 1
        perf2_dict[sncookie] += 1
    elif performance2_answer == 'fcookie':
        incorrect_df[pcookie][fcookie] += 1
        perf2_df['incorrect'][pcookie] += 1
        perf2_dict[fcookie] += 1
    elif performance2_answer == 'tcookie':
        incorrect_df[pcookie][tcookie] += 1
        perf2_df['incorrect'][pcookie] += 1
        perf2_dict[tcookie] += 1

    advertising1_answer = df.loc[index, 'Advertising_1'].split('}')[0].split('/')[-1]
    if advertising1_answer == 'tcookie':
        correct_count[tcookie] += 1
        ad1_df['correct'][tcookie] += 1
    elif advertising1_answer == 'sncookie':
        incorrect_df[tcookie][sncookie] += 1
        ad1_df['incorrect'][tcookie] += 1
        ad1_dict[sncookie] += 1
    elif advertising1_answer == 'fcookie':
        incorrect_df[tcookie][fcookie] += 1
        ad1_df['incorrect'][tcookie] += 1
        ad1_dict[fcookie] += 1
    elif advertising1_answer == 'pcookie':
        incorrect_df[tcookie][pcookie] += 1
        ad1_df['incorrect'][tcookie] += 1
        ad1_dict[pcookie] += 1

    advertising2_answer = df.loc[index, 'Advertising_2'].split('}')[0].split('/')[-1]
    if advertising2_answer == 'tcookie':
        correct_count[tcookie] += 1
        ad2_df['correct'][tcookie] += 1
    elif advertising2_answer == 'sncookie':
        incorrect_df[tcookie][sncookie] += 1
        ad2_df['incorrect'][tcookie] += 1
        ad2_dict[sncookie] += 1
    elif advertising2_answer == 'fcookie':
        incorrect_df[tcookie][fcookie] += 1
        ad2_df['incorrect'][tcookie] += 1
        ad2_dict[fcookie] += 1
    elif advertising2_answer == 'pcookie':
        incorrect_df[tcookie][pcookie] += 1
        ad2_df['incorrect'][tcookie] += 1
        ad2_dict[pcookie] += 1
    
    # print(stricly_necessary1_answer, stricly_necessary2_answer)
    # print(functional1_answer, functional2_answer, functional3_answer)
    # print(performance1_answer, performance2_answer)
    # print(advertising1_answer, advertising2_answer)
    # print('\n')

print("Amount of participants shown cookie:", participants_shown, "\n")
print("Correctly chosen answer:", correct_count)
# print(incorrect_df)
incorrect_df.to_csv('incorrect_answers.csv')
print()
# to get the number of times the answer was correct, we do # times it was correct / # times it was shown
print("Strictly necessary correct", correct_count['Strictly Necessary'] / (participants_shown['Strictly Necessary'] * 2) * 100, "% of the time")
print("Necessary correct", correct_count['Necessary'] / (participants_shown['Necessary'] * 2) * 100, "% of the time")

print("Functional correct", correct_count['Functional'] / (participants_shown['Functional'] * 3) * 100, "% of the time")
print("Personalization correct", (correct_count['Personalization'] / (participants_shown['Personalization'] * 3)) * 100, "% of the time")
print("Preferences correct", (correct_count['Preferences'] / (participants_shown['Preferences'] * 3)) * 100, "% of the time")
print("Personalized Experience correct", (correct_count['Personalized Experience'] / (participants_shown['Personalized Experience'] * 3)) * 100, "% of the time")
print("Customization correct", (correct_count['Customization'] / (participants_shown['Customization'] * 3)) * 100, "% of the time")

print("Performance correct", (correct_count['Performance'] / (participants_shown['Performance'] * 2)) * 100, "% of the time")
print("Anonymous Analytics correct", (correct_count['Anonymous Analytics'] / (participants_shown['Anonymous Analytics'] * 2)) * 100, "% of the time")
print("Aggregated Analytics correct", (correct_count['Aggregated Analytics'] / (participants_shown['Aggregated Analytics'] * 2)) * 100, "% of the time")

print("Advertising correct", (correct_count['Advertising'] / (participants_shown['Advertising'] * 2)) * 100, "% of the time")
print("Targeting correct", (correct_count['Targeting'] / (participants_shown['Targeting'] * 2)) * 100, "% of the time")
print("Marketing correct", (correct_count['Marketing'] / (participants_shown['Marketing'] * 2)) * 100, "% of the time")
print("Personalized Advertising correct", (correct_count['Personalized Advertising'] / (participants_shown['Personalized Advertising'] * 2)) * 100, "% of the time")
print("Targeted Advertising correct", (correct_count['Targeted Advertising'] / (participants_shown['Targeted Advertising'] * 2)) * 100, "% of the time")

print()
print()

sn1_df.to_csv('Strictly_Necessary_1.csv')
sn2_df.to_csv('Strictly_Necessary_2.csv')
print("Strictly necessary 1 incorrect options: ", sn1_dict, '\n')
print("Strictly necessary 2 incorrect options: ", sn2_dict, '\n')

print()
print()
fun1_df.to_csv('Functional_1.csv')
fun2_df.to_csv('Functional_2.csv')
fun3_df.to_csv('Functional_3.csv')
print("Functional 1 incorrect options: ", fun1_dict, '\n')
print("Functional 2 incorrect options: ", fun2_dict, '\n')
print("Functional 3 incorrect options: ", fun3_dict, '\n')

# perf1_df['incorrectly_selected'] = pd.Series(perf1_dict)
# perf2_df['incorrectly_selected'] = pd.Series(perf2_dict)
perf1_df.to_csv('Performance_1.csv')
perf2_df.to_csv('Performance_2.csv')
print()
print()
print("Performance 1 incorrect options: ", perf1_dict, '\n')
print("Performance 2 incorrect options: ", perf2_dict, '\n')

# ad1_df['incorrectly_selected'] = pd.Series(ad1_dict)
# ad2_df['incorrectly_selected'] = pd.Series(ad2_dict)
ad1_df.to_csv('Advertising_1.csv')
ad2_df.to_csv('Advertising_2.csv')
print()
print()
print("Advertising 1 incorrect options: ", ad1_dict, '\n')
print("Advertising 2 incorrect options: ", ad2_dict, '\n')


# matplotlib barh
