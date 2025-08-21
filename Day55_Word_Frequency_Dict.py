from collections import Counter
import string
def frequency(text):
    clean_text=text.lower().translate(str.maketrans("","",string.punctuation))
    words=clean_text.split()
    freq=Counter(words)
    return freq
user_text=input("Enter a text:")
freq=frequency(user_text)
print(f"frequency of words:{freq}")