def recursive_count_vowels(word):
    vowels="aeiouAEIOU"
    if word =="":
        return 0,0
    vowel_count,cons_count=recursive_count_vowels(word[1:])
    
    char=word[0]
    if char.isalpha():  
        if char in vowels:
            return vowel_count+1,cons_count
        else:
            return vowel_count,cons_count+1
    else:
        return vowel_count, cons_count


word=input("Enter a Word:")
vowels, consonants = recursive_count_vowels(word)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")