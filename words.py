input_words = input().split(",")
real_dict={}
for word in input_words:
  first_char = word[0]
  if first_char not in real_dict:
    real_dict[first_char] = []
  real_dict[first_char].append(word)  
