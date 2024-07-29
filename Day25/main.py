# with open("weatherdata.csv") as infile:
#     data =infile.readlines()
# print(data)

# import csv
# with open("weatherdata.csv") as infile:
#     data = csv.reader(infile)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
# print(temperature)

import pandas

data  = pandas.read_csv("weatherdata.csv")
# print(data['temp'])
# print(data['temp'].mean())
# temp_list = data['temp'].to_list()
# print(temp_list)
# sum = 0
# for temp in temp_list:
#     sum += temp
# temp_avg = sum / len(temp_list)
# print(data['temp'].max())

##
# print(data['condition'])
# print(data.condition)
##

# print(data[data.temp ==data.temp.max()])
# monday_temp = data.temp[data.day == "Monday"]
# temp_in_f = monday_temp * 9/5 + 32
# print(f"Temp in F: {monday_temp}")
##

## Data frame from dict
my_dict = {
    "student": ["Merkel", "Obama", "Al Savadaro"],
    "marks": [72, 80, 67]
}
df_data = pandas.DataFrame(my_dict)
print(df_data)
df_data.to_csv("dict.csv")
