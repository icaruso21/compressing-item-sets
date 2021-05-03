def standard(I, db):
	'''
	Returns a list of item sets I sorted in decreasing order by level of support in dataset db.

	Parameters:
		I (list of sets): List of item sets (singleton items only in this application)
		db (list of lists): List of transactions comprising dataset 
	Returns:
		res (list of sets): I sorted in decreasing order by level of support in db
	'''
	res = [[itemset, 0] for itemset in I]
	for idx, iset in enumerate(I):
		# Compute support for each itemset
		for transaction in db:
			if iset.issubset(set(transaction)):
				res[idx][1] += 1

	# Sort in descending order of support
	res.sort(key= lambda x: x[1])
	# Remove support values
	res = [x[0] for x in res]

	return res