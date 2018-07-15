i = 1
j_sum = 0
o_sum = 0
all_sum = 0
while  i <100:
	if i%2 != 0:
		j_sum = j_sum + i
	elif i%2 == 0:
		o_sum = o_sum + i
	i+=1
all_sum = all_sum + j_sum - o_sum
print("1-2+3-4+5.....+99得和是%d"%all_sum)
