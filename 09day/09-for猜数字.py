import random
pc = random.randint(1,20)
for i in range(1,11):
	player = int(input("请输入数字:"))
	if player > pc:
		print("猜大了")
	elif player < pc:
		print("猜小了")
	elif player == pc:
		print("猜对了")
		break

