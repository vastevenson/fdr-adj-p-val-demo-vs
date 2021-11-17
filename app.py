'''
Goal: demo how to apply the False Discovery Rate (FDR) formula in Python
FDR = Benjamini-Hochberg procedure

The purpose of the FDR adjustment is for when you have thousands of p values, it will allow you to determine the subset of p-values for which you are even more confident there is no Type 1 (false positive) error made.

Formula: p_val*len_p_val_list/rank
'''

import random

# create a uniform distribution of 1000 p-values
p_val_list = []
for i in range(1000):
    p_val = random.random()
    p_val_list.append(p_val)

# now perform the FDR adjustment
# start by sorting the list asc
p_val_list.sort()

# next, assign a rank to each item in list, start at 1
rank = 1
len_p_val_list = len(p_val_list)
p_adj_list = []
for p in p_val_list:
    fdr_adj_p_val = p*len_p_val_list/rank
    rank += 1
    p_adj_list.append(
        {
            "p_val": p,
            "fdr_adj_p_val": fdr_adj_p_val
        }
    )
print()
