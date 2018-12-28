try:
    print('If you want to encode, enter natural number. If you want to decode, number less zero.\n')
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    k = int(input('enter cipher key: '))
except ValueError:
    print('It isn\'t an integer number. Please try again')
try:
    phrase = input('enter phrase only with small letters: ').strip()
    text = ''
    for i in phrase:
        text = text + alphabet[(alphabet.index(i) + k) % len(alphabet)]
    print(text + '\n')
except ValueError:
    print('It isn\'t a text. Please try again')