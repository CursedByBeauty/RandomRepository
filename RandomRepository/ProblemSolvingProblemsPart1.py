
def reverse_a_string():

    word = 'Hello'

    reversed_word = word[len(word) -1]

    reversed_word = ''

    for index in range(len(word) -1, -1, -1):
        reversed_word += word[index]
    print(reversed_word)
reverse_a_string()

def capping_my_string():
    the_string = ['this ', 'is ', 'cool!']
    print(the_string[0].capitalize() + the_string[1].capitalize() + the_string[2].capitalize())
capping_my_string()

def compressing_my_string():
    pls_compress = "aaabbbbbccccaacccbbbaaabbbaaa"

    first_letters = pls_compress[0:3]
    second_letters = pls_compress[3:8]
    third_letters = pls_compress[8:12]
    fourth_letters = pls_compress[12:14]
    fifth_letters = pls_compress[14:17]
    sixth_letters = pls_compress[17:20]
    seventh_letters = pls_compress[20:23]
    eighth_letters = pls_compress[23:26]
    ninth_letters = pls_compress[26:29]

    print(len(first_letters), end = 'a')
    print(len(second_letters), end = 'b')
    print(len(third_letters), end = 'c') 
    print(len(fourth_letters), end = 'a')
    print(len(fifth_letters), end = 'c')
    print(len(sixth_letters), end = 'b') 
    print(len(seventh_letters), end = 'a')
    print(len(eighth_letters), end = 'b') 
    print(len(ninth_letters), end = 'a')
    print()
    print()
compressing_my_string()

def palindrome():
    word = input("Type a word you want to be reversed: ")

    reversed_word = word[len(word) -1]

    reversed_word = ''

    for index in range(len(word) -1, -1, -1):
        reversed_word += word[index]

    print(reversed_word)

    if word[::-1] == (reversed_word[::-1]):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")

palindrome()














