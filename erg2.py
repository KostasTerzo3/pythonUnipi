ores=[]
for i in range (24):
 ores.append(raw_input("Dwse "))
ores = (zip(*[iter(ores)]*6))

for index, i in enumerate(ores):
	max = 0
	for j in i:
		if j > max:
			max = j
	print (index + 4, "pm:", max)
