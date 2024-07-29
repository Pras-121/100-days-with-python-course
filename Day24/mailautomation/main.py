with open("mailcontent.txt") as letter:
    letter_contents = letter.read()

unread_lines = True
with open("invite_list.txt") as invite_list:
    names = invite_list.readlines()
    # while unread_lines:
    #     # name = invite_list.readline().strip()
    #     # print(f"Read line: {name}")
    #     if name != "":
    #         names.append(name)
    #         # print(names)
    #     else:
    #         unread_lines = False
# print(names)
for name in names:
    name = name.strip()
    new_letter = letter_contents.replace("[name]",name)
    with open(f"ReadyToSend/{name}_invite.txt", "w") as file:
        file.write(f"{new_letter}")


