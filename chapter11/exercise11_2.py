def inverse_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)
	return inverse

a = {'a': 2, 'b': 3, 'c': 1, 'd': 2, 'e': 4}
print(inverse_dict(a))
