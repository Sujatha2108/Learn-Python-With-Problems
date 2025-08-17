def isomorphic(s1,s2):
    if len(s1)!=len(s2):
       return False
    s1_to_s2_map ={}
    s2_to_s1_map ={}
    for i in range(len(s1)):
        char_s1=s1[i]
        char_s2=s2[i]
        if char_s1 in s1_to_s2_map:
            if s1_to_s2_map[char_s1] != char_s2:
                return False
        else:
            s1_to_s2_map[char_s1]=char_s2
        if char_s2 in s2_to_s1_map:
            if s2_to_s1_map[char_s2] != char_s1:
                return False
        else:
            s2_to_s1_map[char_s2]=char_s1
    return True
str1=input("Enter 1st String:")
str2=input("Enter 2nd String:")
if isomorphic(str1,str2):
    print("The strings are isomorphic ")
else:
    print("The Strings are not isomorphic")
        