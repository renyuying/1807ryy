home = ["老王","老赵","老宋",1,2,3,True]#定义一个列表
home1 = ["老王"]
#home1.append("老宋")#老宋进来
#print(home1)

home1.insert(0,"老宋")#插队
print(home1)

#走出房间　　　　删除
home1.pop()  #谁在后面谁先走
print(home1)

home1.pop(0) #根据数字删
print(home1)

home1.remove("老宋")
print(home1)
