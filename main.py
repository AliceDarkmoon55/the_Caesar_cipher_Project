answer = input('If you want to encode, enter 1. If you want to decode, enter 2.\n')
if answer == '1':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    k = int(input('enter cipher key: '))
    phrase = input('enter phrase only with small letters: ').strip()
    text = ''
    for i in phrase:
        text = text + alphabet[(alphabet.index(i) + k) % len(alphabet)]
    print(text + '\n')
elif answer == '2':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    k = int(input('enter cipher key: '))
    phrase = input('enter phrase only with small letters: ').strip()
    text = ''
    for i in phrase:
        text = text + alphabet[(alphabet.index(i) - k) % len(alphabet)]
    print(text + '\n')
else:
    print('There is no such command. Please try again')

