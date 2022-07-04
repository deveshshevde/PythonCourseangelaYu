alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

en_de = input("type encode to encode and decode to decode")

shift = int(input("enter the shift number"))

string = input("enter the sentence").lower()


def encrypt(plainText, shift):
    coded_text = ""
    for letter in plainText:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        coded_text += new_letter
    print(f"the coded text is {coded_text}")


def decoder(plain_text,shift):
    decoded_text = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decoded_text += new_letter
    print(f"the decoded text is {decoded_text}")


if en_de == "encode":
    decoder(string, shift)

elif en_de == "decode":

    encrypt(string, shift)

else:
    print("choose correctly")
