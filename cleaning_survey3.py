import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# sncookie, fcookie, pcookie, tcookie
df = pd.read_csv('fullsurvey.csv')

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
s_n_percent = correct_count['Strictly Necessary'] / (participants_shown['Strictly Necessary'] * 2)
print("Strictly necessary correct", s_n_percent, "% of the time")
nec_percent = correct_count['Necessary'] / (participants_shown['Necessary'] * 2)
print("Necessary correct", nec_percent, "% of the time")
# x = np.array(["Strictly Necessary", "Necessary"])
# y = np.array([s_n_percent, nec_percent])
 
# plt.barh(x, y)

# plt.show()

# plt.rcdefaults()
# fig, ax = plt.subplots()
# c1_terms = ('Strictly Necessary', 'Necessary')
# y_pos = np.arange(len(c1_terms))
# c1_percents = (s_n_percent, nec_percent)
# ax.barh(y_pos, c1_percents,  align='center')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(c1_terms)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Percentage for correctness')
# ax.set_title('How often was a term chosen when it was the correct answer?')
# for i,val in enumerate(c1_percents):
#     ax.text(val, i, str("{:.2%}".format(val)), color="b", fontsize=10)
# plt.show()

functional_percent = correct_count['Functional'] / (participants_shown['Functional'] * 3)
personalization_percent = (correct_count['Personalization'] / (participants_shown['Personalization'] * 3))
prefs_percent = (correct_count['Preferences'] / (participants_shown['Preferences'] * 3))
p_ex_percent = (correct_count['Personalized Experience'] / (participants_shown['Personalized Experience'] * 3))
cus_percent = (correct_count['Customization'] / (participants_shown['Customization'] * 3))
print("Functional correct", functional_percent, "% of the time")
print("Personalization correct", personalization_percent * 100, "% of the time")
print("Preferences correct", prefs_percent * 100, "% of the time")
print("Personalized Experience correct", p_ex_percent * 100, "% of the time")
print("Customization correct", cus_percent * 100, "% of the time")
# plt.rcdefaults()
# fig, ax = plt.subplots()
# c2_terms = ('Functional', 'Personalization', 'Preferences', 'Personalized Experience', 'Customization')
# y_pos = np.arange(len(c2_terms))
# p_ex_percent = (correct_count['Personalized Experience'] / (participants_shown['Personalized Experience'] * 3))
# c2_percents = (functional_percent, personalization_percent, prefs_percent, p_ex_percent, cus_percent)
# ax.barh(y_pos, c2_percents,  align='center')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(c2_terms)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Percentage for correctness')
# ax.set_title('How often was a term chosen when it was the correct answer?')
# for i,val in enumerate(c2_percents):
#     ax.text(val, i, str("{:.2%}".format(val)), color="b", fontsize=10)
# plt.show()

perf_percent = (correct_count['Performance'] / (participants_shown['Performance'] * 2))
anon_an_percent = (correct_count['Anonymous Analytics'] / (participants_shown['Anonymous Analytics'] * 2))
agg_an_percent = (correct_count['Aggregated Analytics'] / (participants_shown['Aggregated Analytics'] * 2))
print("Performance correct", perf_percent * 100, "% of the time")
print("Anonymous Analytics correct", anon_an_percent * 100, "% of the time")
print("Aggregated Analytics correct", agg_an_percent * 100, "% of the time")
# plt.rcdefaults()
# fig, ax = plt.subplots()
# c3_terms = ('Performance', 'Anonymous Analytics', 'Aggregated Analytics')
# y_pos = np.arange(len(c3_terms))
# c3_percents = (perf_percent, anon_an_percent, agg_an_percent)
# ax.barh(y_pos, c3_percents,  align='center')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(c3_terms)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Percentage for correctness')
# ax.set_title('How often was a term chosen when it was the correct answer?')
# for i,val in enumerate(c3_percents):
#     ax.text(val, i, str("{:.2%}".format(val)), color="b", fontsize=10)
# plt.show()

