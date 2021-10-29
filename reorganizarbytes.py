#reorganizando los bytes

lista = []
num = 24
for i in range (24):
	lista.append(num)
	if(num == 30):
		num = num + 24
	if(num == 62):
		num = num - 39
	if(num == 31):
		num = num + 24
	if(num == 63):
		num = num - 49
	if(num == 22):
		num = num + 24
	num = num +2

num = 17
for i in range (24):
	lista.append(num)
	if(num == 23):
		num = num + 24
	if(num == 55):
		num = num - 49
	if(num == 14):
		num = num + 24
	if(num == 46):
		num = num - 39
	if(num == 15):
		num = num + 24
	num = num +2

num = 0
for i in range (16):
	lista.append(num)
	if(num == 6):
		num = num + 24
	if(num == 38):
		num = num - 39
	if(num == 7):
		num = num +24

	num = num +2


#parte 2 del bitmap

num = 88
for i in range (24):
	lista.append(num)
	if(num == 94):
		num = num + 24
	if(num == 126):
		num = num - 39
	if(num == 95):
		num = num + 24
	if(num == 127):
		num = num - 49
	if(num == 86):
		num = num + 24
	num = num +2

num = 81
for i in range (24):
	lista.append(num)
	if(num == 87):
		num = num + 24
	if(num == 119):
		num = num - 49
	if(num == 78):
		num = num + 24
	if(num == 110):
		num = num - 39
	if(num == 79):
		num = num + 24
	num = num +2

num = 64
for i in range (16):
	lista.append(num)
	if(num == 70):
		num = num + 24
	if(num == 102):
		num = num - 39
	if(num == 71):
		num = num +24

	num = num +2

print(lista)