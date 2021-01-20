import random
#https://www.geeksforgeeks.org/python-multiple-indices-replace-in-string/
print("H A N G M A N\n\n")
list_names = ['python', 'java']  #'kotlin', 'javascript']
word_1 = random.choice(list_names)
word_2 = "-" * (len(word_1))
temp_list = list(word_2)
count = 0
while count < 3:
  letter = input(f"{str(word_2)}\nInput a letter:")
  count += 1
  index_1 = [str(i) for i, e in enumerate(word_1) if e == letter]  
  for index_num in index_1:
    temp_list[int(index_num)] = letter
    word_2 = "".join(temp_list)
  if letter not in list(word_1) and count < 3:
    print("The letter dosen't apear in the word\n")
  elif count == 3:
    print("Thanks for playing!\nWe'll see how well you did in the next stage\n")
    
#print(word_2)
#print(word_2[:index_1] + letter + word_2[(index_1+1):])
        #count += 1
#print(word_2.replace(word_2[index_1], letter))
#elif count == 9:
#print("Thanks for playing! We'll see how well you did in the next stage")
#else:

#print("The letter dosen't apear in the word")
