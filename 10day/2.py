import random
pc = random.randint(1,100)
for i in range(1,10):
	j = int(input("请输入数字"))
	if j < pc:
		print("猜小了")
	elif j > pc:
		print("猜大了")
	else:
		print("猜对了")
		break


