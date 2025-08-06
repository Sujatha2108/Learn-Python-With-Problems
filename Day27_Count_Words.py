def count_letters(word):
    word_count = 0
    for char in word:
        if char.isalpha():  
                word_count += 1
    return word_count


word=input("Enter a Word:")
letter_count = count_letters(word)
print(f"No of words: {letter_count}")

def count_Words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter a Sentence: ")
word_count = count_Words(sentence)
print(f"No of words: {word_count}")