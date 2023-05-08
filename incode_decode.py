alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


<<<<<<< HEAD
def encode():
    pass


def decode():
    pass
=======
# password = ''.join(password_list)   list.index(elmnt)


def encode(tex, shifft):
    new_en = []
    for i in range(0, len(tex)):
        if tex[i] == " ":
            new_en.append(tex[i])
            continue
        a = alphabet.index(tex[i])
        if a + shifft >= len(alphabet):
            new_en.append(alphabet[(a + shifft) - len(alphabet)])
        else:
            new_en.append(alphabet[a + shifft])
    encoded = "".join(new_en)
    print(encoded)


def decode(tex, shifft):
    new_de = []
    for i in range(0, len(tex)):
        if tex[i] == " ":
            new_de.append(tex[i])
            continue
        a = alphabet.index(tex[i])
        new_de.append(alphabet[a - shifft])
    decoded = "".join(new_de)
    print(decoded)
>>>>>>> 5a986e2 (11:45)


condition = True
while condition:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
<<<<<<< HEAD
        encode()
    elif direction == "decode":
        decode()
    conn = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if conn == 'no':
        condition = False
























=======
        encode(tex=text, shifft=shift)
    elif direction == "decode":
        decode(tex=text, shifft=shift)
    conn = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if conn == 'no':
        condition = False
>>>>>>> 5a986e2 (11:45)
