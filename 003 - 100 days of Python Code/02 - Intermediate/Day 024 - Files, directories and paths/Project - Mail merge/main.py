from os import path

PLACEHOLDER = "[name]"

# Create a letter using starting_letter.txt
with open(
    path.join(path.dirname(__file__), "Input/Letters/starting_letter.txt"), "r"
) as base_letter:
    starting_letter = base_letter.read()
# for each name in invited_names.txt
with open(
    path.join(path.dirname(__file__), "Input/Names/invited_names.txt"), "r"
) as base_names:
    names_list = base_names.read().splitlines()

for name in names_list:
    # Replace the [name] placeholder with the actual name.
    new_letter = starting_letter.replace("[name]", name)
    # Save the letters in the folder "ReadyToSend".
    with open(
        path.join(path.dirname(__file__), f"Output/ReadyToSend/{name}.txt"),
        "w",
    ) as new_file:
        new_file.write(new_letter)


# Hint1: : https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2:  you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: : https://www.w3schools.com/python/ref_string_strip.asp
