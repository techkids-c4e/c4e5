while True:
    salary = [{"full_name":"Tran Quang Hiep",
               "class":"C4E",
               "rate":"$6.70",
               "session":17},
              {"full_name":"Nguyen Quang Huy",
               "class":"iOS",
               "rate":"$8.38",
               "session":18},
              {"full_name":"Nguyen Thanh Cuong",
               "class":"WEB",
               "rate":"$7.34",
               "session":19},
              {"full_name":"Ton Hong Duc",
               "class":"WEB",
               "rate":"$7.98",
               "session":18},
              {"full_name":"Tran Duc Hung",
               "class":"Android",
               "rate":"$5.62",
               "session":15}]
    def calculate_salary(rate, session):
        total_salary = float(rate.replace("$", "")) * float(session)
        return total_salary
    for person in salary:
        print(person['full_name'], 'taught', person['session'], 'sessions, salary: ', calculate_salary(person['rate'], person['session']))
    def print_salary():
        user_name = input('Please input your name: ')
        for person in salary:
            if user_name == person['full_name']:
                print (person['full_name'], "'s salary is", calculate_salary(person['rate'], person['session']))
    def add_info():
        x, y, z, t = input('Please input your information(name, class, rate, session): ').split()
        new_info = {'full_name': x,
                    'class': y,
                    'rate': z,
                    'session': t}
        salary.append(new_info)
        print('Your information has been added')
        for person in salary:
            print(person)
    def update_info():
        x, y, z, t = input('Please input your updated information(name, class, rate, session): ').split()
        updated_info = {'full_name': x,
                        'class': y,
                        'rate': z,
                        'session': t}
        for person in salary:
            if person['full_name'] == x:
                person['class'] = y
                person['rate'] = z
                person['session'] = t
                print('Your information has been updated')
            else:
                print('No information related to', x, 'found, information not updated')
            print(person)
    def delete_info():
        user_name = input('Please input the name to be deleted: ')
        for person in salary:
            if user_name == person['full_name']:
                salary.remove(person)
                print('Information removed')
            else:
                print('No such information')
        print(person)
    selection = input('''
    1. View
    2. Add
    3. Update
    4. Delete
    Please select option: ''')
    while True:
        if selection == '1':
            print_salary()
        elif selection == '2':
            add_info()
        elif selection == '3':
            update_info()
        elif selection == '4':
            delete_info()
        else:
            print('Please reselect')
        break
