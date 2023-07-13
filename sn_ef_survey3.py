import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('test-python.csv')

# dictionaries that we need
participants_shown = {'Strictly Necessary': 0, 
    'Extra Functionality': 0
    }

correct_count = {'Strictly Necessary': 0,
    'Extra Functionality': 0}

incorrect_count = {'Strictly Necessary': 0,
    'Extra Functionality': 0}

# we need to look at each row and see which cookie category they selected
# print(list(df.columns.values))
# print(df["sncookie"])
# print(df)

row_indices = ['Strictly Necessary', 'Extra Functionality']
col_indices = ['Strictly Necessary', 'Extra Functionality']
incorrect_df = pd.DataFrame(0, row_indices, col_indices)
# print(result_df)

sn1_dict = {'Extra Functionality': 0,}
sn2_dict = {'Extra Functionality': 0}
fun1_dict = {'Strictly Necessary': 0}
fun2_dict = {'Strictly Necessary': 0}
fun3_dict = {'Strictly Necessary': 0}
# need to make 9 data frames where each frame's rows correspond to all the possible terms that are the correct answer for that question
sn1_df = pd.DataFrame(0, ['Strictly Necessary'], ['correct', 'incorrect'])
sn2_df = pd.DataFrame(0, ['Strictly Necessary'], ['correct', 'incorrect'])

fun1_df = pd.DataFrame(0, ['Extra Functionality'], ['correct', 'incorrect'])
fun2_df = pd.DataFrame(0, ['Extra Functionality'], ['correct', 'incorrect'])
fun3_df = pd.DataFrame(0, ['Extra Functionality'], ['correct', 'incorrect'])

sncookie = 'Strictly Necessary'
fcookie = 'Extra Functionality'

print()
print()

for index in df.index:
    # pull out what the cookie terms are
    # sncookie = df.loc[index, 'sncookie']
    # fcookie = df.loc[index, 'fcookie']

    # mark when the cookie has been shown
    participants_shown[sncookie] += 1
    participants_shown[fcookie] += 1
    
    # getting the answers that participants put in
    stricly_necessary1_answer = df.loc[index, 'Strictly_Necessary_1'].split('}')[0].split('/')[-1]
    # need to do the correct check
    # print()
    # print(index)
    # print(sncookie)
    # print(stricly_necessary1_answer)
    # print()

    if stricly_necessary1_answer == sncookie:
        correct_count[sncookie] += 1
        sn1_df['correct'][sncookie] += 1
    elif stricly_necessary1_answer == fcookie:
        # so the first value is the column and the second value is the rows
        # this way, it's easier to pull values out
        incorrect_count[fcookie] +=1 
        incorrect_df[sncookie][fcookie] += 1
        sn1_df['incorrect'][sncookie] += 1
        sn1_dict[fcookie] += 1

    stricly_necessary2_answer = df.loc[index, 'Strictly_Necessary_2'].split('}')[0].split('/')[-1]
    if stricly_necessary2_answer == sncookie:
        correct_count[sncookie] += 1
        sn2_df['correct'][sncookie] += 1
    elif stricly_necessary2_answer == fcookie:
        incorrect_count[fcookie] +=1 
        incorrect_df[sncookie][fcookie] += 1
        sn2_df['incorrect'][sncookie] += 1
        sn2_dict[fcookie] += 1

    functional1_answer = df.loc[index, 'Functional_1'].split('}')[0].split('/')[-1]
    if functional1_answer == fcookie:
        correct_count[fcookie] += 1
        fun1_df['correct'][fcookie] += 1
    elif functional1_answer == sncookie:
        incorrect_count[sncookie] +=1 
        incorrect_df[fcookie][sncookie] += 1
        fun1_df['incorrect'][fcookie] += 1
        fun1_dict[sncookie] += 1
    
    functional2_answer = df.loc[index, 'Functional_2'].split('}')[0].split('/')[-1]
    if functional2_answer == fcookie:
        correct_count[fcookie] += 1
        fun2_df['correct'][fcookie] += 1
    elif functional2_answer == sncookie:
        incorrect_count[sncookie] +=1
        incorrect_df[fcookie][sncookie] += 1
        fun2_df['incorrect'][fcookie] += 1
        fun2_dict[sncookie] += 1
    
    functional3_answer = df.loc[index, 'Functional_3'].split('}')[0].split('/')[-1]
    if functional3_answer == fcookie:
        correct_count[fcookie] += 1
        fun3_df['correct'][fcookie] += 1
    elif functional3_answer == sncookie:
        incorrect_count[sncookie] +=1
        incorrect_df[fcookie][sncookie] += 1
        fun3_df['incorrect'][fcookie] += 1
        fun3_dict[sncookie] += 1


