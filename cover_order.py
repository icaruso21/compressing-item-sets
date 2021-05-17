import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

def cover_order(j, db):
    '''
    Returns a list of item sets j sorted by decreasing cover over db

    Parameters:
    j (list of sets): List of item sets
    db (list of lists): List of transactions comprising data set 
    Returns:
        ordered_j (list of sets): j sorted by decreasing cover over db
    '''
    # Apriori from: http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/
    # Use TransactionEncoder to convert transactions to matrix
    te = TransactionEncoder()
    te_ary = te.fit(db).transform(db)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    # Run apriori to get support of each itemset
    frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
    # Calculate cover from support and length
    frequent_itemsets['cover'] = frequent_itemsets['length'] * frequent_itemsets['support']
    # Sort itemsets by cover, descending
    frequent_itemsets = frequent_itemsets.sort_values('cover', ascending=False)
    #print("Itemsets with the 10 largest covers: ")
    #print(frequent_itemsets[:10])
    sorted_covers = frequent_itemsets['itemsets'].values.tolist()
    toreturn_covers = []
    # Add itemsets in j to toreturn_covers list to be returned
    for itemset in sorted_covers:
        if itemset in j:
            toreturn_covers.append(itemset)
    return toreturn_covers

#j = [{2,3,4}, {1,2,3}, {3}, {1,2}, {2,3,4,5}]
#db = [[1,2,3,4,5],[1,2],[1,2,3]]
#cover_test = cover_order(j, db)
#print("List of itemsets returned from cover_test by descending cover: ")
#print(cover_test)
