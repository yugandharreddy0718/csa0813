def anagrams(word1,word2):
    word1 =word1.replace("","").lower()
    word2=word2.replace("","").lower()
    return sorted(word1)==sorted(word2)
word1=input("enter the first word:")
word2=input("enter the second word:")
if anagrams(word1,word2):
    print(" it is a anagram")
else:
    print(" not a anagram")
