name = 'Indraja Naik'
name  = name.lower()
d = {}

for i in name:
	if i not in d:
		d[i] = 1
	else:
		d[i] = d[i] + 1
print(d)