# ad_perc = (correct_count['Advertising'] / (participants_shown['Advertising'] * 2))
# targ_perc = (correct_count['Targeting'] / (participants_shown['Targeting'] * 2))
# marketing_perc = (correct_count['Marketing'] / (participants_shown['Marketing'] * 2))
# p_ad_perc = (correct_count['Personalized Advertising'] / (participants_shown['Personalized Advertising'] * 2))
# t_ad_perc = (correct_count['Targeted Advertising'] / (participants_shown['Targeted Advertising'] * 2))
# print("Advertising correct", ad_perc * 100, "% of the time")
# print("Targeting correct", targ_perc * 100, "% of the time")
# print("Marketing correct", marketing_perc * 100, "% of the time")
# print("Personalized Advertising correct", p_ad_perc * 100, "% of the time")
# print("Targeted Advertising correct", t_ad_perc * 100, "% of the time")
# plt.rcdefaults()
# fig, ax = plt.subplots()
# c4_terms = ('Advertising', 'Targeting', 'Marketing', 'Personalized Advertising', 'Targeted Advertising')
# y_pos = np.arange(len(c4_terms))
# c4_percents = (ad_perc, targ_perc, marketing_perc, p_ad_perc, t_ad_perc)
# ax.barh(y_pos, c4_percents,  align='center')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(c4_terms)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Percentage for correctness')
# ax.set_title('How often was a term chosen when it was the correct answer?')
# for i,val in enumerate(c4_percents):
#     ax.text(val, i, str("{:.2%}".format(val)), color="b", fontsize=10)
# plt.show()

# print()
# print()

# sn1_df.to_csv('Strictly_Necessary_1.csv')
# sn2_df.to_csv('Strictly_Necessary_2.csv')
# print("Strictly necessary 1 incorrect options: ", sn1_dict, '\n')
# print("Strictly necessary 2 incorrect options: ", sn2_dict, '\n')

# print()
# print()
# fun1_df.to_csv('Functional_1.csv')
# fun2_df.to_csv('Functional_2.csv')
# fun3_df.to_csv('Functional_3.csv')
# print("Functional 1 incorrect options: ", fun1_dict, '\n')
# print("Functional 2 incorrect options: ", fun2_dict, '\n')
# print("Functional 3 incorrect options: ", fun3_dict, '\n')

# perf1_df['incorrectly_selected'] = pd.Series(perf1_dict)
# perf2_df['incorrectly_selected'] = pd.Series(perf2_dict)
# perf1_df.to_csv('Performance_1.csv')
# perf2_df.to_csv('Performance_2.csv')
# print()
# print()
# print("Performance 1 incorrect options: ", perf1_dict, '\n')
# print("Performance 2 incorrect options: ", perf2_dict, '\n')

# ad1_df['incorrectly_selected'] = pd.Series(ad1_dict)
# ad2_df['incorrectly_selected'] = pd.Series(ad2_dict)
# ad1_df.to_csv('Advertising_1.csv')
# ad2_df.to_csv('Advertising_2.csv')
# print()
# print()
# print("Advertising 1 incorrect options: ", ad1_dict, '\n')
# print("Advertising 2 incorrect options: ", ad2_dict, '\n')

print()
print()

# print('--------------------------------------------------------------------------------------------------------------------------------------------------')

# print("Strictly Necessary Q1: Imagine that you are browsing an online clothing store for the first time. You see a couple of pieces of clothing that you are interested in, which you start adding to your shopping cart without creating an account on the website. Which of the following cookies do you believe helps the website remember the contents of your online shopping cart?")
# sn_correct_percent = sn1_df['correct']['Strictly Necessary'] / participants_shown['Strictly Necessary']
# print('Strictly necessary was correctly chosen', str("{:.2%}".format(sn_correct_percent)))

