while True:
	height = float(input("输入身高"))
	weight = float(input("请输入体重"))
	a = weight/ (height**2)
	if a < 18.5:
		print("过轻")
	elif a < 25 and a>=18.5:
		print("正常")
	elif a < 28 and a >= 25:
		print("过重")
	elif a < 32 and a >= 28:
		print("过胖")
	elif a > 32:
		print ("严重过胖")
	else:
		print("不正常")
