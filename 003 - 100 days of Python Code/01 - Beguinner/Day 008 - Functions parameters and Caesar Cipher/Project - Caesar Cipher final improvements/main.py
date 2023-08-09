import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo.logo)


#  Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(entry_text, shift_amount, caesar_direction):
    converted_text = ""
    if caesar_direction == "decode":
        shift_amount *= -1
    for letter in entry_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = (position + shift_amount) % 26
            converted_text += alphabet[shifted_position]
        else:
            converted_text += letter
    print(f"The {caesar_direction}d text is: {converted_text }")


# Loop the program
end_program = False
while not end_program:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #  Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(text, shift, direction)
    ending = input(
        "Do you want to continue the program? Type 'yes' if so, or 'no' if you want to finish it. ")
    if ending == "no":
        end_program = True
        print("Finishing the execution")