# nec_correct_percent = sn1_df['correct']['Necessary'] / participants_shown['Necessary']
# print('Necessary was correctly chosen', str("{:.2%}".format(nec_correct_percent)))
# print()
# for k in sn1_dict:
#     # need to find how many times incorrect option was chosen / how many times incorrect option was shown
#     # print(k, "was shown", participants_shown[k], "times and chosen", sn1_dict[k], "times")

#     incorrect_percent = (sn1_dict[k] / participants_shown[k])
#     print(k, "was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

# print()
# print('--------------------------------------------------------------------------------------------------------------------------------------------------')

# print("Strictly Necessary Q2: You visit a community events bulletin website for the first time and are greeted with a cookie banner. You can either allow or prevent the website from placing cookies on your browser. You decide to 'Decline' the website's request to set cookies and continue browsing the various events. The next week you return to the website to confirm the details of a particular event. You no longer see the cookie banner. Which of the following cookies do you think helps the website remember that you have already set your cookie settings?")
# sn2_correct_percent = sn2_df['correct']['Strictly Necessary'] / participants_shown['Strictly Necessary']
# print('Strictly necessary was correctly chosen', str("{:.2%}".format(sn2_correct_percent)))

# nec2_correct_percent = sn2_df['correct']['Necessary'] / participants_shown['Necessary']
# print('Necessary was correctly chosen', str("{:.2%}".format(nec2_correct_percent)))
# print()
# for k in sn2_dict:
#     incorrect_percent = (sn2_dict[k] / participants_shown[k])
#     print(k, "was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

# print('--------------------------------------------------------------------------------------------------------------------------------------------------')
# print("Performance Q1: Websites use cookies to understand how many users visit their websites during a day without uniquely identifying each user. Which of the following cookies do you think allows the website to use this feature?")
# perf_correct_percent = perf1_df['correct']['Performance'] / participants_shown['Performance']
# print()
# print('Performance was correctly chosen', str("{:.2%}".format(perf_correct_percent)))
# print()
# anon_correct_percent = perf1_df['correct']['Anonymous Analytics'] / participants_shown['Anonymous Analytics']
# print('Anonymous Analytics was correctly chosen', str("{:.2%}".format(anon_correct_percent)))
# print()
# agg_correct_percent = perf1_df['correct']['Aggregated Analytics'] / participants_shown['Aggregated Analytics']
# print('Aggregated Analytics was correctly chosen', str("{:.2%}".format(agg_correct_percent)))
# print()

# for k in perf1_dict:
#     incorrect_percent = (perf1_dict[k] / participants_shown[k])
#     print(k, "was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

# print()
# print('--------------------------------------------------------------------------------------------------------------------------------------------------')
# print("Performance Q2: You’ve accepted all cookies on a website but notice that multiple pages on the website are broken and are showing you error messages. What type of cookies are recording these error messages and sending information to the company without linking to your identity?")
# perf2_correct_percent = perf2_df['correct']['Performance'] / participants_shown['Performance']
# print()
# print('Performance was correctly chosen', str("{:.2%}".format(perf2_correct_percent)))
# print()
# anon2_correct_percent = perf2_df['correct']['Anonymous Analytics'] / participants_shown['Anonymous Analytics']
# print('Anonymous Analytics was correctly chosen', str("{:.2%}".format(anon2_correct_percent)))
# print()
# agg2_correct_percent = perf2_df['correct']['Aggregated Analytics'] / participants_shown['Aggregated Analytics']
# print('Aggregated Analytics was correctly chosen', str("{:.2%}".format(agg2_correct_percent)))
# print()

# for k in perf2_dict:
#     incorrect_percent = (perf2_dict[k] / participants_shown[k])
#     print(k, "was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

# print()

