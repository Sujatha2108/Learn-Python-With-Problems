from collections import Counter
def char_Frequency(S):
    return Counter(S)
S=input("Enter a String:")
char_counts=char_Frequency(S)
print(char_counts)