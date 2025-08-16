def anagaram_Check(string1,string2):
    word1=sorted(string1)
    word2=sorted(string2)
    if word1==word2:
        print("The given Two strings are Anagrams ")
    else:
        print("The given Two strings are not Anagrams ")
s1=input("Enter the first string :")
s2=input("Enter the second string :")
anagaram_Check(s1,s2)