# print('--------------------------------------------------------------------------------------------------------------------------------------------------')
# print("Functional Q1: You open an online shopping website and you select “Decline all cookies”. You start looking at different products on the website, and notice that reviews aren’t loading properly. Which cookies would allow for the reviews to load?")
# func_correct_percent = fun1_df['correct']['Functional'] / participants_shown['Functional']
# print()
# print('Functional was correctly chosen', str("{:.2%}".format(func_correct_percent)))
# print()
# personalization_correct_percent = fun1_df['correct']['Personalization'] / participants_shown['Personalization']
# print('Personalization was correctly chosen', str("{:.2%}".format(personalization_correct_percent)))
# print()
# prefs_correct_percent = fun1_df['correct']['Preferences'] / participants_shown['Preferences']
# print('Preferences was correctly chosen', str("{:.2%}".format(prefs_correct_percent)))
# print()
# pe_correct_percent = fun1_df['correct']['Personalized Experience'] / participants_shown['Personalized Experience']
# print('Personalized Experience was correctly chosen', str("{:.2%}".format(pe_correct_percent)))
# print()
# cus_correct_percent = fun1_df['correct']['Customization'] / participants_shown['Customization']
# print('Customization was correctly chosen', str("{:.2%}".format(cus_correct_percent)))
# print()
# for k in fun1_dict:
#     incorrect_percent = (fun1_dict[k] / participants_shown[k])
#     print(k, "was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

# print()

# print('--------------------------------------------------------------------------------------------------------------------------------------------------')
# print("Functional Q2: You are having trouble with your internet service provider and visit their webpage to look for a solution. You see that they have the option of starting an online conversation with one of their agents through the website’s chat bot feature. Which of the following cookies would you want to turn on so that you can access the chat bot on the page?")
# func2_correct_percent = fun2_df['correct']['Functional'] / participants_shown['Functional']
# print()
# print('Functional was correctly chosen', str("{:.2%}".format(func2_correct_percent)))
# print()
# personalization2_correct_percent = fun2_df['correct']['Personalization'] / participants_shown['Personalization']
# print('Personalization was correctly chosen', str("{:.2%}".format(personalization2_correct_percent)))
# print()
# prefs2_correct_percent = fun2_df['correct']['Preferences'] / participants_shown['Preferences']
# print('Preferences was correctly chosen', str("{:.2%}".format(prefs2_correct_percent)))
# print()
# pe2_correct_percent = fun2_df['correct']['Personalized Experience'] / participants_shown['Personalized Experience']
# print('Personalized Experience was correctly chosen', str("{:.2%}".format(pe2_correct_percent)))
# print()
# cus2_correct_percent = fun2_df['correct']['Customization'] / participants_shown['Customization']
# print('Customization was correctly chosen', str("{:.2%}".format(cus2_correct_percent)))
# print()
# for k in fun2_dict:
#     incorrect_percent = (fun2_dict[k] / participants_shown[k])
#     print(k, "was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

# print()

# print('--------------------------------------------------------------------------------------------------------------------------------------------------')
# print("Functional Q3: You visit a graphic design website to design posters for an event and accept all cookies on the website’s cookie banner. The first time you visit the website you are greeted with an optional short tutorial that guides you on how to use the platform effectively. You step through the tutorial and dismiss it once you’ve completed it. After you are done working for the day, you close your browser window. When revisiting the website the next day, you see that the tutorial is no longer offered to you. Which cookie remembers that you have already seen the tutorial and knows not to offer it to you again?")
# func3_correct_percent = fun3_df['correct']['Functional'] / participants_shown['Functional']
# print()
# print('Functional was correctly chosen', str("{:.2%}".format(func3_correct_percent)))
# print()
# personalization3_correct_percent = fun3_df['correct']['Personalization'] / participants_shown['Personalization']
# print('Personalization was correctly chosen', str("{:.2%}".format(personalization3_correct_percent)))
# print()
# prefs3_correct_percent = fun3_df['correct']['Preferences'] / participants_shown['Preferences']
# print('Preferences was correctly chosen', str("{:.2%}".format(prefs3_correct_percent)))
# print()
# pe3_correct_percent = fun3_df['correct']['Personalized Experience'] / participants_shown['Personalized Experience']
# print('Personalized Experience was correctly chosen', str("{:.2%}".format(pe3_correct_percent)))
# print()
# cus3_correct_percent = fun3_df['correct']['Customization'] / participants_shown['Customization']
# print('Customization was correctly chosen', str("{:.2%}".format(cus3_correct_percent)))
# print()
# for k in fun3_dict:
#     incorrect_percent = (fun3_dict[k] / participants_shown[k])
#     print(k, "was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

