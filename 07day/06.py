x = int(input("请输入x值"))
y = int(input("请输入y值"))
shuru = input("请输入+-*/")
c = 0
if shuru == "+":
	c = c + x + y
	print("x+y的结果%d"%(c))
elif shuru == "-":
	c = c + x - y
	print("x-y的结果%d"%(c))
elif shuru == "*":
	c = c + x * y
	print("x*y的结果%d"%(c))
elif shuru == "/":
	c = c + x / y
	print("x/y的结果%d"%(c))
else:
 	print("输入错误")

