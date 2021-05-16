from noise import noise

def denoise (i, code_set, db):
    '''
	Removes noise from the db

	Arguments:
		I: List[Set[]] - The alphabet, list of singleton item sets
        CodeSet: List[Set[]] - minimal coding set of db
        db: List[List] - List of transactions comprising dataset 
	Returns:
		CodeSet
	'''
    # set of sets of transactions which are noise
    noise = noise(i, code_set, db)
    denoised_db = []
    for transaction in db:
        if set(transaction) not in noise:
            denoised_db.append(transaction)
    return denoised_db
