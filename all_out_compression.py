from compress_and_prune import compress_and_prune
from sanitize import sanitize


def all_out_compression(I,J,db):
    '''
	Returns a list of item sets J sorted in decreasing order by level of "cover" in dataset db.

	Parameters:
		I (list of sets): Alphabet, list of singleton item sets
		J (list of sets): List of all item sets (permutations) made from I 
		db (list of lists): List of transactions comprising dataset 
	Returns:
		codeSet (list of sets): coding set of db
	'''
    result = compress_and_prune(I, J, db)
    result = sanitize(I, result, db)
    return result
