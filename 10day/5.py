import random
i = 1
for i in range(1,4):
	print("第%d局"%i)
	player = int(input("请选择 1-石头 2-剪刀 3-布:"))
	computer = random.randint(1,3)
	if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
		print("玩家赢")
	elif (player == computer):
		print("平局")
	else:
		print("电脑赢")
	i+=1
