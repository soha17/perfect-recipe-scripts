import pandas as pd

def rewrite(df, index, current_question, sncookie, fcookie, pcookie, tcookie):
    if df.loc[index, current_question] == '${e://Field/sncookie} Cookies':
        df.loc[index, current_question] = sncookie
    elif df.loc[index, current_question] == '${e://Field/fcookie} Cookies':
       df.loc[index, current_question] = fcookie
    elif df.loc[index, current_question] == '${e://Field/pcookie} Cookies':
        df.loc[index, current_question] = pcookie
    elif df.loc[index, current_question] == '${e://Field/tcookie} Cookies':
        df.loc[index, current_question] = tcookie

# this method will give us a row x column data structure (row = each answer; col = each question)
def replace_with_term():
    df = pd.read_csv('s3_run2.csv')
    for index in df.index:
    # pull out what the cookie terms the participants saw
        sncookie = df.loc[index, 'sncookie']
        fcookie = df.loc[index, 'fcookie']
        pcookie = df.loc[index, 'pcookie']
        tcookie = df.loc[index, 'tcookie']

        rewrite(df, index, 'Strictly_Necessary_1', sncookie, fcookie, pcookie, tcookie)
        rewrite(df, index, 'Strictly_Necessary_2', sncookie, fcookie, pcookie, tcookie)
        rewrite(df, index, 'Functional_1', sncookie, fcookie, pcookie, tcookie)
        rewrite(df, index, 'Functional_2', sncookie, fcookie, pcookie, tcookie)
        rewrite(df, index, 'Functional_3', sncookie, fcookie, pcookie, tcookie)
        rewrite(df, index, 'Performance_1', sncookie, fcookie, pcookie, tcookie)
        rewrite(df, index, 'Performance_2', sncookie, fcookie, pcookie, tcookie)
        rewrite(df, index, 'Advertising_1', sncookie, fcookie, pcookie, tcookie)
        rewrite(df, index, 'Advertising_2', sncookie, fcookie, pcookie, tcookie)

    # print out replaced terms in csv file
    # df.to_csv("s3_replaced_terms.csv")
def get_counts():
    # dictionary that stores how many participants saw each term
    participants_shown = {
    'Strictly Necessary': 0, 
    'Necessary': 0, 
    'Functional': 0, 
    'Personalization': 0, 
    'Preferences': 0, 
    'Personalized Experience': 0,
    'Extra Functionality': 0,
    'Functionality': 0,    
    'Customization': 0, 
    'Performance': 0, 
    'Anonymous Analytics': 0, 
    'Advertising': 0, 
    'Personalized Advertising': 0
    }

    # making a dictionary where rows are each of the term and columns are each question
    row_indices = ['Strictly Necessary', 'Necessary', 'Functional', 'Functionality', 'Extra Functionality', 'Personalization', 'Preferences', 'Personalized Experience', 'Customization', 'Performance', 'Anonymous Analytics', 'Advertising', 'Personalized Advertising']
    col_indices = ['Strictly_Necessary_1', 'Strictly_Necessary_2', 'Performance_1', 'Performance_2', 'Functional_1', 'Functional_2', 'Functional_3', 'Advertising_1', 'Advertising_2']
    answer_percentages = pd.DataFrame(0, row_indices, col_indices)
    
    df = pd.read_csv('s3_replaced_terms.csv')
    # filling the answer count dataframes
    for index in df.index:
    # pull out what the cookie terms the participants saw
        sncookie = df.loc[index, 'sncookie']
        fcookie = df.loc[index, 'fcookie']
        pcookie = df.loc[index, 'pcookie']
        tcookie = df.loc[index, 'tcookie']

        # update counts for how many terms were seen
        participants_shown[sncookie] += 1
        participants_shown[fcookie] += 1
        participants_shown[pcookie] += 1
        participants_shown[tcookie] += 1

        # now change counts for terms chosen 
        answer = df.loc[index, 'Strictly_Necessary_1']
        answer_percentages.loc[answer, 'Strictly_Necessary_1'] += 1
        answer = df.loc[index, 'Strictly_Necessary_2']
        answer_percentages.loc[answer, 'Strictly_Necessary_2'] += 1

        answer = df.loc[index, 'Functional_1']
        answer_percentages.loc[answer, 'Functional_1'] += 1
        answer = df.loc[index, 'Functional_2']
        answer_percentages.loc[answer, 'Functional_2'] += 1
        answer = df.loc[index, 'Functional_3']
        answer_percentages.loc[answer, 'Functional_3'] += 1

        answer = df.loc[index, 'Performance_1']
        answer_percentages.loc[answer, 'Performance_1'] += 1
        answer = df.loc[index, 'Performance_2']
        answer_percentages.loc[answer, 'Performance_2'] += 1

        answer = df.loc[index, 'Advertising_1']
        answer_percentages.loc[answer, 'Advertising_1'] += 1
        answer = df.loc[index, 'Advertising_2']
        answer_percentages.loc[answer, 'Advertising_2'] += 1

    for index in answer_percentages.index:
        # now need to set the percentages = # times chosen / # people it was shown to 
        percent = answer_percentages.loc[index, 'Strictly_Necessary_1'] / participants_shown[index]
        answer_percentages.loc[index, 'Strictly_Necessary_1'] = str("{:.2%}".format(percent))
        percent = answer_percentages.loc[index, 'Strictly_Necessary_2'] / participants_shown[index]
        answer_percentages.loc[index, 'Strictly_Necessary_2'] = str("{:.2%}".format(percent))
        percent = answer_percentages.loc[index, 'Functional_1'] / participants_shown[index]
        answer_percentages.loc[index, 'Functional_1'] = str("{:.2%}".format(percent))
        percent = answer_percentages.loc[index, 'Functional_2'] / participants_shown[index]
        answer_percentages.loc[index, 'Functional_2'] = str("{:.2%}".format(percent))
        percent = answer_percentages.loc[index, 'Functional_3'] / participants_shown[index]
        answer_percentages.loc[index, 'Functional_3'] = str("{:.2%}".format(percent))
        percent = answer_percentages.loc[index, 'Performance_1'] / participants_shown[index]
        answer_percentages.loc[index, 'Performance_1'] = str("{:.2%}".format(percent))
        percent = answer_percentages.loc[index, 'Performance_2'] / participants_shown[index]
        answer_percentages.loc[index, 'Performance_2'] = str("{:.2%}".format(percent))
        percent = answer_percentages.loc[index, 'Advertising_1'] / participants_shown[index]
        answer_percentages.loc[index, 'Advertising_1'] = str("{:.2%}".format(percent))
        percent = answer_percentages.loc[index, 'Advertising_2'] / participants_shown[index]
        answer_percentages.loc[index, 'Advertising_2'] = str("{:.2%}".format(percent))
        

        # print(answer_percentages.loc[index, 'Strictly_Necessary_1'])
        # print(index)
        # str("{:.2%}".format(count))


    print("Amount of participants shown cookie:", participants_shown, '\n')
    print(answer_percentages)
    answer_percentages.to_csv("answer_percents.csv")

# replace_with_term()
get_counts()