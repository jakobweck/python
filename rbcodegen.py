import random
#number of codes desired
codes_to_gen = int(raw_input())
for i in range(0, codes_to_gen):
	#numbers usable in a code
	possible_numbers = [3,4,7]
	#two of these letters appear in every code
	possible_letters = ["C", "X", "K"]
	#randomly choose two letters, can be identical
	firstletter,secondletter = random.choice(possible_letters), random.choice(possible_letters)
	#init array to contain code
	code_array = []
	#append 8 numbers to the code from the three possibilities
	for i in range (0,8):
		code_array.append(random.choice(possible_numbers))
	#generate random index location to insert 1st letter
	letter_location_1 = random.randint(0,7)
	#create array without location 1 for the second location to be chosen from
	remaining_locs = range(0,8)
	remaining_locs.remove(letter_location_1)
	#choose location to insert 2nd letter
	letter_location_2 = random.choice(remaining_locs)
	#delete numbers at indices where letters will be inserted
	#then insert letter at that index
	#letter must be inserted immediately after deleting extraneous number
	#to ensure that reducing the length of the array doesn't result in the second del command
	#having an invalid index
	del code_array[letter_location_1]
	code_array.insert(letter_location_1,firstletter)
	del code_array[letter_location_2]
	code_array.insert(letter_location_2, secondletter)
	code = "".join(str(x) for x in code_array)
	print code
