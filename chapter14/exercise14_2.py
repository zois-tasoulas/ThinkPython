from anagram_set import all_anagrams
from anagram_set import signature
import dbm
import pickle
db_name = 'anagrams-db'

def store_anagrams(dic):
	db = dbm.open(db_name, 'c')
	for key in dic:
		db[key] = pickle.dumps(dic[key])
	db.close()

def read_anagrams(dic, word):
	db = dbm.open(db_name, 'c')
	if signature(word) in db:
		print(pickle.loads(db[signature(word)]))
	db.close()
	

if __name__ == '__main__':
	d = all_anagrams('../chapter9/words.txt')
	store_anagrams(d)
	read_anagrams(d, 'tree')
