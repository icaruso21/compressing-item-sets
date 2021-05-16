from typing import Set
from denoise import denoise

def sanitize (i, code_set, db):
    '''
	Sanitizes the dataset (removes freak items from the dataset and code set)

	Arguments:
		I: List[Set[]] - The alphabet, list of singleton item sets
        CodeSet: List[Set[]] - minimal coding set of db
        db: List[List] - List of transactions comprising dataset 
	Returns:
		CodeSet
	'''
    db = denoise(i, code_set, db)
    denoised_code_set = []
    for j in code_set:
        n_transactions = 0
        for transaction in db:
            if j.issubset(transaction):
                n_transactions += 1
        cover = len(j) * n_transactions
        if cover != 0: 
            denoised_code_set.append(j)
    return denoised_code_set