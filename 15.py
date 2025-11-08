sentence = input("Enter a sentence: ")
if not sentence:
    print("not a sentence")
else:
     words = sentence.split()
     print("number of words"len(words))