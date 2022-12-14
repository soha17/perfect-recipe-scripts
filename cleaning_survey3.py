import pandas as pd
# sncookie, fcookie, pcookie, tcookie

sncookie_correct = 0
fcookie_correct = 0
pcookie_correct = 0
tcookie_correct = 0

# we need to look at each row and see which cookie category they selected
df = pd.read_csv('comprehension1.csv')
print(list(df.columns.values))