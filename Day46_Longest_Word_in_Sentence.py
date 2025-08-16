def longest_word(sentence):
    words=sentence.split()
    longest=max(words,key=len)
    return longest,len(longest)
s = input("Enter a sentence: ")
word, length = longest_word(s)
print(f"The longest word is '{word}' with length {length}")
