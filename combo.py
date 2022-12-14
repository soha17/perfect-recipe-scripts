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
for x in combinations:
    count = count + 1

print(count)

hashmap = {"stn": ["Strictly Necessary", "Necessary"], 
           "fnc": ["Functional", "Personalization", "Preferences", "Personalized Experience", "Customization"],  
           "perf": ["Anonymous Analytics", "Aggregated Analytics", "Performance"], 
           "targ": ["Targeting", "Marketing", "Advertising", "Targeted Advertising", "Personalized Advertising"]}

countmap = {"stn": [0,0], 
            "fnc": [0,0],  
            "perf": [0,0], 
            "tar": [0,0]}

for x in combinations:
    for strings in x:
        for key, value in hashmap.items():
            if strings in value:
                chk = hashmap.get(key)
                chk1= countmap.get(key)
                print(chk1[chk.index(strings)])
                print(chk1)
                # chk1[chk.index(strings)] = chk1[chk.index(strings)] + 1
                # up_dict = {key: chk1}
                # countmap.update(up_dict)

print(countmap)
        







