from naive_compression import naive_compression
from sanitize import sanitize


def compress_and_sanitize (I,J,db):
    '''
	Returns a list of item sets J sorted in decreasing order by level of "cover" in dataset db.

	Parameters:
		I (list of sets): Alphabet, list of singleton item sets
		J (list of sets): List of all item sets (permutations) made from I 
		db (list of lists): List of transactions comprising dataset 
	Returns:
		codeSet (list of sets): coding set of db
	'''
    result = naive_compression(I, J, db)
    result = sanitize(I, result, db)
    return result