import string
def pangram_check(sentence):
    alphabets=set(string.ascii_lowercase)
    letters=set(sentence.lower())
    return alphabets.issubset(letters)
s=input("Enter a sentence:")
if pangram_check(s):
    print("The given sentence is a Pangram")
else:
    print("The given sentence is NOT a Pangram")
    
