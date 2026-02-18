word=input("Enter a word in camel case: ")
word_in_snk=""

for _ in range (len(word)):
    if 65 < ord(word[_]) < 90 :
        word_in_snk = word_in_snk + "_" + word[_].lower()
    else: 
        word_in_snk = word_in_snk + word[_]

print(word_in_snk)
