height = int(input("请输入身高"))
face = int(input("请输入颜值"))
moeny = int(input("请输入身价"))
if height > 180 and moeny > 1000000 and face > 99:
	print("高富帅")
if moeny > 1000000 and face > 99:
	print("富帅")
if face > 99:
	print("帅")
elif height < 160 and moeny < 100 and face < 60:
	print("矮挫穷")
