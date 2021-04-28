import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

def cover-order(j, db):
'''
Returns a list of item sets I sorted in decreasing order by level of support in dataset db.

Parameters:
j (list of sets): List of item sets
db (list of lists): List of transactions comprising data set 
Returns:
	ordered_j (list of sets): j sorted by decreasing cover over db
'''
    # Apriori from: http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/
    te = TransactionEncoder()
    te_ary = te.fit(db).transform(db)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    df
    for itemset in j:
