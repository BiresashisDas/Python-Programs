# Author :- Biresashis Das

# Here I will show you how to 'encode' and 'decode' a message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shift_amount, cipher_direction):
    plain_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            plain_text += alphabet[new_position]
        else:
            plain_text += char

    print(f"Your {cipher_direction}d text is {plain_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caeser(start_text = text, shift_amount = shift, cipher_direction = direction)

    result = input("Type 'yes' for continue and 'no' for stop.\n")
    if result == "no":
        should_continue = False
        print("The program is stopped.")
        
        
        


#     SAMPLE OUTPUT

#     Type 'encode' to encrypt, type 'decode' to decrypt:
#     encode
#     Type your message:
#     hello
#     Type the shift number:
#     4
#     Your encoded text is lipps
#     Type 'yes' for continue and 'no' for stop.
#     yes
#     Type 'encode' to encrypt, type 'decode' to decrypt:
#     decode
#     Type your message:
#     lipps
#     Type the shift number:
#     4
#     Your decoded text is hello
#     Type 'yes' for continue and 'no' for stop.
#     no
#     The program is stopped.

#     Process finished with exit code 0
