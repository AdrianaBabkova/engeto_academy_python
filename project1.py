'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
         red, purple, yellow and gray beds of the Wasatch 
         Formation. Eroded portions of these horizontal 
         beds slope gradually upward from the valley floor 
         and steepen abruptly. Overlying them and extending 
         to the top of the butte are the much steeper 
         buff-to-white beds of the Green River Formation, 
         which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
         a portion of the largest deposit of freshwater fish 
         fossils in the world. The richest fossil fish deposits 
         are found in multiple limestone layers, which lie some 
         100 feet below the top of the butte. The fossils 
         represent several varieties of perch, as well as 
         other freshwater genera and herring similar to those 
         in modern oceans. Other fish such as paddlefish, 
         garpike and stingray are also present.'''
         ]

credentials = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}
print('Welcome dear user in our app.')

# Ask user to input username and password
username = input('Please enter your username: ')
password = input('Please enter your password: ')
separator = '-' * 35

# validate the username and password and match them
if credentials.get(username) != password:
    print('You have entered incorrect username and password')

elif credentials.get(username) == password:
    print('Password and username entered are among registered credentials')

print(separator)

# ask user to select the text which will be analyzed
text_input = input('We have 3 texts to be analyzed.\nEnter a number btw. 1 and 3 to select: ')

# validate the input:
# 1.numeric only input
if not text_input.isnumeric():
    print('The entered number must be a number only and between 1-3')

# 2. in a range (1-3)
idx = int(text_input)
if not (1 <= idx <= 3):
    print('The entered number must be between 1 - 3')

# Choose the text from user selection
txt = TEXTS[idx - 1]

# fragment the text into words
text_words = txt.split()

# analyze the text
count_word = 0
capital_letter = 0
uppercase = 0
lowercase = 0
numeric_only = 0
sum_numeric = 0
unique_length = 0

length_dict = {}

for word in text_words:
    count_word += 1

    # increment the number of words with the same length
    ln = len(word)

    if word.istitle():
        capital_letter += 1
    if word.isupper():
        uppercase += 1
    if word.islower():
        lowercase += 1
    if word.isnumeric():
        numeric_only += 1
        sum_numeric += int(word)
    if not (ln in length_dict.keys()):
        length_dict[ln] = 1
    else:
        length_dict[ln] += 1

print(f" Total amount of word: {count_word}")
print(f" Amount of words with capital letter: {capital_letter}")
print(f" Amount of words with uppercase letter: {uppercase}")
print(f" Amount of words with lowercase letter: {lowercase}")
print(f" Amount of numeric only words: {numeric_only}")
print(f" The sum of all the numeric words in the given text: {sum_numeric}")


sort = sorted(length_dict)

for key in sort:
    value = length_dict[key]
    stars = value * '*'
    print(key, stars, value)
