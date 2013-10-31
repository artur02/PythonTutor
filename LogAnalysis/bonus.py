# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:46:45 2013

@author: Artur_Herczeg
"""

import pandas as pd

ind = ['A', 'B', 'C']

frame = pd.DataFrame({
    'Food': [4, 3, 2],
    'Clothes': [8, 3, 1]},
    index=ind, dtype=float)

frame['Prod'] = ((frame.Food-1)/frame.Food)*frame.Clothes
frame['Tally'] = pd.Series()

for i in frame.index:
    a = list(ind)
    a.remove(i)
    frame.ix[i, "Tally"] = frame.ix[i, "Prod"] + frame.ix[a].Clothes.sum()

if __name__ == "__main__":
    print frame[['Food', 'Clothes']]
#    print frame
    frame.Tally.plot(kind='bar', title='Production')
