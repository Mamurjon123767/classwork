sentence = input("Enter a sentence: ")
if not sentence:
    print("Error: You didn't enter a sentence.")
else:
     words = sentence.split()
     print("Total number of words:", len(words))