def most_frequent(strng):
	d = dict()
	for letter in strng.lower():
		if ord(letter) in range(ord('a'), ord('z')):
			if letter in d:
				d[letter] += 1
			else:
				d[letter] = 1
	lst = []
	for key in d:
		lst.append((d[key], key))
	lst.sort(reverse=True)
	for (num, let) in lst:
		print(num, let)

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eleifend dictum velit ut euismod. Vivamus at finibus odio. Nunc eget enim in ante tincidunt imperdiet. Nunc in ornare massa, lobortis volutpat metus. Mauris eu urna vitae leo luctus pellentesque quis rutrum ipsum. Quisque massa ante, hendrerit in blandit in, eleifend tristique est. Pellentesque ullamcorper ex non rhoncus feugiat. Cras varius lectus non dignissim luctus. Sed massa metus, interdum vitae dui a, feugiat sodales orci. Vestibulum ornare neque fermentum augue porttitor, ac iaculis ipsum varius. Aenean cursus placerat imperdiet. Aliquam mi est, ullamcorper in dignissim eu, euismod et arcu. Etiam at eros nunc. Pellentesque efficitur massa quis mi sollicitudin, nec fermentum eros lobortis. Fusce rutrum interdum nulla sed malesuada. Etiam at orci at eros vestibulum laoreet."
most_frequent(txt)
