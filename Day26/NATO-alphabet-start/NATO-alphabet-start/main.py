student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
nato_csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# df = pandas.DataFrame(nato_csv)
#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


nato_dict = {row.letter:row.code for (index,row) in nato_csv_data.iterrows()}
# print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a string:  ")
str_list = [letter for letter in user_input]
# print(str_list)
result_list = [nato_dict[letter.upper()] for letter in str_list]
# result_list = []
# for letter in str_list:
#     result_list.append(nato_dict[letter.upper()])
print(result_list)


