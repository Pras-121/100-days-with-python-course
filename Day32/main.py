
import pandas as pd
import random
import smtplib as smtp
import datetime as dt


def gen_letter(recv_name):
    file_path = "letter_templates"+"\\"+ f"letter_{random.randint(1, 3)}.txt"
    with open(file_path, 'r') as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", str(recv_name))
        return contents
        # letter_list = ['letter_1.txt','letter_3.txt','letter_3.txt']
        # chc = random.choice(letter_list)
        # lines = letter.readlines(), use .read() instead
        # for line in lines:
        #     mod_line = line.replace("[NAME]", str(recv_name))
        #     out_letter.append(mod_line)
        #     # print(str(mod_line))


def send_mail(recv_mailId, msgText):
    MY_EMAIL = "prasannaragav29@gmail.com"
    PASSKEY = "uypazguixpssrxls"
    with smtp.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSKEY)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recv_mailId,
            msg=f"Subject:Happy Birthday\n\n {msgText}"

        )


df = pd.read_csv('birthdays.csv')
system_date = dt.datetime.now()
today_month = system_date.month
today_day = system_date.day

for index, record in df.iterrows():
    if record.month == today_month and record.day == today_day:
        msgbody = gen_letter(record["name"])
        print(msgbody)
        send_mail(record.email, msgbody)




