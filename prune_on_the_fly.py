def prune_on_the_fly(canCodeSet, codeSet, db):
	'''
	Removes an element from CanCodeSet and check if the resulting compression is better than that of CodeSet itself.

	Parameters:
		canCodeSet (list of sets): Candidate coding set of db
		codeSet (list of sets): Current coding set of db
		db (list of lists): List of transactions comprising dataset 
	Returns:
		codeSet (list of sets): minimal coding set of db
	'''

	pruneSet = [] # TODO: intialize pruneSet
	# pruneSet contains all J from codeSet where cover(J, canCodeSet) < cover(J, codeSet)

	pruneSet = standard(pruneSet, db)

	while(len(pruneSet) > 0):
		cand = pruneSet.pop()

		posCodeSet = codeSet.copy()
		posCodeSet.remove(cand) 

		if comp_len(posCodeSet, db) < comp_len(canCodeSet, db):
			canCodeSet = posCodeSet

	return canCodeSet