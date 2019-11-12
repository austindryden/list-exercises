stringer = "abcdef"

print("Uppercase a String")
print(stringer.upper())

print("Capitalize a String")
print(stringer.capitalize())


def reverse(stringy):
    new_str = ""
    for i in range(len(stringy)):
        new_str += stringy[((i+1) * -1)]
    return new_str
print("Reverse a String")
print(reverse(stringer))


def leet(sentence):
    leet_list = ['O', "I", "R", 'E', 'A', 'S', 'G', 'T']
    new_word = []
    for letter in sentence:
        if letter.upper() in leet_list:
            new_word.append(str(leet_list.index(letter.upper())))
        else:
            new_word.append(letter)
    return ''.join(new_word)


print("leetspeak")
print(leet("hey heres is a sentence that is gonna get leeted up yo!"))

def longLong(word):
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    new_word = ''
    for i in range(len(word)-1):
        new_word += word[i]
        for vowel in vowel_list:
            if word[i].upper() == vowel and word[i+1].upper() == vowel:
                new_word += word[i] * 3
    new_word += word[-1]
    return new_word

print(longLong("Good"))
print(longLong("Cheese"))
print(longLong("man"))
print(longLong("oOolong"))
print(longLong("spoon"))
print(longLong("menefee"))

def caesar(sentence, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetl = list(alphabet.lower())
    alphabetu = list(alphabet.upper())
    new_word = ""
    for letter in sentence:
        try:
            if letter == letter.upper():
                new_word += alphabetu[((alphabetu.index(letter) + rot) % 26)]
            else:
                new_word += alphabetl[((alphabetl.index(letter) + rot) % 26)]
        except ValueError:
            new_word += letter
    return new_word

print(caesar("lbh zhfg hayrnea jung lbh unir yrnearq", 13))