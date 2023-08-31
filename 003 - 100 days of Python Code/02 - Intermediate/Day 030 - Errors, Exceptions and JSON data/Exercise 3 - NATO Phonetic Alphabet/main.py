# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
from os import path

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}


# Function to get the directory of the path
# So files won't be read/written from the root directory (machinelarningground)
def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


# Looping through dictionaries:
for key, value in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv(dir("nato_phonetic_alphabet.csv"))
# we don't use the index, so "_" is used in the compreheension per convention
alphabet_dict = {row.letter: row.code for (_, row) in nato_data.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    try:
        user_input = input(
            "Which word would you like converted in the NATO Alphabet? "
        )
        nato_word = [alphabet_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed")
    else:
        break

print(nato_word)
