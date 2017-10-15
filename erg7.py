words = raw_input("Dwse lekseis xerismenes me keno.")
words = words.split()
biggest_word = ""
max = 0

for i in words:
	if len(i) >= max:
		max = len(i)
		biggest_word = i

print biggest_word
