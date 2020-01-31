for a in range(1,101):
	if a%10==7:
		continue
	elif a in range(70,80):
		continue
	elif a/7 in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
		continue
	else:
		print(a)

