import random
#https://www.geeksforgeeks.org/python-multiple-indices-replace-in-string/
print("H A N G M A N")
list_names = ['python', 'java', 'kotlin', 'javascript']
word_1 = random.choice(list_names)
word_2 = "-" * (len(word_1))
temp_list = list(word_2)
count = 8
while count > 0:
  letter = input(f"\n{str(word_2)}\nInput a letter:")
  count -= 1
  index_1 = [str(i) for i, e in enumerate(word_1) if e == letter]  
  for index_num in index_1:
    temp_list[int(index_num)] = letter
    word_2 = "".join(temp_list)
  if letter not in list(word_1) and count > 0:
    print("The letter dosen't apear in the word")
  #elif letter not in list(word_1) and count == 0:
    #print("The letter dosen't apear in the word")
    #print("\nThanks for playing!\nWe'll see how well you did in the next stage")
  elif count == 0:
      break
      print()
print("\nThanks for playing!\nWe'll see how well you did in the next stage")