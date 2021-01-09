#this program is to create basic translator in which we would be
#converting any vowels in given word into some other letter like "g"
#vowels -> g
#-----examaples-------
#dog -> dgg
#cat -> cgt

def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))



#other version in which we would take care of user entered uppercase letters
def translate1 (phrase):
    translation1 = ""
    for letter1 in phrase:
        if letter1.lower() in "aeiou":
            if letter1.isupper():
                translation1 = translation1 + "G"
            else:
                translation1 = translation1 + "g"
        else:
            translation1 = translation1 + letter1
    return translation1

print(translate1(input("Enter a phrase: ")))
