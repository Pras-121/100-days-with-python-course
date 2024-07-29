import pandas as pd
df = pd.read_csv("./squireldata_2018.csv")
# print(df)
distinct_colors = df["Primary Fur Color"].unique().tolist()
distinct_colors.remove(distinct_colors[0])
new_df = df["Primary Fur Color"]
# print('*******')
# print(new_df[new_df == 'Gray'])
# print(new_df[new_df == 'Cinnamon'])
# print(new_df[new_df == 'Black'])
# print('*******')
lst= []
for color in distinct_colors:
    lst.append(new_df[new_df == color].count())
        # print(f"Color: {color}")
        # countlst.append([df['Primary Fur Color'] == color].count())
# print(lst)
new_dict ={
    'Fur color': distinct_colors,
    'count': lst
}
new_df = pd.DataFrame(new_dict)
new_df.to_csv('squirrelcolor.csv')
