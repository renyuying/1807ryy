a = 0
while a<=3:
	a=a+1
	zh = input("请输入帐号:")
	ma = int(input("请输入密码:"))
	if zh == "ryy" and ma == 123:
		print("登录成功:")	
		yx = int(input("选择英雄范围 0=ADC 1=肉　3=法师\n:"))
		if yx == 0:	
			print("鲁班大师")
		elif yx == 1:
			print("程咬金")
		elif yx == 3:
			print("妲己")
	else:
		print("重新输入")



















