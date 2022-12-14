import itertools
import random

def foo(l):
    yield from itertools.product(*([l] * 4)) 

def moving():
    for x in foo(stuff):
        print(x)

    for L in range(len(stuff) + 1):
        for subset in itertools.combinations(stuff, L):
            print(subset)

stuff = [["Strictly Necessary", "Necessary"], 
         ["Functional", "Personalization", "Preferences", "Personalized Experience", "Customization"],  
         ["Anonymous Analytics", "Aggregated Analytics", "Performance"], 
         ["Targeting", "Marketing", "Advertising", "Targeted Advertising", "Personalized Advertising"]]

combinations = [p for p in itertools.product(*stuff)]
count = 0
strictly = 0
necessary = 0

functional = 0
personalization = 0
preferences = 0
personalized_experience = 0
customization = 0

anonymous_analytics = 0
aggregated_analytics = 0
performance = 0

targeting = 0
marketing = 0
advertising = 0
targeted_advertising = 0
personalized_advertising = 0

for x in combinations:
    count = count + 1
    
    if x[0] == 'Strictly Necessary':
        strictly += 1
    elif x[0] == 'Necessary':
        necessary += 1
    
    if x[1] == 'Functional':
        functional += 1
    elif x[1] == 'Personalization':
        personalization += 1
    elif x[1] == 'Preferences':
        preferences += 1
    elif x[1] == 'Personalized Experience':
        personalized_experience += 1
    elif x[1] == 'Customization':
        customization += 1
    
    if x[2] == 'Anonymous Analytics':
        anonymous_analytics += 1
    elif x[2] == 'Aggregated Analytics':
        aggregated_analytics += 1
    elif x[2] == 'Performance':
        performance += 1
    
    if x[3] == 'Targeting':
        targeting += 1
    elif x[3] == 'Marketing':
        marketing += 1
    elif x[3] == 'Advertising':
        advertising += 1
    elif x[3] == 'Targeted Advertising':
        targeted_advertising += 1
    elif x[3] == 'Personalized Advertising':
        personalized_advertising += 1

    # print(x)
print("Strictly Necessary:", strictly, "Necessary:", necessary)
print("Functional:", functional, "Personalization:", personalization, "Preferences", preferences, "Personalized Experience", personalized_experience, "Customization", customization)
print("Anonymous Analytics:", anonymous_analytics, "Aggregated Analytics:", aggregated_analytics, "Performance:", performance)
print("Targeting:", targeting, "Marketing:", marketing, "Advertising:", advertising, "Targeted Advertising:", targeted_advertising, "Personalized Advertising:", personalized_advertising)

print(count)

# hashmap = {"stn": ["Strictly Necessary", "Necessary"], 
#            "fnc": ["Functional", "Personalization", "Preferences", "Personalized Experience", "Customization"],  
#            "perf": ["Anonymous Analytics", "Aggregated Analytics", "Performance"], 
#            "targ": ["Targeting", "Marketing", "Advertising", "Targeted Advertising", "Personalized Advertising"]}

# countmap = {"stn": [0,0], 
#             "fnc": [0,0],  
#             "perf": [0,0], 
#             "tar": [0,0]}

# for x in combinations:
#     for strings in x:
#         for key, value in hashmap.items():
#             if strings in value:
#                 chk = hashmap.get(key)
#                 chk1= countmap.get(key)
#                 print(chk1[chk.index(strings)])
#                 print(chk1)
#                 # chk1[chk.index(strings)] = chk1[chk.index(strings)] + 1
#                 # up_dict = {key: chk1}
#                 # countmap.update(up_dict)

# print(countmap)
        







