separator = " "
sentence = ""
while True:
    word = input("Give me a word or press '.' to exit: ")
    if word == ".":
        break
    sentence += f"{word}{separator}"
print(f"The given sentence is: {sentence}\nThe sentence contains {sentence.count(separator)} words")
