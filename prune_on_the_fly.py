def prune_on_the_fly(canCodeSet, codeSet, db):
	'''
	Returns ...

	Parameters:
		canCodeSet (list of sets): Candidate coding set of db
		codeSet (list of sets): Current coding set of db
		db (list of lists): List of transactions comprising dataset 
	Returns:
		codeSet (list of sets): minimal coding set of db
	'''

	return canCodeSet