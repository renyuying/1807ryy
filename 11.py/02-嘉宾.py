name = ["老王","老李","老刘"]
for j in name:
	print("%s我想要共进晚餐"%j)
print('')


print('老李不能赴约，另邀请嘉宾：老宋')
name[2]='老宋'
for j in name:
	print('想要邀请%s一起共进晚餐'%j)
print('')


print('找到更大的桌,找更多的人')
name.insert(0,'隋婧')
name.insert(1,'袁雨华')
name.append('马欢丽')
for n in name:
	print('想要%s 我们一起吧'%n)
print('')


print('餐桌因无法送达,只能邀请两个嘉宾')
name.pop()
name.pop()
name.pop()
name.pop()
for m in name:
	print('%s 你很受欢迎'%m)
print('')


del name[0]
del name[0]
print(name)












