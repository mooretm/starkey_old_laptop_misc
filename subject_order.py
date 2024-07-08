

import pandas as pd
import itertools
import random

# Define conditions
gains = ['OAG', 'LFG', 'HFG']
conds = ['JND', 'PREF', 'SLOW']

# Return list of all permutations
conds_iter = list(itertools.permutations(conds, 3)) 
gains_iter = list(itertools.product(gains, conds_iter))

# Flatten tuple
order = [(x, *rest) for x, rest in gains_iter]

# Create sub list based on number of permutations
subs = range(1,len(order)+1)

# Must zip lists to create data frame
zipped = list(zip(subs, order))

# Create initial data frame
# 'order' contains tuples
df = pd.DataFrame(zipped, columns=['sub', 'order'])

# Flatten tuples and create columns for each value
col_names = ['c1', 'c2', 'c3', 'c4']
for n, col in enumerate(col_names):
    df[col] = df['order'].apply(lambda order: order[n])

# Drop original 'order' column with tuples
df = df.drop('order', axis=1)

# Provide command line feedback
print(df)




####################
# Redefine subs to fit the number of conditions
subs = range(7,13)

# Subset data frame by gain type
oag = df[df['c1'] == 'OAG']
lfg = df[df['c1'] == 'LFG']
hfg = df[df['c1'] == 'HFG']

# Get randomized index values for each gain type
oag_rand = random.sample(list(oag.index), k=len(list(oag.index)))
lfg_rand = random.sample(list(lfg.index), k=len(list(lfg.index)))
hfg_rand = random.sample(list(hfg.index), k=len(list(hfg.index)))

# Assign subs based on randomized indeces
for i, sub in enumerate(subs):
    df.loc[oag_rand[i], 'sub'] = sub
    df.loc[lfg_rand[i], 'sub'] = sub
    df.loc[hfg_rand[i], 'sub'] = sub

df = df.sort_values(by='sub')

print(df)

#for sub in subs:
#    x = df[df['sub'] == sub]
#    rand_index = random.sample(list(x.index), k=3)
#    print(x.loc[rand_index])

# Write file
df.to_csv('sub_order.csv', index=False)


