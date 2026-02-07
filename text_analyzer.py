def get_text():
    return input("Enter the text : ")

def count_characters(text):
    char=0
    for ch in text:
        char+=1
    return char

def count_words(text):
    l=text.split()
    return len(l)

def count_vowels(text):
    vowels_count=0
    for ch in text:
        if ch.lower() in "aeiou":
            vowels_count+=1
    return vowels_count

def longest_word(text):
    words=text.split()
    longest_word=words[0]
    for word in words:
        if len(word)>len(longest_word):
            longest_word=word
    return longest_word

def reversed_sentence(text):
    words=text.split()
    rev=[]
    for i in range(len(words)-1,-1,-1):
        rev.append(words[i])
    return " ".join(rev)
text=get_text()

print("Characters:", count_characters(text))
print("Words:", count_words(text))
print("Vowels:", count_vowels(text))
print("Longest word:", longest_word(text))
print("Reversed sentence:", reversed_sentence(text))
