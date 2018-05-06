

def almost_equal(first , second):
	if len(first) < len(second):
		first, second = second , first

	len_diff = len(first) -len(second)
#need to find diffrence in length for the algo
	if len_diff > 1 :
		return False
#checking which character has changed, finding the index and checking if the string after that is equal
	elif len_diff == 0 :

		if first == second:
			return True
		
		for i in range(0,len(first)):
			if first[i] == second[i]:
				continue
			else:
				diff_char = i
				break

		new_first = first[:i] + first[i+1:]
		new_second = second[:i] + second[i+1:]

		if new_first == new_second:
			return True

		else:
			return False
#checking which character/characters have changed, removing the first changed character then comparing the remaining string
	elif len_diff == 1:
	
		for i  in range(0,len(second)):
			if first[i] == second[i]:
				continue
			else:
				diff_char = i
				break

		if i == len(second):
			return True
		else:
			new_first = first[:i] + first[i+1:]
			print(new_first)
			if new_first == second:
				return True
			else:
				return False




#result = almost_equal("pearl","perl")

#print(result)


