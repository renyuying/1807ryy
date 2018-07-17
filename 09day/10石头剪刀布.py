import random
i = 1
for i in range(1,11):
	print(i)
	player = int(input("请出拳　石头 /剪刀 /布:"))
	computer = random.randint(1,3)
	if ((player == 1 and computer == 2)  or (player == 2 and computer == 3) or (player == 3 and computer == 1)):

		print("弱爆了")
	elif player == computer:
		print("再来一盘")
	else:
		print("不行")
	i += 1
