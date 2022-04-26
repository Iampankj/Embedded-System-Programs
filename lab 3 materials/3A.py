def caeser(msg, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet1 = alphabet + alphabet.upper()
    new_message = ""
    for c in msg:
        position = alphabet1.find(c)
        new_position = (position+key)%len(alphabet1)
        new_character = alphabet1[new_position]
        new_message += new_character
    return new_message
key = 3
while True:
    message = input('Please enter a message: ')
    if message == 'q':break
    encry_message = caeser(message, key)
    print('Encrypted message: ',encry_message)
    