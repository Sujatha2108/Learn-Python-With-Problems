import string
def remove_Punctuation():
    text=input()
    translator= str.maketrans('','',string.punctuation)
    clean_text=text.translate(translator)
    print(clean_text)
remove_Punctuation()