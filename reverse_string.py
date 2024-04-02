def reverse_string(sentence):
    words = sentence.split()
    
    stack = []
    for word in words:
        stack.append(word)
        
    reversed_sentence = ""
    while stack:
        reversed_sentence += stack.pop() + " "
        
    return reversed_sentence.rstrip()
    
sentence = input().strip()

print(reverse_string(sentence))
