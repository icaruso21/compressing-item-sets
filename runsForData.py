import sys
import itertools
import json
from naive_compression import naive_compression
from DBReader import getDB
from timeit import default_timer as timer
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from compress_and_prune import compress_and_prune
from compress_and_sanitize import compress_and_sanitize
from all_out_compression import all_out_compression

def runsForData(algorithm, filepath, min_supp):
	'''
	Runs a version of dataset compression and prints the resulting coding set.

	Arguments:
		--v: Version of compression algorithm to run, default=naive
		--f: Path to .txt file representing dataset
	Returns:
		None
	'''
	# Parse arguments
	
	# Read data file into memory
	data = getDB(filepath)

	#print("Data: ", data)

	# Extract alphabet
	alphabet = set()
	for transaction in data:
		for item in transaction:
			alphabet.add(item)
	
	alphabet = [set(singleton) for singleton in alphabet]

	#print("Alphabet: ", alphabet)

	# Extract all item sets J
	#j = set()
	freq = min_supp / len(data)
	te = TransactionEncoder()
	te_ary = te.fit(data).transform(data)
	df = pd.DataFrame(te_ary, columns=te.columns_)
	# Run apriori to get support of each itemset
	
	frequent_itemsets = apriori(df, min_support=freq, use_colnames=True)
	print(frequent_itemsets)
	j = frequent_itemsets['itemsets'].tolist()
	# for transaction in data:
	# 	for l in range(1,len(transaction)+1):
	# 		subsets = list(map(set, itertools.combinations(transaction,l)))
	# 		for s in subsets:
	# 			j.add(frozenset(s))
	# 	j.add(frozenset(transaction))
	
	#j = list(j)

	#print("J: ", j)


	# Run Compression Algorithm
	start = timer()
	if(algorithm == "pruning"):
		print("Running compression with pruning on data in " + filepath + ".")
		codeSet = compress_and_prune(alphabet, j, data)
	elif(algorithm == "allout"):
		print("Running all-out compression on data in " + filepath + ".")
		codeSet = all_out_compression(alphabet, j, data)
	elif(algorithm == "sanitize"):
		print("Running compress-and-sanitize on data in " + filepath + ".")
		codeSet = compress_and_sanitize(alphabet, j, data)
	elif(algorithm == "naive"):
		print("Running naive compression (default) on data in " + filepath + ".")
		codeSet = naive_compression(alphabet, j, data)
	end = timer()

	runtime = (end - start)

	# Print final codeSet
	print("Code Set:")
	for itemset in codeSet:
		print(itemset)

	print("Compression took " + str(runtime) + " seconds on data in " + filepath + ".")
	return {"runtime": runtime,
			"code_set": [list(x) for x in codeSet],
			"code_set_length": len(codeSet)}

def do_runs(filepath, dataset):
	algorithms = ["pruning", "allout", "sanitize", "naive"]
	min_supps = [1, 2, 3, 4]
	for min_supp in min_supps:
		for algorithm in algorithms:
			output = runsForData(algorithm, filepath, min_supp)
			output['min_supp'] = min_supp
			output['algorithm'] = algorithm
			with open(f'./out/{dataset}_{algorithm}_{min_supp}.json', 'w') as f:
				json.dump(output, f)


filepath = "./data/input.txt"
dataset = "input"
do_runs(filepath, dataset)