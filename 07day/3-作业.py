year = int(input("请输入年份"))
if (year % 4 ==0 and year % 100 !=0) or year % 400 ==0:
	print("%d年是闰年"%year)
else:
	print("%d是平年"%year)
for i in range(1,10):
	for j in  range(1,i+1):
		print("%d*%d=%d"%(i,j*i),end = "\t")
	print("")
