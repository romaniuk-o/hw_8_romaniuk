from datetime import datetime, timedelta

# ______________________________________________________________________________
'''
Програма виводить дані про іменинників на наступні 7 днів, 
починаючи від поточної дати, але не включаючи її.
Дні народженняб які попадають на вихідні дні - виводяться в понеділок.

'''


# -----------Словник для перевірки ---------------------------------------------
users = [{'name': 'Hlib', 'birthday': '2020-05-23'},
         {'name': 'Varvara', 'birthday': '2020-05-17'},
         {'name': 'Anna', 'birthday': '2020-05-16'},
         {'name': 'Alex', 'birthday': '2020-06-20'},
         {'name': 'Nick', 'birthday': '2020-05-22'},
         {'name': 'Jack', 'birthday': '2020-05-19'}]
# ------------------------------------------------------------------------------


def get_birthdays_per_week(data):
    dic_7days = [datetime.today().date() + timedelta(days=i)
                 for i in range(1, 8)]
    dic = {}
    count = 1
    weekend_list = []
    for dic_7days_k in dic_7days:
        name_list = []
        for user in users:
            birth = datetime.strptime(user.get('birthday', ''), '%Y-%m-%d')
            if dic_7days_k.strftime('%m-%d') == birth.strftime('%m-%d'):
                if dic_7days_k.weekday() < 5:
                    name_list.append(user.get('name', ''))
                if (dic_7days_k.weekday() == 5) and count < 6:
                    weekend_list.append(user.get('name', ''))
                if (dic_7days_k.weekday() == 6) and count < 7:
                    weekend_list.append(user.get('name', ''))
                count += 1
            weekend_str = ', '.join(weekend_list)
            name_str = ', '.join(name_list)
        if len(name_str) != 0:
            dic.update({dic_7days_k.strftime('%A'): name_str})
    f = dic.get('Monday', '') + ", " + weekend_str
    dic['Monday'] = f
    # print(dic)
    for k, v in dic.items():
        print(k + ': ' + v)


get_birthdays_per_week(users)