# print()

# print('--------------------------------------------------------------------------------------------------------------------------------------------------')
# print("Targeting/Advertising Q1: While visiting a social media website, you see a website banner announcing a 40% price drop on a Caribbean cruise and click on the banner to learn more. After reading through the details on the cruise, you close the page for the cruise and go back to the social media website. Which cookie would you turn off to prevent the social media website from knowing that you’re interested in a specific offer like the cruise?")
# ad1_correct_percent = ad1_df['correct']['Advertising'] / participants_shown['Advertising']
# print()
# print('Advertising was correctly chosen', str("{:.2%}".format(ad1_correct_percent)))
# print()
# targeting1_correct_percent = ad1_df['correct']['Targeting'] / participants_shown['Targeting']
# print('Targeting was correctly chosen', str("{:.2%}".format(targeting1_correct_percent)))
# print()
# marketing1_correct_percent = ad1_df['correct']['Marketing'] / participants_shown['Marketing']
# print('Marketing was correctly chosen', str("{:.2%}".format(marketing1_correct_percent)))
# print()
# pa1_correct_percent = ad1_df['correct']['Personalized Advertising'] / participants_shown['Personalized Advertising']
# print('Personalized Advertising was correctly chosen', str("{:.2%}".format(pa1_correct_percent)))
# print()
# ta1_correct_percent = ad1_df['correct']['Targeted Advertising'] / participants_shown['Targeted Advertising']
# print('Targeted Advertising was correctly chosen', str("{:.2%}".format(ta1_correct_percent)))
# print()
# for k in ad1_dict:
#     incorrect_percent = (ad1_dict[k] / participants_shown[k])
#     print(k, "was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

# print()

print('--------------------------------------------------------------------------------------------------------------------------------------------------')
print("While browsing a travel website, you notice a pop-up promoting price drops of flights to France and click on it, which opens a new window with the details. After going back to the main travel website, you see multiple pop-ups and banners have appeared that show hotels and restaurants in Paris. Which cookie do you think is responsible for this?")
ad2_correct_percent = ad2_df['correct']['Advertising'] / participants_shown['Advertising']
print()
print('Advertising was correctly chosen', str("{:.2%}".format(ad2_correct_percent)))
print()
targeting2_correct_percent = ad2_df['correct']['Targeting'] / participants_shown['Targeting']
print('Targeting was correctly chosen', str("{:.2%}".format(targeting2_correct_percent)))
print()
marketing2_correct_percent = ad2_df['correct']['Marketing'] / participants_shown['Marketing']
print('Marketing was correctly chosen', str("{:.2%}".format(marketing2_correct_percent)))
print()
pa2_correct_percent = ad2_df['correct']['Personalized Advertising'] / participants_shown['Personalized Advertising']
print('Personalized Advertising was correctly chosen', str("{:.2%}".format(pa2_correct_percent)))
print()
ta2_correct_percent = ad2_df['correct']['Targeted Advertising'] / participants_shown['Targeted Advertising']
print('Targeted Advertising was correctly chosen', str("{:.2%}".format(ta2_correct_percent)))
print()
for k in ad2_dict:
    incorrect_percent = (ad2_dict[k] / participants_shown[k])
    print(k, "was incorrectly chosen", str("{:.2%}".format(incorrect_percent)))

print()