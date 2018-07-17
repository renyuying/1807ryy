import random
i = 0
num = random.randint(1,100)
while i <9:
	u_sum = int(input("请输入数字"))
	if u_sum > sum:
		print("猜大了")
	elif u_sum < sum:
		print("猜小了")
	else:
		print("猜对了")