print()
print()
print("Amount of participants shown cookie:", participants_shown, "\n")
print("Correctly chosen answer:", correct_count)
print()
# print(incorrect_df)
# incorrect_df.to_csv('incorrect_answers.csv')
print()
# to get the number of times the answer was correct, we do # times it was correct / # times it was shown
s_n_percent = correct_count['Strictly Necessary'] / (participants_shown['Strictly Necessary'] * 2)
print("Strictly necessary correct", str("{:.2%}".format(s_n_percent)), "% of the time")
s_n_percent = incorrect_count['Strictly Necessary'] / (participants_shown['Strictly Necessary'] * 2)
print("Strictly necessary incorrect", str("{:.2%}".format(s_n_percent)), "% of the time")


functional_percent = correct_count['Extra Functionality'] / (participants_shown['Extra Functionality'] * 3)
print("Extra Functionality correct", str("{:.2%}".format(functional_percent)), "% of the time")
functional_percent = incorrect_count['Extra Functionality'] / (participants_shown['Extra Functionality'] * 3)
print("Extra Functionality incorrect", str("{:.2%}".format(functional_percent)), "% of the time")

print()
print()

print('--------------------------------------------------------------------------------------------------------------------------------------------------')

# print("Strictly Necessary Q1: Imagine that you are browsing an online clothing store for the first time. You see a couple of pieces of clothing that you are interested in, which you start adding to your shopping cart without creating an account on the website. Which of the following cookies do you believe helps the website remember the contents of your online shopping cart?")
sn_correct_percent = sn1_df['correct']['Strictly Necessary'] / participants_shown['Strictly Necessary']
print('Strictly necessary in SN_Q1 was correctly chosen', str("{:.2%}".format(sn_correct_percent)))

print()
incorrect_percent = (sn1_dict[fcookie] / participants_shown[fcookie])
print(fcookie, "in SN_Q1 was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

print()
print('--------------------------------------------------------------------------------------------------------------------------------------------------')

# print("Strictly Necessary Q2: You visit a community events bulletin website for the first time and are greeted with a cookie banner. You can either allow or prevent the website from placing cookies on your browser. You decide to 'Decline' the website's request to set cookies and continue browsing the various events. The next week you return to the website to confirm the details of a particular event. You no longer see the cookie banner. Which of the following cookies do you think helps the website remember that you have already set your cookie settings?")
sn2_correct_percent = sn2_df['correct']['Strictly Necessary'] / participants_shown['Strictly Necessary']
print('Strictly necessary in SN_Q2 was correctly chosen', str("{:.2%}".format(sn2_correct_percent)))

print()
incorrect_percent = (sn2_dict[fcookie] / participants_shown[fcookie])
print(fcookie, "in SN_Q2 was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))


print('--------------------------------------------------------------------------------------------------------------------------------------------------')
# print("Functional Q1: You open an online shopping website and you select “Decline all cookies”. You start looking at different products on the website, and notice that reviews aren’t loading properly. Which cookies would allow for the reviews to load?")
func_correct_percent = fun1_df['correct']['Extra Functionality'] / participants_shown['Extra Functionality']
print()
print('Extra Functionality in F_Q1 was correctly chosen', str("{:.2%}".format(func_correct_percent)))

print()
incorrect_percent = (fun1_dict[sncookie] / participants_shown[sncookie])
print(sncookie, "in F_Q1 was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

print()

print('--------------------------------------------------------------------------------------------------------------------------------------------------')
# print("Functional Q2: You are having trouble with your internet service provider and visit their webpage to look for a solution. You see that they have the option of starting an online conversation with one of their agents through the website’s chat bot feature. Which of the following cookies would you want to turn on so that you can access the chat bot on the page?")
func2_correct_percent = fun2_df['correct']['Extra Functionality'] / participants_shown['Extra Functionality']
print()
print('Extra Functionality in F_Q2 was correctly chosen', str("{:.2%}".format(func2_correct_percent)))

print()
incorrect_percent = (fun2_dict[sncookie] / participants_shown[sncookie])
print(sncookie, "in F_Q2 was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

print()

print('--------------------------------------------------------------------------------------------------------------------------------------------------')
# print("Functional Q3: You visit a graphic design website to design posters for an event and accept all cookies on the website’s cookie banner. The first time you visit the website you are greeted with an optional short tutorial that guides you on how to use the platform effectively. You step through the tutorial and dismiss it once you’ve completed it. After you are done working for the day, you close your browser window. When revisiting the website the next day, you see that the tutorial is no longer offered to you. Which cookie remembers that you have already seen the tutorial and knows not to offer it to you again?")
func3_correct_percent = fun3_df['correct']['Extra Functionality'] / participants_shown['Extra Functionality']
print()
print('Extra Functionality in F_Q3 was correctly chosen', str("{:.2%}".format(func3_correct_percent)))

print()
incorrect_percent = (fun3_dict[sncookie] / participants_shown[sncookie])
print(sncookie, "in F_Q3 was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

print()

print()